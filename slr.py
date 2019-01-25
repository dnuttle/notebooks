#!/usr/env/bin python

import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG)

class SimpleLinearRegression(object):
    def run(self, fname, fout):
        with open(fname) as fin:
            for line in fin:
                fout.write(line)

def main(args):
    slr = SimpleLinearRegression()
    slr.run('/Users/dnuttle/Documents/python/test.csv', sys.stdout)

if __name__ == '__main__':
    main(sys.argv[1:])
