from typing import Dict, List

import click

from labela_generator import generators
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

        component_paths = self._generate_paths(components)
        if y or click.confirm("Continue?"):
            self._generate_files(components, component_paths)
        else:
            click.echo('Cancelled by user')
            return

    def _generate_paths(self, components: List) -> Dict[str, str]:
        component_paths = self._config.find_components_path(
            components=components
        )
        for component_path in component_paths:
            if self._config.find_file(path=component_path):
                # TODO: Exception raising / file replace?
                print('Exception: File already exists, skipping...')
                continue

            click.echo(
                "About to generate file {full_path}".format(
                    full_path=component_path
                )
            )
        return component_paths

    def _generate_files(self, components: List, component_paths: Dict) -> None:
        for component in components:
            generator = getattr(generators, component)
            generator(self._config, component_paths[component])
