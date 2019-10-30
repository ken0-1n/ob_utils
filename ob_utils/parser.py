#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ken0-1n
"""

import sys
import argparse
from .version import __version__
from .comp_sv import comp_main
from .merge_sv import merge_main

def create_parser():
    prog = "ob_utils"
    parser = argparse.ArgumentParser(prog = prog)
    parser.add_argument("--version", action = "version", version = prog + "-" + __version__)
    subparsers = parser.add_subparsers()
    
    def _create_comp_parser(subparsers):
        
        comp_parser = subparsers.add_parser("comp", help = "onebreak results and GenomonSV results")
        comp_parser.add_argument("--in_onebreak", help = "the result of onebreak", type = str, required=True)
        comp_parser.add_argument("--in_genomonsv", help = "the result of GenomonSV", type = str, required=True)
        comp_parser.add_argument("--output", help = "the output file", type = str, required=True)
        comp_parser.add_argument("--margin", help = "the margin for comparing SVs and SVs", type = int, default = 10)
        
        return comp_parser
        
    def _create_merge_parser(subparsers):
        
        merge_parser = subparsers.add_parser("merge", help = "merge onebreak filt results")
        merge_parser.add_argument("--in_onebreak_filt1", help = "the result of onebreak filt 1", type = str, required=True)
        merge_parser.add_argument("--in_onebreak_filt2", help = "the result of onebreak filt 2", type = str, required=True)
        merge_parser.add_argument("--output", help = "the output file", type = str, required=True)

        return merge_parser

    comp_parser = _create_comp_parser(subparsers)
    comp_parser.set_defaults(func = comp_main)
    merge_parser = _create_merge_parser(subparsers)
    merge_parser.set_defaults(func = merge_main)
    return parser
