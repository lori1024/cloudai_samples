from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = []

setup(
    name='criteo-trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Trains Criteo with XGBoost.'
)
