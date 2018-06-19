from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='dataent_io',
    version=version,
    description='dataent.io',
    author='Dataent',
    author_email='info@dataent.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("dataent",),
)
