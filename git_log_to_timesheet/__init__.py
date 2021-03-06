# -*- coding: utf-8 -*-

"""Top-level package for Git log to timesheet."""

__author__ = """Bimochan Shrestha"""
__email__ = 'bmochan@gmail.com'
__version__ = '0.1.0'

from sys import argv

standupMsg = (str(argv[1]))
lines = standupMsg.split("\n")
separated_lines = []

for line in lines:
  line_without_hyphen = line.split("-")
  separated_lines.append(line_without_hyphen[1])
for counter, separated_line in enumerate(separated_lines):
  line_without_parenthesis = separated_line.split("(")
  result = str(counter+1) + ")" + line_without_parenthesis[0]
  print(result)
