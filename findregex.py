#!/usr/bin/env python


###############################################################################
#     																		  #
#     							findregex.py							      #
# 																			  #
# 	author: Bruna Bonguardo													  #
# 	date: Jul-08-2018														  #
# 																			  #
# 	version: 1.0															  #
# 	python version: 3.6														  #
# 																			  #
# 	design pattern: Using the TEMPLATE Design Pattern, which defines the	  #
#                    skeleton of an algorithm, deferring steps to subclasses. #
# 																			  #
# 	usage: findregex.py [-h] [-u | -c | -m] [infile [infile ...]] regex		  #
# 																		 	  #
# 	description: The script searches one or more named input files for lines  #
#                containing a match to a regular expression pattern.          #
#                If a line matches, it is print alongside the file name and   #
#                the line number for every match.                             #
# 																			  #
# 	positional arguments:													  #
#   	infile            the name of the file(s) to search.			      #
#   	regex             the regular expression.							  #
# 																			  #
# 	optional arguments:														  #
#   	-h, --help        show this help message and exit					  #
#   	-u, --underscore  prints "^" under the matching text.				  #
#   	-c, --color       highlights matching text.							  #
#   	-m, --machine     generates machine readable output.				  #
# 																			  #
###############################################################################


import argparse
import re


def print_line(filename, linenumber, linetoprint):
    print(linetoprint, end="")
    print(f" | line number: {linenumber} | file name: {filename} ")


def underscore_output(filename, linenumber, linetoprint, start, end):
    print_line(filename, linenumber, linetoprint)

    for j in range(0, start):
        print(" ", end="")
    for j in range(start, end):
        print("^", end="")
    print()


def color_output(filename, linenumber, line, string):
    newline = line.replace(string, "\033[44;33m{}\033[m".format(string))
    print_line(filename, linenumber, newline[:-1])


def machine_output(filename, linenumber, start, string):
    print(f"{filename}:{linenumber}:{start}:{string}")


def init_parser():
    parser = argparse.ArgumentParser(description="The script searches one or \
                                     more named input files for lines \
                                     containing a match to a regular \
                                     expression pattern.")
    parser.add_argument('infile', nargs='*', type=argparse.FileType('r'),
                        help='the name of the file(s) to search.')
    parser.add_argument('regex', help='the regular expression.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--underscore', action='store_true', help='prints \
                       "^" under the matching text.')
    group.add_argument('-c', '--color', action='store_true', help='highlights \
                       matching text.')
    group.add_argument('-m', '--machine', action='store_true', help='generates \
                       machine readable output.')

    return parser


args = init_parser().parse_args()
for file in args.infile:
    for i, line in enumerate(file):
        substrings = re.finditer(args.regex, line)
        if substrings:
            for substring in substrings:
                if args.underscore:
                    underscore_output(file.name, i + 1, line[:-1],
                                      substring.start(), substring.end())
                elif args.color:
                    color_output(file.name, i + 1, line[:-1],
                                 substring.group())
                elif args.machine:
                    machine_output(file.name, i + 1, substring.start(),
                                   substring.group())
                else:
                    print_line(file.name, i + 1, line[:-1])
