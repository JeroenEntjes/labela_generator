import configparser
import os, sys
from typing import List, Dict


class Config:
    def __init__(self, ini_file: str = 'lagen.ini', section='lagen'):
        self.config_ini = ini_file
        self.section = section
        self.config = configparser.ConfigParser()
        self.config.read(self.config_ini)

    def get_section_option(self, section, name) -> str:
        """
        Return an option from the given section of the .ini file.

        """
        if not self.config.has_section(section):
            #TODO: Raise exception
            print('Exception: Cannot find section in config file')
        if self.config.has_option(section, name):
            return self.config.get(section, name)
        #TODO: Raise exception
        print('Exception: Cannot find option in config file')

    def project_path(self) -> str:
        return os.path.join(self.project_root(), self.project_name())

    def project_name(self) -> str:
        return self.get_main_option('root')

    def get_main_option(self, name) -> str:
        """
        Get a section from the ini file
        """
        return self.get_section_option(self.section, name)

    def find_paths(self, name: str, only: List = None) -> Dict[str, str]:
        paths = {}
        if not only:
            only = ['models', 'repositories', 'services']
        root = self.project_path()
        if 'models' in only:
            paths['models'] = os.path.join(
                self.find_component_path(root, 'models'), name + '.py'
            )

        if 'repositories' in only:
            paths['repositories'] = os.path.join(
                self.find_component_path(root, 'repository'), name + '.py'
            )

        if 'services' in only:
            paths['services'] = os.path.join(
                self.find_component_path(root, 'service'), name + '.py'
            )
        return paths

    def find_component_path(self, root: str, component: str) -> str:
        path = os.path.join(root, component)
        if os.path.isdir(path):
            return os.path.join(path)
        path = path + 's'
        if os.path.isdir(path):
            return os.path.join(path)
        path = path[:-1] + 'ies'
        if os.path.isdir(path):
            return os.path.join(path)
        else:
            # TODO: Exception?
            print(
                'Exception: Cannot locate {component} folder! Searched in: '
                '{path}'.format(
                    component=component, path=root
                )
            )
            sys.exit(1)

    @staticmethod
    def project_root() -> str:
        return os.getcwd()
