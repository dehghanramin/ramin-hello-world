from setuptools import setup
import sys,os

setup(
    name = 'ramin-hello-world',
    version = '0.2.0',
    description = 'Python test app',
    license='GPL v3',
    author = 'Ramin Dehghan',
    packages = ['src'],
    package_data={'src': ['description.txt']
                 },
    install_requires=['future'],
    entry_points = {
        'console_scripts': [
            'ramin-hello-world=src.helloworld:main']
            },
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)