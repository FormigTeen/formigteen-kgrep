"""This module provides the RP To-Do CLI."""
from typing import Annotated, Optional
from rich import print
from pyperclip import copy

# rptodo/cli.py
import typer
import subprocess

app = typer.Typer()

def get_resources(name: str, resource: str, namespace: str = None):
    command = ("kubectl get " + ("-n " + namespace if namespace is not None else "") + " " + (resource if resource is not None else "pods") + " | grep " + name)
    result, _ = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    result = result.decode("utf-8").replace('\\n', ' ')
    return [_.strip() for _ in str(result).split() if name in _.strip()]

@app.command()
def get(
        name: str,
        namespace: Annotated[Optional[str], typer.Option("--namespace", "-n")] = None,
        resource: Annotated[Optional[str], typer.Option("--resource", "-r")] = None

):
    for _ in get_resources(name, resource, namespace):
        print(_)

@app.command()
def cp(
        name: str,
        namespace: Annotated[Optional[str], typer.Option("--namespace", "-n")] = None,
        resource: Annotated[Optional[str], typer.Option("--resource", "-r")] = None
):
    copy(' '.join(get_resources(name, resource, namespace)))
    print('Copied!')


@app.callback()
def callback():
    pass