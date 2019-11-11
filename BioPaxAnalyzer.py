#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from biopax_tools import BioPaxParser
import os

argParser = argparse.ArgumentParser()
argParser.add_argument("-biopax","--biopaxFilePath",type = str, help="input file path in BioPax format")
argParser.add_argument("-json","--jsonFile",type = str, help="output file path")

args = argParser.parse_args()

def main() :

    foutPath = os.path.join(os.getcwd(),"outputs")

    bpxParser = BioPaxParser.Parser()
    inputFilePath = args.biopaxFilePath

    if os.path.exists(inputFilePath) :
        if os.path.isfile(inputFilePath) :
            if str.endswith(inputFilePath,".xml") :
                bioPax = bpxParser.parse(inputFilePath)
        
if __name__ == "__main__":
    main()