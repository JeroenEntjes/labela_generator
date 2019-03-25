from os import path

import click

from labela_generator.templates.generate import file_from_template
from labela_generator.templates.models import model_template_path


file_name = 'models.py.mako'


def model(config, name: str, y: bool):
    paths = config.find_paths(name, only=['models'])
    models_path = paths['models']
    if path.isfile(models_path):
        #TODO: Exception raising
        print('Exception: File already exists')
        return

    if y or click.confirm(
        "About to generate file {full_path}. Continue?".format(
            full_path=models_path
        )
    ):
        template_location = path.join(model_template_path, file_name)
        file_from_template(template_location, models_path,
                           project=config.project_name(),
                           class_name=name.capitalize())
