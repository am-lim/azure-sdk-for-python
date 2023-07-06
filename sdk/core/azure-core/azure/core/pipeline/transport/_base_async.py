# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import asyncio
import abc
from collections.abc import AsyncIterator
from typing import AsyncIterator as AsyncIteratorType, TypeVar, Generic
from contextlib import AbstractAsyncContextManager

from ._base import (
    _HttpResponseBase,
    _HttpClientTransportResponse,
)
from ...utils._pipeline_transport_rest_shared_async import _PartGenerator

AsyncHTTPResponseType = TypeVar("AsyncHTTPResponseType")
HTTPResponseType = TypeVar("HTTPResponseType")
HTTPRequestType = TypeVar("HTTPRequestType")


class _ResponseStopIteration(Exception):
    pass


def _iterate_response_content(iterator):
    """To avoid the following error from Python:
    > TypeError: StopIteration interacts badly with generators and cannot be raised into a Future

    :param iterator: An iterator
    :type iterator: iterator
    :return: The next item in the iterator
    :rtype: any
    """
    try:
        return next(iterator)
    except StopIteration:
        raise _ResponseStopIteration()  # pylint: disable=raise-missing-from


class AsyncHttpResponse(_HttpResponseBase, AbstractAsyncContextManager):  # pylint: disable=abstract-method
    """An AsyncHttpResponse ABC.

    Allows for the asynchronous streaming of data from the response.
    """

    def stream_download(self, pipeline, **kwargs) -> AsyncIteratorType[bytes]:
        """Generator for streaming response body data.

        Should be implemented by sub-classes if streaming download
        is supported. Will return an asynchronous generator.

        :param pipeline: The pipeline object
        :type pipeline: azure.core.pipeline.Pipeline
        :keyword bool decompress: If True which is default, will attempt to decode the body based
            on the *content-encoding* header.
        :return: An async iterator of bytes
        :rtype: AsyncIterator[bytes]
        """
        raise NotImplementedError("stream_download is not implemented.")

    def parts(self) -> AsyncIterator:
        """Assuming the content-type is multipart/mixed, will return the parts as an async iterator.

        :return: An async iterator of the parts
        :rtype: AsyncIterator
        :raises ValueError: If the content is not multipart/mixed
        """
        if not self.content_type or not self.content_type.startswith("multipart/mixed"):
            raise ValueError("You can't get parts if the response is not multipart/mixed")

        return _PartGenerator(self, default_http_response_type=AsyncHttpClientTransportResponse)

    async def __aexit__(self, exc_type, exc_value, traceback):
        return None


class AsyncHttpClientTransportResponse(  # pylint: disable=abstract-method
    _HttpClientTransportResponse, AsyncHttpResponse
):
    """Create a HTTPResponse from an http.client response.

    Body will NOT be read by the constructor. Call "body()" to load the body in memory if necessary.

    :param HttpRequest request: The request.
    :param httpclient_response: The object returned from an HTTP(S)Connection from http.client
    """


class AsyncHttpTransport(
    AbstractAsyncContextManager,
    abc.ABC,
    Generic[HTTPRequestType, AsyncHTTPResponseType],
):
    """An http sender ABC."""

    @abc.abstractmethod
    async def send(self, request: HTTPRequestType, **kwargs) -> AsyncHTTPResponseType:
        """Send the request using this HTTP sender.

        :param request: The request object. Exact type can be inferred from the pipeline.
        :type request: any
        :return: The response object. Exact type can be inferred from the pipeline.
        :rtype: any
        """

    @abc.abstractmethod
    async def open(self):
        """Assign new session if one does not already exist."""

    @abc.abstractmethod
    async def close(self):
        """Close the session if it is not externally owned."""

    async def sleep(self, duration: float) -> None:
        """Sleep for the specified duration.

        You should always ask the transport to sleep, and not call directly
        the stdlib. This is mostly important in async, as the transport
        may not use asyncio but other implementation like trio and they their own
        way to sleep, but to keep design
        consistent, it's cleaner to always ask the transport to sleep and let the transport
        implementor decide how to do it.
        By default, this method will use "asyncio", and don't need to be overridden
        if your transport does too.

        :param float duration: The number of seconds to sleep.
        """
        await asyncio.sleep(duration)
