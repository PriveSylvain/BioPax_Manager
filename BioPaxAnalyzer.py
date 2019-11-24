#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from biopax_tools import BioPaxParser
from biopax_tools.bioPaxFormalizer import ToString
import os
import sys

argParser = argparse.ArgumentParser()
argParser.add_argument("-bioPax","--bioPaxFilePath",type = str, help="input file path in BioPax format")
argParser.add_argument("-V","--verbose", action="store_true", help="increase output verbosity")

args = argParser.parse_args()

def analyseBiochemicalReactionCollection(bioPax):
    for biochID in bioPax.BiochemicalReactionCollection :
        biochemicalReaction = bioPax.BiochemicalReactionCollection[biochID]
        analyseBiochemicalReaction(bioPax,biochemicalReaction)

def compareLeftRight(left,right) :
    l = []
    r = []
    for component in left :
        if not component in right :
            l.append(component)
    for component in right :
        if not component in left :
            r.append(component)
    return l,r

def analyseBiochemicalReaction(bioPax,biochemicalReaction) :
    leftComponents = []
    rightComponents = []
    decompose(bioPax,biochemicalReaction.left,leftComponents)
    decompose(bioPax,biochemicalReaction.right,rightComponents)
    left,right = compareLeftRight(leftComponents,rightComponents)
        
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
            #raise an error
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
    verbose = args.verbose
    if os.path.exists(inputFilePath) :
        if os.path.isfile(inputFilePath) :
            if str.endswith(inputFilePath,".xml") :
                bioPax = bpxParser.parse(inputFilePath,verbose)
    analyseBiochemicalReactionCollection(bioPax)
    if verbose:
        print(ToString(bioPax))
    
if __name__ == "__main__":
    main()