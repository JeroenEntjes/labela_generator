import os

import click

from labela_generator.helpers.project_structure import find_paths


@click.command()
@click.option('-y', is_flag=True)
@click.argument('name')
def model(name: str, y: bool):
    """
    Generate model
    """
    model_(name, y)


def model_(name: str, y: bool = False):
    models_path, repositories_path, services_path = find_paths(name)
    if os.path.isfile(models_path):
        #TODO: Exception raising
        print('file already exists')
        return

    if y or click.confirm(
        "About to generate file {full_path}. Continue?".format(
            full_path=models_path
        )
    ):
        new_model = open(models_path, 'w')
