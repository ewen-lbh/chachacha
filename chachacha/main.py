"""
Created on 25 feb 2020

@author: Alessandro Ogier <alessandro.ogier@gmail.com>
"""

import typing

import click
from click.core import Context

from chachacha import drivers
from chachacha.drivers.kac import ChangelogFormat


@click.group()
@click.option("--filename", default="CHANGELOG.md", help="changelog filename")
@click.option("--driver", default="kac", help="changelog format driver")
@click.pass_context
def main(ctx: Context, filename: str, driver: str) -> None:

    driver = drivers.kac.ChangelogFormat(filename)

    ctx.obj = driver


@main.command(help="initialize a new file")
@click.option("--overwrite", default=False, help="overwrite", is_flag=True)
@click.pass_obj
def init(driver: ChangelogFormat, overwrite: bool) -> None:

    driver.init(overwrite)


@main.command(help='add an "added" entry')
@click.pass_obj
@click.argument("changes", nargs=-1)
def added(driver: ChangelogFormat, changes: typing.Union[str, tuple]) -> None:

    driver.add_entry("added", changes)


@main.command(help='add a "changed" entry')
@click.pass_obj
@click.argument("changes", nargs=-1)
def changed(driver: ChangelogFormat, changes: typing.Union[str, tuple]) -> None:

    driver.add_entry("changed", changes)


@main.command(help='add a "deprecated" entry')
@click.pass_obj
@click.argument("changes", nargs=-1)
def deprecated(driver: ChangelogFormat, changes: typing.Union[str, tuple]) -> None:

    driver.add_entry("deprecated", changes)


@main.command(help='add a "removed" entry')
@click.pass_obj
@click.argument("changes", nargs=-1)
def removed(driver: ChangelogFormat, changes: typing.Union[str, tuple]) -> None:

    driver.add_entry("removed", changes)


@main.command(help='add a "fixed" entry')
@click.pass_obj
@click.argument("changes", nargs=-1)
def fixed(driver: ChangelogFormat, changes: typing.Union[str, tuple]) -> None:

    driver.add_entry("fixed", changes)


@main.command(help='add a "security" entry')
@click.pass_obj
@click.argument("changes", nargs=-1)
def security(driver: ChangelogFormat, changes: typing.Union[str, tuple]) -> None:

    driver.add_entry("security", changes)


@main.command(help="release a version")
@click.option("--major", "mode", flag_value="major", help="overwrite")
@click.option("--minor", "mode", flag_value="minor", help="overwrite")
@click.option("--patch", "mode", flag_value="patch", help="overwrite", default=True)
@click.pass_obj
def release(driver: ChangelogFormat, mode: str) -> None:

    driver.release(mode)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter