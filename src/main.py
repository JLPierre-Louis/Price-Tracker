"""
Author: Luco
Author: Ryan
Python Version: 3.7
"""

import argparse

<<<<<<< HEAD
def init_parser():
=======

def init_parser():

>>>>>>> 9146c8e2ea024e67a8f1035842979eefc8290a7f
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url",
                        dest="url",
                        help="The url to be searched")
<<<<<<< HEAD

def main(args):
    pass    


if __name__ == '__main__':
    parser = init_parser()
    args = parser.parser_args()
    main(args)
=======
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
    main()


>>>>>>> 9146c8e2ea024e67a8f1035842979eefc8290a7f
