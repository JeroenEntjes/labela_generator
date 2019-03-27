"""
View from template
"""
from typing import Dict

from pyramid.view import view_config, view_defaults

from ${project}.${containers_folder}.${services_folder} import Services
from ${project}.${services_folder}.${model_name} import ${model_class_name}Service


@view_defaults(renderer="json", permission="private")
class ${model_class_name}View:
    def __init__(self, request):
        self.request = request
        self._service = Services.${model_name}()  # type: ${model_class_name}Service

    @view_config(route_name='api.${model_name}s', request_method='POST')
    def create(self) -> Dict:
        params = self.request.json_body
        ${model_name} = self._service.create(**params)

        return {
            'success': True,
            'data': ${model_name}
        }

    @view_config(route_name='api.${model_name}', request_method='GET')
    def get(self) -> Dict:
        ${model_name}_id = self.request.matchdict['id']
        ${model_name} = self._service.get(${model_name}_id)

        return {
            'success': True,
            'data': ${model_name}
        }

    @view_config(route_name='api.${model_name}s', request_method='GET')
    def list(self) -> Dict:
        ${model_name}s = self._service.list()

        return {
            'success': True,
            'data': ${model_name}s
        }

    @view_config(route_name='api.${model_name}', request_method='PATCH')
    def update(self) -> Dict:
        ${model_name}_id = self.request.matchdict['id']
        params = self.request.json_body
        ${model_name} = self._service.update(${model_name}_id)

        return {
            'success': True,
            'data': ${model_name}
        }

    @view_config(route_name='api.${model_name}', request_method='DELETE')
    def delete(self) -> Dict:
        ${model_name}_id = self.request.matchdict['id']
        self._service.delete(${model_name}_id)

        return {
            'success': True,
            'data': None
        }
