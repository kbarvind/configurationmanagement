from setuptools import setup
import setuptools

setup(
      name='irobo_cli',
      version='1.0',
      description='iRobo is command line executors',
      author='kb.arvind@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      zip_safe=False,
      entry_points = {
        'console_scripts': ['pogu=irobo_cli.pogucli:bootstrapcli'],
        }
      )