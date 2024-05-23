# setup.py
from setuptools import setup, find_packages

setup(
    name='PsycheSystem',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'requests'
    ],
    description='PsycheSystem: A library for window management, system security, password management, and file installation.',
    author='kai_studio',
    author_email='diekunnazar@gmail.com',
    url='https://github.com/kaiproduction/PsycheSystem',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
