'''
Created on 19-May-2021

@author: kbarvind
'''
import click

@cli.command()
@click.option("--file", "-f", help="configstepfile")
def cli(file):
    if file is None:
        raise Exception("Configuration stpes not provided")
    print("File path is "+file)


if __name__ == '__main__':
    cli()