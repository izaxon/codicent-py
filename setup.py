from setuptools import setup

setup(
    name='codicent-py',
    version='1.0',
    package_dir={'': 'src'},
    packages=[''],  # Empty string to include the root package
    py_modules=['codicentpy'],  # Specify the codicentpy module
    install_requires=['requests'],
)
