#! /usr/bin/env python

from phplint import PHPLint
from optparse import OptionParser

def main():
    usage = "%prog [options] path";
    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true",
                      help="This is default option. It will show result for each file",
                      default=True)
    parser.add_option("-q", "--quiet", dest="verbose", action="store_false",
                      help="Show only stderr output")

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("You must specify a path to lint")

    linter = PHPLint()
    linter.silent = not options.verbose
    linter.lint(args[0])

if __name__ == "__main__":
    main()
