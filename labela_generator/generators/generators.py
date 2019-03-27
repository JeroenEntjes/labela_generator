from os import path

from labela_generator.helpers.config import Config
from labela_generator.helpers.constants import TemplateName, Components
from labela_generator.templates.containers import container_template_path
from labela_generator.templates.generate import (
    file_from_template,
    append_template_to_file
)
from labela_generator.templates.models import model_template_path
from labela_generator.templates.repositories import repository_template_path
from labela_generator.templates.services import service_template_path
from labela_generator.templates.views import (
    view_template_path, routes_template_path
)


def model(config, model_path: str) -> None:
    template_location = path.join(
        model_template_path, TemplateName.MODEL.value
    )
    models_folder = config.get_component(Components.MODELS.value)
    file_from_template(
        template_location, model_path,
        models_folder=models_folder,
        project=config.project_name(),
        model_class_name=config.get_resource_name().capitalize()
    )


def service(config, service_path: str) -> None:
    template_location = path.join(
        service_template_path, TemplateName.SERVICE.value
    )
    services_folder = config.get_component(Components.SERVICES.value)
    repositories_folder = config.get_component(Components.REPOSITORIES.value)
    file_from_template(
        template_location, service_path,
        services_folder=services_folder,
        repository_template_path=repositories_folder,
        project=config.project_name(),
        model_class_name=config.get_resource_name().capitalize()
    )

    _add_container(config, TemplateName.SERVICE_CONTAINER.value)


def repository(config, repo_path: str) -> None:
    template_location = path.join(
        repository_template_path, TemplateName.REPOSITORY.value
    )
    repositories_folder = config.get_component(Components.REPOSITORIES.value)
    models_folder = config.get_component(Components.MODELS.value)
    file_from_template(
        template_location, repo_path,
        repositories_folder=repositories_folder,
        models_folder=models_folder,
        project=config.project_name(),
        model_name=config.get_resource_name(),
        model_class_name=config.get_resource_name().capitalize()
    )

    _add_container(config, TemplateName.REPO_CONTAINER.value)


def view(config, view_path: str) -> None:
    template_location = path.join(
        view_template_path, TemplateName.VIEW.value
    )
    services_folder = config.get_component(Components.SERVICES.value)
    file_from_template(
        template_location, view_path,
        services_folder=services_folder,
        project=config.project_name(),
        model_name=config.get_resource_name(),
        model_class_name=config.get_resource_name().capitalize()
    )

    _add_routes(config, TemplateName.ROUTES.value)


def _add_routes(config, template):
    template_location = path.join(
        routes_template_path, TemplateName.ROUTES.value
    )
    routes_path = Config.find_file(root=Config.project_root(), file_name=)

    append_template_to_file(
        template_location, routes_path,
        project=config.project_name(),
        class_name=config.get_resource_name().capitalize()
    )

def _add_container(config, template):
    container_template_location = path.join(
        container_template_path, template
    )
    container_path = config.find_components_path(
        [Components.CONTAINERS.value]
    )[Components.CONTAINERS.value]
    append_template_to_file(
        container_template_location, container_path,
        model_name=config.get_resource_name(),
        model_class_name=config.get_resource_name().capitalize()
    )
