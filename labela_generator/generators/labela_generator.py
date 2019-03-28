from typing import Dict, List

import click

from labela_generator.generators import generators
from labela_generator.helpers.constants import ComponentsContains
from labela_generator.helpers.config import Config


class LabelAGenerator:
    def __init__(self, config: Config) -> None:
        self._config = config

    def generate(self, component: str, y: bool) -> None:
        components = ComponentsContains.MAPPING.value[component]
        if not components:
            # TODO: Exception
            print('Exception: Unknown operation')
            return

        components_and_paths = self._generate_paths(components)
        if not components_and_paths:
            click.echo('Nothing to generate')
            return
        if y or click.confirm("Continue?"):
            self._generate_files(components_and_paths)
        else:
            click.echo('Cancelled by user')
            return

    def _generate_paths(self, components: List) -> Dict[str, str]:
        component_paths = self._config.find_components_path(
            components=components
        )
        components_to_add = {}
        for component, component_path in component_paths.items():
            if self._config.find_file(component_path):
                # TODO: Exception raising / file replace?
                print('Exception: File {path} already exists, '
                      'skipping...'.format(path=component_path))
                continue

            click.echo(
                "About to generate file {full_path}".format(
                    full_path=component_path
                )
            )
            components_to_add[component] = component_path
        return components_to_add

    def _generate_files(self, components_and_paths: Dict) -> None:
        for component, path in components_and_paths.items():
            generator = getattr(generators, component)
            generator(self._config, components_and_paths[component])
