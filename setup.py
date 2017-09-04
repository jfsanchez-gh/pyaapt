import os
from setuptools import setup, find_packages

version = '0.1.1'
README = os.path.join(os.path.dirname(__file__), 'README.txt')
long_description = open(README).read() + '\n\n'
setup(
	name='pyaapt',
	version=version,
	description=("Python wrapper for Android aapt command line tool."),
	long_description=long_description,
	keywords='android aapt wrapper',
	author='Jorge Fernández Sánchez',
	author_email='jfsanchez.email@gmail.com',
	license='GPLv2',
	packages=['pyaapt'],
	namespace_packages=['pyaapt'],
)