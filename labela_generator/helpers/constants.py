from enum import Enum


class Components(Enum):
    REPOSITORIES = 'repository'
    MODELS = 'model'
    SERVICES = 'service'
    VIEWS = 'view'
    SCAFFOLD = 'scaffold'
    ROUTES = 'route'
    CONTAINERS = 'container'
    BASE = 'base'


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
            Components.SERVICES.value
        ]
    }


class TemplateName(Enum):
    REPOSITORY = 'repository.py.mako'
    MODEL = 'model.py.mako'
    ROUTES = 'routes.py.mako'
    VIEW = 'view.py.mako'
    SERVICE = 'service.py.mako'
    SERVICE_CONTAINER = 'service_container.py.mako'
    REPO_CONTAINER = 'repository_container.py.mako'
    BASE_SERVICE = 'service_base.py.mako'
    BASE_REPO = 'repository_base.py.mako'


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
