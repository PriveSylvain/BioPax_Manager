#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
from biopax_tools.Objects.Classes import Stoichiometry


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
        self.addControls(bioPax,root,ns)
        self.addStoichiometries(bioPax,root,ns)

    def addPathways(self,bioPax,root,ns) :
        pathways = root.findall('bp:Pathway',ns)

        for pw in pathways :

            rdfID = pw.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            pathwayComponents = pw.findall('bp:pathwayComponent',ns)
            organism = pw.find('bp:organism',ns)
            name = pw.findall('bp:name',ns)
            displayName = pw.find('bp:displayName',ns)
            comment = pw.findall('bp:comment',ns)
            xref = pw.findall('bp:xref',ns)
            dataSource = pw.find('bp:dataSource',ns)
            pathwaySteps = pw.findall('bp:pathwaySteps',ns)
            
            newPathway = Pathway(rdfID, pathwayComponents, pathwaySteps, organism, name, displayName, comment, xref,dataSource)
            bioPax.addPathway(newPathway)
    def addBiochemicalReactions(self,bioPax,root,ns) :
        BiochemicalReactions = root.findall('bp:BiochemicalReaction',ns)

        for bioch in BiochemicalReactions :
            rdfID = bioch.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            conversionDirection = bioch.find("bp:conversionDirection",ns)
            left = bioch.findall("bp:left",ns)
            right = bioch.findall("bp:right",ns)
            displayName = bioch.find("bp:displayName",ns)
            comment = bioch.findall("bp:comment",ns)
            xref = bioch.findall("bp:xref",ns)
            dataSource = bioch.find("bp:dataSource",ns)

            newBiochemicalReaction = BiochemicalReaction(rdfID,conversionDirection,left,right,displayName,comment,xref,dataSource)
            bioPax.addBiochemicalReaction(newBiochemicalReaction)
    def addProteins(self,bioPax,root,ns) :
        proteins = root.findall('bp:Protein',ns)

        for protein in proteins :
            rdfID = protein.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            cellularLocation = protein.find('bp:cellularLocation',ns)
            displayName = protein.find("bp:displayName",ns)
            comment = protein.findall("bp:comment",ns)
            xref = protein.findall("bp:xref",ns)
            dataSource = protein.find("bp:dataSource",ns)
            entityReference = protein.find("bp:entityReference",ns)
            feature = protein.findall("bp:feature",ns)
            name = protein.findall("bp:name",ns)
            memberPhysicalEntities = protein.findall("bp:memberPhysicalEntities",ns)

            newProtein = Protein(rdfID,cellularLocation,displayName,comment,xref,dataSource,entityReference,feature,name,memberPhysicalEntities)
            bioPax.addProtein(newProtein)
    def addSmallMolecules(self,biopax,root,ns) :
        smallMolecules = root.findall('bp:SmallMolecule',ns)

        for smallMolecule in smallMolecules :
            rdfID = smallMolecule.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            entityReference = smallMolecule.find("bp:entityReference",ns)
            name = smallMolecule.findall("bp:name",ns)
            cellularLocation = smallMolecule.find("bp:cellularLocation",ns)
            displayName = smallMolecule.find("bp:displayName",ns)
            comment = smallMolecule.findall("bp:comment",ns)
            xref = smallMolecule.findall("bp:xref",ns)
            dataSource = smallMolecule.find("bp:dataSource",ns)

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
        catalysis = root.findall('bp:Catalysis',ns)

        for control in catalysis :
            rdfID = control.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            controller = control.find("bp:controller",ns)
            controlled = control.find("bp:controlled",ns)
            controlType = control.find("bp:controlType",ns)
            xref = control.findall("bp:xref",ns)
            dataSource = control.find("bp:dataSource",ns)

            newCatalysis = Catalysis(rdfID, controller, controlled, controlType, xref, dataSource)
            bioPax.addCatalysis(newCatalysis)
    def addControls(self,bioPax,root,ns):
        controls = root.findall('bp:Control',ns)

        for control in controls :
            rdfID = control.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            controller = control.find("bp:controller",ns)
            controlled = control.find("bp:controlled",ns)
            controlType = control.find("bp:controlType",ns)
            xref = control.findall("bp:xref",ns)
            dataSource = control.find("bp:dataSource",ns)

            newControl = Control(rdfID, controller, controlled, controlType, xref, dataSource)
            bioPax.addControl(newControl)
    def addStoichiometries(self,biopax,root,ns) :
        stoichiometries = root.findall("bp:Stoichiometry",ns)
        for stoichiometry in stoichiometries :
            rdfID = stoichiometry.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            stoichiometricCoefficient = stoichiometry.find("bp:stoichiometricCoefficient",ns)
            physicalEntity = stoichiometry.find("bp:physicalEntity",ns)

            newStoichiometry = Stoichiometry(rdfID, stoichiometricCoefficient, physicalEntity)
            biopax.addStoichiometry(newStoichiometry)
