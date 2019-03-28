from setuptools import setup, find_packages


requires = [
    "click==7.0",
    "dependency-injector==3.14.4",
    "mako==1.0.8",
    "pyramid==1.10.2",
    "SQLAlchemy==1.3.0"
]

setup(
    name='labela_generator',
    version='0.2',
    install_requires=requires,
    description='Labela Code Generation Tools',
    url='',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
    [console_scripts]
    lagen=labela_generator.generators.lagen:lagen
    '''
)
