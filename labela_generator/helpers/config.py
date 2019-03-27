import configparser
import os, sys
from typing import List, Dict, Optional

from labela_generator.helpers.constants import ConfigOptions


class Config:
    def __init__(
            self,
            ini_file: str,
            resource_name: str,
            section: str = ConfigOptions.SECTION.value
    ):
        self._config_ini = ini_file
        self._section = section
        self._resource_name = resource_name
        self._config = configparser.ConfigParser()
        self._config.read(self._config_ini)

        self.component_folder = {}

    def get_section_option(self, section: str, option: str) -> str:
        if not self._config.has_section(section):
            # TODO: Raise exception
            print('Exception: Cannot find section in config file')
        if self._config.has_option(section, option):
            return self._config.get(section, option)
        # TODO: Raise exception
        print('Exception: Cannot find option in config file')

    def project_path(self) -> str:
        return os.path.join(self.project_root(), self.project_name())

    def project_name(self) -> str:
        return self.get_main_option(ConfigOptions.ROOT.value)

    def get_main_option(self, option) -> str:
        return self.get_section_option(self._section, option)

    def find_components_path(self, components: List) -> Dict[str, str]:
        paths = {}

        root = self.project_path()
        for component in components:
            folder = Config.find_component(root, component)
            if not folder:
                # TODO: Exception?
                print('Exception: Cannot locate {component} folder!')
                sys.exit(1)
            self.set_component(component, folder)
            paths[component] = os.path.join(
                root, folder, self._resource_name + '.py'
            )
        return paths

    def get_resource_name(self):
        return self._resource_name

    def set_component(self, component: str, folder: str) -> None:
        self.component_folder[component] = folder

    def get_component(self, component: str):
        if not self.component_folder[component]:
            self.find_components_path([component])
        return self.component_folder[component]

    @staticmethod
    def find_file(root: str = None, path: str = None, resource_name: str = None
    ) -> Optional[str]:
        file_name = resource_name + '.py'
        file_location = os.path.join(root, path, file_name)
        if path.isfile(file_location):
            return file_location

        file_name = resource_name + 's.py'
        file_location = os.path.join(root, path, file_name)
        if path.isfile(file_location):
            return file_location

        file_name = resource_name[:-1] + 'ies.py'
        file_location = os.path.join(root, path, file_name)
        if path.isfile(file_location):
            return file_location

        return None

    @staticmethod
    def find_component(root: str, component: str) -> Optional[str]:
        folder = component
        path = os.path.join(root, folder)
        if os.path.isdir(path):
            return component

        folder = component + 's'
        path = os.path.join(root, folder)
        if os.path.isdir(path):
            return component

        folder = component[:-1] + 'ies'
        path = os.path.join(root, folder)
        if os.path.isdir(path):
            return component

        return None

    @staticmethod
    def project_root() -> str:
        return os.getcwd()
