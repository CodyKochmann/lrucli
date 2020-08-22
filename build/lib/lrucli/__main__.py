#!/usr/bin/env python3
# by: Cody Kochmann

import sys
from argparse import ArgumentParser
from functools import lru_cache

__doc__ = '''
This program provides lru cache functionality for
lines running through stdin. This is helpful when
you want to see a deduped view of some long input
stream but don't want to wait for `sort | uniq`.
'''

DEFAULT_CACHE_SIZE = 0


def main():

    parser = ArgumentParser(description=__doc__)

    parser.add_argument(
        '--maxsize',
        type=int,
        default=DEFAULT_CACHE_SIZE,
        metavar=DEFAULT_CACHE_SIZE,
        help='how many items to cache (0 is unlimited)'
    )

    try:
        maxsize = parser.parse_args().maxsize
    except:
        maxsize = DEFAULT_CACHE_SIZE

    if maxsize <= 0:
        maxsize = None

    try:
        set(
            map(
                lru_cache(maxsize=maxsize)(sys.stdout.write),
                sys.stdin
            )
        )
    except Exception as e:
        parser.print_help()
        #raise e


if __name__ == '__main__':
    main()
