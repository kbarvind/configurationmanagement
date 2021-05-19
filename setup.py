from setuptools import setup
import setuptools

setup(
      name='boxconfig',
      version='1.0',
      description='Box Config is configuration manager',
      author='kb.arvind@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      zip_safe=False,
      entry_points = {
        'console_scripts': ['boxconfig=app.cli.configmanagercli:cli'],
        }
      )