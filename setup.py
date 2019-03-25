from setuptools import setup, find_packages


requires = [
    "click==7.0",
    "mako==1.0.8"
]

setup(
    name='labela_generator',
    version='0.1',
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
