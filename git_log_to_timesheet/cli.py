# -*- coding: utf-8 -*-

"""Console script for git_log_to_timesheet."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for git_log_to_timesheet."""
    click.echo("Replace this message by putting your code into "
               "git_log_to_timesheet.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
