from setuptools import setup, find_packages


requires = [
    "flake8",
    "wheel",
    "click"
]

setup(
    name='labela_generator',
    version='0.1',
    install_requires=requires,
    description='Labela Code Generation Tools',
    url='',
    license='MIT',
    packages=find_packages(),
    entry_points='''
    [console_scripts]
    scaffold=labela_generator.generators.scaffold:scaffold
    model=labela_generator.generators.model:model
    '''
)
