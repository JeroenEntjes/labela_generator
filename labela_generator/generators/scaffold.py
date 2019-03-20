import os
import click

from labela_generator.generators.model import model_


@click.command()
@click.option('-y', is_flag=True)
@click.argument('module')
def scaffold(module: str, y: bool):
    """
    Generate a full scaffold of a module.

    Scaffold is:
    Model
    Repository
    View
    Service
    Test
    Route
    Container
    """
    click.echo("Generating scaffold for {module}".format(module=module))

    path = os.getcwd()
    model_(module, path, y)
