'''
Created on 19-May-2021

@author: kbarvind
'''
import click
from app.boxconfig.Main import BoxConfig
import sys

@click.command()
@click.option("--file", "-f", help="configstepfile")
def cli(file):
    if file is None:
        raise Exception("Configuration steps not provided")
    
    try:
        boxconfig = BoxConfig(file)
        boxconfig.process()
    except Exception as ex:
        print(str(ex))
        sys.exit(1)
        


if __name__ == '__main__':
    cli()