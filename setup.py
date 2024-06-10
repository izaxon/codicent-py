from setuptools import setup

setup(
    name='codicent-py',
    version='1.0',
    package_dir={'': 'src'},
    packages=['codicentpy'],
    install_requires=['requests'],
)
