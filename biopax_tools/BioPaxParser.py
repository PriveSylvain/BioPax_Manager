#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import os
import xml.etree.ElementTree as ET
from biopax_tools.Objects.Classes import BioPax
from biopax_tools.Objects.Classes import Pathway
from biopax_tools.Objects.Classes import Protein
from biopax_tools.Objects.Classes import Catalysis
from biopax_tools.Objects.Classes import Complex
from biopax_tools.Objects.Classes import Control
from biopax_tools.Objects.Classes import SmallMolecule
from biopax_tools.Objects.Classes import BiochemicalReaction


class Parser(object) :
    def parse(self,xmlFilePath) :
        
        bioPax = BioPax()

        tree = ET.parse(xmlFilePath)
        root = tree.getroot()

        ns = {
            "rdf" : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "owl" : "http://www.w3.org/2002/07/owl#",
            "bp" : "http://www.biopax.org/release/biopax-level3.owl#",
            "rdfs" : "http://www.w3.org/2000/01/rdf-schema#",
            "xsd" : "http://www.w3.org/2001/XMLSchema#",
            "base" : "http://www.reactome.org/biopax/70/177929#",
        }
        self.process(bioPax,root,ns)
        return bioPax
        
    def process(self,bioPax,root,ns) :
        self.addPathways(bioPax,root,ns)
        self.addBiochemicalReactions(bioPax,root,ns)        
        self.addProteins(bioPax,root,ns)
        self.addSmallMolecules(bioPax,root,ns)
        self.addComplexes(bioPax,root,ns)
        self.addCatalysis(bioPax,root,ns)
        self.addControl(bioPax,root,ns)
    def addPathways(self,bioPax,root,ns) :
        pathways = root.findall('bp:Pathway',ns)

        for pw in pathways :

            rdfID = pw.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            pathwayComponents = pw.findall('bp:pathwayComponent')
            organism = pw.find('bp:organism')
            name = pw.find('bp:name')
            displayName = pw.find('bp:displayName')
            comment = pw.findall('bp:comment')
            xref = pw.findall('bp:xref')
            dataSource = pw.find('bp:dataSource')
            pathwaySteps = pw.findall('bp:pathwaySteps')
            
            newPathway = Pathway(rdfID, pathwayComponents, pathwaySteps, organism, name, displayName, comment, xref,dataSource)
            bioPax.addPathway(newPathway)
    def addBiochemicalReactions(self,bioPax,root,ns) :
        BiochemicalReactions = root.findall('bp:BiochemicalReaction',ns)

        for bioch in BiochemicalReactions :
            rdfID = bioch.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            conversionDirection = bioch.find("bp:datatype")
            left = bioch.find("bp:left")
            right = bioch.find("bp:right")
            displayName = bioch.find("bp:displayName")
            comment = bioch.findall("bp:comment")
            xref = bioch.findall("bp:xref")
            dataSource = bioch.find("bp:dataSource")

            newBiochemicalReaction = BiochemicalReaction(rdfID,conversionDirection,left,right,displayName,comment,xref,dataSource)
            bioPax.addBiochemicalReaction(newBiochemicalReaction)
    def addProteins(self,bioPax,root,ns) :
        proteins = root.findall('bp:Protein',ns)

        for protein in proteins :
            rdfID = protein.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            cellularLocation = protein.find('bp:cellularLocation')
            displayName = protein.find("bp:displayName")
            comment = protein.findall("bp:comment")
            xref = protein.findall("bp:xref")
            dataSource = protein.find("bp:dataSource")
            entityReference = protein.find("bp:entityReference")
            feature = protein.findall("bp:feature")
            name = protein.findall("bp:name")
            memberPhysicalEntities = protein.findall("bp:memberPhysicalEntities")

            newProtein = Protein(rdfID,cellularLocation,displayName,comment,xref,dataSource,entityReference,feature,name,memberPhysicalEntities)
            bioPax.addProtein(newProtein)
    def addSmallMolecules(self,biopax,root,ns) :
        smallMolecules = root.findall('bp:SmallMolecule',ns)

        for smallMolecule in smallMolecules :
            rdfID = smallMolecule.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            entityReference = smallMolecule.find("bp:entityReference")
            name = smallMolecule.findall("bp:name")
            cellularLocation = smallMolecule.find("bp:cellularLocation")
            displayName = smallMolecule.find("bp:displayName")
            comment = smallMolecule.findall("bp:comment")
            xref = smallMolecule.findall("bp:xref")
            dataSource = smallMolecule.find("bp:dataSource")

            newSmallMolecule = SmallMolecule(rdfID,entityReference,name,cellularLocation,displayName,comment,xref,dataSource)
            biopax.addSmallMolecule(newSmallMolecule)
    def addComplexes(self,bioPax,root,ns):
        complexes = root.findall('bp:Complex',ns)
        for cplx in complexes :
            rdfID = cplx.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            name = cplx.findall("bp:name",ns)
            cellularLocation = cplx.find("bp:cellularLocation",ns)
            displayName = cplx.find("bp:displayName",ns)
            comment = cplx.findall("bp:comment",ns)
            xref = cplx.findall("bp:xref",ns)
            dataSource = cplx.find("bp:dataSource",ns)
            memberPhysicalEntities = cplx.findall("bp:memberPhysicalEntities",ns)
            components = cplx.findall("bp:component",ns)
            componentStoichiometries = cplx.findall("bp:componentStoichiometry",ns)

            newComplex = Complex(rdfID,name,cellularLocation,displayName,comment,xref,dataSource,memberPhysicalEntities,componentStoichiometries,components)
            bioPax.addComplex(newComplex)
    def addCatalysis(self,bioPax,root,ns):
        pass
    def addControl(self,bioPax,root,ns):
        
            rdfID
            controller
            controlled
            controlType
            xref
            dataSource



