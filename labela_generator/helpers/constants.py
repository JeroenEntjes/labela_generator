from enum import Enum


class Components(Enum):
    REPOSITORIES = 'repositories'
    MODELS = 'models'
    SERVICES = 'services'
    VIEWS = 'views'
    SCAFFOLD = 'scaffold'
    ROUTES = 'routes'
    CONTAINERS = 'containers'


class ComponentsContains(Enum):
    MAPPING = {
        Components.MODELS.value: [
            Components.MODELS.value
        ],
        Components.VIEWS.value: [
            Components.VIEWS.value
        ],
        Components.REPOSITORIES.value: [
            Components.REPOSITORIES.value
        ],
        Components.SERVICES.value: [
            Components.SERVICES.value
        ],
        Components.SCAFFOLD.value: [
            Components.REPOSITORIES.value,
            Components.MODELS.value,
            Components.VIEWS.value,
            Components.SERVICES.value,
            Components.CONTAINERS.value
        ]
    }


class TemplateName(Enum):
    REPOSITORY = 'repository.py.mako'
    MODEL = 'generators.py.mako'
    ROUTES = 'routes.py.mako'
    SERVICE = 'services.py.mako'
    SERVICE_CONTAINER = 'service_container.py.mako'
    REPO_CONTAINER = 'repository_container.py.mako'


class Arguments(Enum):
    CONFIGFILE = '-c'
    PROMPTYES = '-y'
    COMPONENT = 'component'
    NAME = 'name'


class ConfigOptions(Enum):
    FILENAME = 'lagen.ini'
    SECTION = 'lagen'

    ROOT = 'root'
    SKIP = 'never_generate'
    IGNOREBASE = 'ignore_base'
