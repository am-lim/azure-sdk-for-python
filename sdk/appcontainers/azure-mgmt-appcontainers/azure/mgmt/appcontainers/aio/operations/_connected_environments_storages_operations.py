# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._connected_environments_storages_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ConnectedEnvironmentsStoragesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.appcontainers.aio.ContainerAppsAPIClient`'s
        :attr:`connected_environments_storages` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def list(
        self, resource_group_name: str, connected_environment_name: str, **kwargs: Any
    ) -> _models.ConnectedEnvironmentStoragesCollection:
        """Get all storages for a connectedEnvironment.

        Get all storages for a connectedEnvironment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Environment. Required.
        :type connected_environment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectedEnvironmentStoragesCollection or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.ConnectedEnvironmentStoragesCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ConnectedEnvironmentStoragesCollection] = kwargs.pop("cls", None)

        request = build_list_request(
            resource_group_name=resource_group_name,
            connected_environment_name=connected_environment_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ConnectedEnvironmentStoragesCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/connectedEnvironments/{connectedEnvironmentName}/storages"
    }

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, connected_environment_name: str, storage_name: str, **kwargs: Any
    ) -> _models.ConnectedEnvironmentStorage:
        """Get storage for a connectedEnvironment.

        Get storage for a connectedEnvironment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Environment. Required.
        :type connected_environment_name: str
        :param storage_name: Name of the storage. Required.
        :type storage_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectedEnvironmentStorage or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.ConnectedEnvironmentStorage
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ConnectedEnvironmentStorage] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            connected_environment_name=connected_environment_name,
            storage_name=storage_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ConnectedEnvironmentStorage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/connectedEnvironments/{connectedEnvironmentName}/storages/{storageName}"
    }

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        storage_name: str,
        storage_envelope: _models.ConnectedEnvironmentStorage,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConnectedEnvironmentStorage:
        """Create or update storage for a connectedEnvironment.

        Create or update storage for a connectedEnvironment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Environment. Required.
        :type connected_environment_name: str
        :param storage_name: Name of the storage. Required.
        :type storage_name: str
        :param storage_envelope: Configuration details of storage. Required.
        :type storage_envelope: ~azure.mgmt.appcontainers.models.ConnectedEnvironmentStorage
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectedEnvironmentStorage or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.ConnectedEnvironmentStorage
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        storage_name: str,
        storage_envelope: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConnectedEnvironmentStorage:
        """Create or update storage for a connectedEnvironment.

        Create or update storage for a connectedEnvironment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Environment. Required.
        :type connected_environment_name: str
        :param storage_name: Name of the storage. Required.
        :type storage_name: str
        :param storage_envelope: Configuration details of storage. Required.
        :type storage_envelope: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectedEnvironmentStorage or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.ConnectedEnvironmentStorage
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        storage_name: str,
        storage_envelope: Union[_models.ConnectedEnvironmentStorage, IO],
        **kwargs: Any
    ) -> _models.ConnectedEnvironmentStorage:
        """Create or update storage for a connectedEnvironment.

        Create or update storage for a connectedEnvironment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Environment. Required.
        :type connected_environment_name: str
        :param storage_name: Name of the storage. Required.
        :type storage_name: str
        :param storage_envelope: Configuration details of storage. Is either a
         ConnectedEnvironmentStorage type or a IO type. Required.
        :type storage_envelope: ~azure.mgmt.appcontainers.models.ConnectedEnvironmentStorage or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectedEnvironmentStorage or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.ConnectedEnvironmentStorage
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConnectedEnvironmentStorage] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(storage_envelope, (IO, bytes)):
            _content = storage_envelope
        else:
            _json = self._serialize.body(storage_envelope, "ConnectedEnvironmentStorage")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            connected_environment_name=connected_environment_name,
            storage_name=storage_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ConnectedEnvironmentStorage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/connectedEnvironments/{connectedEnvironmentName}/storages/{storageName}"
    }

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, connected_environment_name: str, storage_name: str, **kwargs: Any
    ) -> None:
        """Delete storage for a connectedEnvironment.

        Delete storage for a connectedEnvironment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Environment. Required.
        :type connected_environment_name: str
        :param storage_name: Name of the storage. Required.
        :type storage_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            connected_environment_name=connected_environment_name,
            storage_name=storage_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/connectedEnvironments/{connectedEnvironmentName}/storages/{storageName}"
    }
