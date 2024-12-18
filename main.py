#!/usr/bin/env python3
import click

from src.engine import summarizer, entity_extractor


@click.group
def cli():
    """This is to expose the fuctions as cli"""


@cli.command("summarize")
@click.argument("text")
def summurize(text):
    """usage: ./main.py summarize 'Text'"""
    summarizer(text=text)


@cli.command("ner")
@click.argument("text")
def ner(text):
    """usage: ./main.py ner 'Text'"""
    entity_extractor(text=text)


if __name__ == "__main__":
    cli()
