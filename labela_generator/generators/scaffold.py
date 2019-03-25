import click

from labela_generator.generators.model import model



def scaffold(config, name: str, y: bool):
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
    click.echo("Generating scaffold for {module}".format(module=name))

    model(config, name, y)
