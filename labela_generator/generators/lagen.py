import click

from labela_generator.generators.labela_generator import LabelAGenerator
from labela_generator.helpers.constants import Arguments, ConfigOptions
from labela_generator.helpers.config import Config


@click.command()
# TODO: Add -h and --help functions
@click.option(Arguments.CONFIGFILE.value)
@click.option(Arguments.PROMPTYES.value, is_flag=True)
@click.argument(Arguments.COMPONENT.value)
@click.argument(Arguments.NAME.value)
def lagen(component: str, name: str, y: bool, c: str = None) -> None:
    if not c:
        c = ConfigOptions.FILENAME.value
    config = Config(ini_file=c, resource_name=name)
    generator = LabelAGenerator(config)

    generator.generate(component, y)
