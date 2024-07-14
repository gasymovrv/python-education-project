from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=[
        'requests~=2.32.3',
        'numpy~=2.0.0',
        'matplotlib~=3.9.1',
        'setuptools~=70.3.0'
    ]
)
