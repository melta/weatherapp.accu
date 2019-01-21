from setuptools import setup, find_namespace_packages

setup(
    name='weatherapp.accu',
    version='0.1.0',
    author='Taras Melnychuk',
    description="AccuWeather provider",
    long_descriptoin="",
    packages=find_namespace_packages(),
    entry_points={
        'weatherapp.provider': 'accu=weatherapp.accu.provider:AccuProvider',
    },
    install_requires=[
        'bs4'
    ]
)
