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
from labela_generator.templates.routes import routes_template_path
from labela_generator.templates.services import service_template_path
from labela_generator.templates.views import view_template_path


def model(config: Config, model_path: str) -> None:
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


def service(config: Config, service_path: str) -> None:
    template_location = path.join(
        service_template_path, TemplateName.SERVICE.value
    )
    services_folder = config.get_component(Components.SERVICES.value)
    repositories_folder = config.get_component(Components.REPOSITORIES.value)
    file_from_template(
        template_location, service_path,
        services_folder=services_folder,
        repositories_folder=repositories_folder,
        project=config.project_name(),
        model_name=config.get_resource_name(),
        model_class_name=config.get_resource_name().capitalize()
    )

    _add_container(
        config,
        TemplateName.SERVICE_CONTAINER.value,
        Components.SERVICES.value
    )

    _add_base(
        config,
        service_template_path,
        TemplateName.BASE_SERVICE.value,
        services_folder
    )


def repository(config: Config, repo_path: str) -> None:
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

    _add_container(
        config,
        TemplateName.REPO_CONTAINER.value,
        Components.REPOSITORIES.value
    )

    _add_base(
        config,
        repository_template_path,
        TemplateName.BASE_REPO.value,
        repositories_folder
    )


def view(config: Config, view_path: str) -> None:
    template_location = path.join(
        view_template_path, TemplateName.VIEW.value
    )
    services_folder = config.get_component(Components.SERVICES.value)
    containers_folder = config.get_component(Components.CONTAINERS.value)
    file_from_template(
        template_location, view_path,
        services_folder=services_folder,
        containers_folder=containers_folder,
        project=config.project_name(),
        model_name=config.get_resource_name(),
        model_class_name=config.get_resource_name().capitalize()
    )

    _add_routes(config)


def _add_routes(config: Config) -> None:
    template_location = path.join(
        routes_template_path, TemplateName.ROUTES.value
    )
    routes_path = Config.find_file(
        Components.ROUTES.value, root=config.project_path()
    )

    append_template_to_file(
        template_location, routes_path,
        class_name=config.get_resource_name(),
        model_name=config.get_resource_name(),
        model_class_name=config.get_resource_name().capitalize()
    )


def _add_container(config: Config, template: str, component: str) -> None:
    container_template_location = path.join(
        container_template_path, template
    )
    container_path = Config.find_file(
        component,
        root=config.project_path(),
        folder_path=Config.find_component(config.project_path(), Components.CONTAINERS.value)
    )
    append_template_to_file(
        container_template_location, container_path,
        model_name=config.get_resource_name(),
        model_class_name=config.get_resource_name().capitalize()
    )


# TODO: Base generation in different package
def _add_base(config, template_path, template, goal_path):
    base_template_location = path.join(
        template_path, template
    )
    base_path = path.join(
        config.project_path(),
        goal_path,
        Components.BASE.value + '.py'
    )
    if not Config.find_file(base_path):
        file_from_template(base_template_location, base_path)
