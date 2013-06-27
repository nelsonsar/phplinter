#! /usr/bin/env python

from phplint import PHPLint
import sys

def main():
    linter = PHPLint()
    linter.lint(sys.argv[1])

main()
