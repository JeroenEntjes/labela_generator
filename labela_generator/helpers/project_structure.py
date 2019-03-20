import os, sys
from typing import Tuple
from pathlib import Path


def project_root():
    path = Path(__file__).parent.parent
    return path


def find_paths(name: str) -> Tuple[str, str, str]:
    root = project_root()
    models_path = os.path.join(
        find_component_path(root, 'model'), name + '.py'
    )
    repositories_path = os.path.join(
        find_component_path(root, 'repository'), name + '.py'
    )

    services_path = os.path.join(
        find_component_path(root, 'service'), name + '.py'
    )
    return models_path, repositories_path, services_path


def find_component_path(root: str, component: str) -> str:
    path = os.path.join(root, component)
    if os.path.isdir(path):
        return os.path.join(path)
    path = path + 's'
    if os.path.isdir(path):
        return os.path.join(path)
    path = path[:-1] + 'ies'
    if path:
        return os.path.join(path)
    else:
        # TODO: Exception?
        print('Cannot locate {component} folder!'.format(component=component))
        sys.exit(1)
