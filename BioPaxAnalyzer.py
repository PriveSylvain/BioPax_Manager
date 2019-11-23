#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from biopax_tools import BioPaxParser
import os
import sys

argParser = argparse.ArgumentParser()
argParser.add_argument("-bioPax","--bioPaxFilePath",type = str, help="input file path in BioPax format")
argParser.add_argument("-json","--jsonFile",type = str, help="output file path")

args = argParser.parse_args()

def analyseBiochemicalReactionCollection(bioPax):
    for biochID in bioPax.BiochemicalReactionCollection :
        biochemicalReaction = bioPax.BiochemicalReactionCollection[biochID]
        left,right = analyseBiochemicalReaction(bioPax,biochemicalReaction)


def analyseBiochemicalReaction(bioPax,biochemicalReaction) :
    leftComponents = []
    rightComponents = []
    decompose(bioPax,biochemicalReaction.left,leftComponents)
    decompose(bioPax,biochemicalReaction.right,rightComponents)
    return leftComponents,rightComponents
def decompose(bioPax,listComponent,components) :
    for component in listComponent :
        if "Protein" in component :
            if component not in components :
                components.append(component)
        elif "Complex" in component :
            decomposeComplex(bioPax,bioPax.ComplexCollection[component],components)
        elif "SmallMolecule" in component :
            if component not in components :
                components.append(component)
        else :
            pass
def decomposeComplex(bioPax,cplx,components) :
    if hasattr(cplx,"components") : 
        decompose(bioPax,cplx.components,components)
    elif hasattr(cplx,"memberPhysicalEntities") :
        #raise an error
        pass

def main() :

    foutPath = os.path.join(os.getcwd(),"outputs")

    bpxParser = BioPaxParser.Parser()
    inputFilePath = args.bioPaxFilePath

    if os.path.exists(inputFilePath) :
        if os.path.isfile(inputFilePath) :
            if str.endswith(inputFilePath,".xml") :
                bioPax = bpxParser.parse(inputFilePath)
    analyseBiochemicalReactionCollection(bioPax)
    
if __name__ == "__main__":
    main()