#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

# Auther    shun
# Filename  option_parser.py

from argparse import ArgumentParser


def option_add(args):
    print(args)
    print('add')


def option_show(args):
    print(args)
    print('show')


def option_edit(args):
    print(args)
    print('edit')


def option_delete(args):
    print(args)
    print('delete')


def option_finish(args):
    print(args)
    print('finish')


def option_help(args):
    print(args)
    print('help')


def option_parse():
    parser = ArgumentParser(description='test option parser')
    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser('add', help='try add -h')
    parser_add.add_argument('-d', '--day', action='store_true', help='limit day')
    parser_add.add_argument('-p', '--priority', action='store_true', help='priority')
    parser_add.set_defaults(handler=option_add)

    parser_show = subparsers.add_parser('show', help='try show -h')
    parser_show.set_defaults(handler=option_show)

    parser_edit = subparsers.add_parser('edit', help='try edit -h')
    parser_edit.set_defaults(handler=option_edit)

    parser_delete = subparsers.add_parser('delete', help='try delete -h')
    parser_delete.set_defaults(handler=option_delete)

    parser_finish = subparsers.add_parser('finish', help='try finish -h')
    parser_finish.set_defaults(handler=option_finish)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    option_parse()
