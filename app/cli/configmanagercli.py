'''
Created on 19-May-2021

@author: kbarvind
'''
import click
from app.boxconfig.Main import BoxConfig
import sys
from app.boxconfig.boot.install import BoxConfigInstallation



@click.group()
def boxconfigcli():
    pass

@boxconfigcli.command()
@click.option("--file", "-f", help="configstepfile")
def apply(file):
    if file is None:
        raise Exception("Configuration steps not provided")
    
    try:
        boxconfig = BoxConfig(file)
        boxconfig.process()
    except Exception as ex:
        print(str(ex))
        sys.exit(1)
        

@boxconfigcli.command()
@click.option("--hostname", "-h", prompt="Hostname to install boxconfig", required=True)
@click.option("--username", "-u", prompt="SSH User name", required=True)
@click.password_option()
def install(hostname, username, password):
    
    try:
        boxconfiguration = BoxConfigInstallation(hostname, username, password)
        boxconfiguration.install()
    except Exception as ex:
        print(ex)


@boxconfigcli.command()
@click.option("--hostname", "-h", prompt="Hostname to install boxconfig", required=True)
@click.option("--username", "-u", prompt="SSH User name", required=True)
@click.password_option()
def uninstall(hostname, username, password):
    
    try:
        boxconfiguration = BoxConfigInstallation(hostname, username, password)
        boxconfiguration.uninstall()
    except Exception as ex:
        print(ex)


def climain():
    boxconfigcli()


if __name__ == '__main__':
    climain()