#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `git_log_to_timesheet` package."""


import unittest
from click.testing import CliRunner

from git_log_to_timesheet import git_log_to_timesheet
from git_log_to_timesheet import cli


class TestGit_log_to_timesheet(unittest.TestCase):
    """Tests for `git_log_to_timesheet` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'git_log_to_timesheet.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
