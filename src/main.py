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

def main(args):
    pass    


if __name__ == '__main__':
    parser = init_parser()
    args = parser.parser_args()
    main(args)