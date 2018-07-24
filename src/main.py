"""
Author: Luco
Author: Ryan
Python Version: 3.7
"""

import argparse

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url",
                        dest="url",
                        help="The url to be searched")
    parser.add_argument("-v", "--verbose",
                        dest="verbose",
                        action='store_true',
                        default=False,
                        help="Determine if the user wants it to be verbose")
    parser.add_argument("-s", "--store",
                        dest="store_directory",
                        help="The relative path to directory where to store")
    return parser


def main():
    pass


if __name__ == '__main__':
    parser = init_parser()
    args = parser.parse_args()
    main(args)


