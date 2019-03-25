import click

from labela_generator.generators.model import model
from labela_generator.generators.scaffold import scaffold
from labela_generator.helpers.project_structure import Config


@click.command()
@click.option('-c')
@click.option('-y', is_flag=True)
@click.argument('component')
@click.argument('name')
def lagen(component: str, name: str, y: bool, c: str):

    config = Config(ini_file=c)

    #TODO: No magic strings
    if component == 'scaffold':
        return scaffold(config, name, y)
    elif component == 'models':
        return model(config, name, y)

    #TODO: Exception
    print('Exception: Unknown operation')
