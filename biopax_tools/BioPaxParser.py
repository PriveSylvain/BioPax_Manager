#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET
from biopax_tools.bioPaxFormalizer import ToString
from biopax_tools.Objects.Classes import BioPax
from biopax_tools.Objects.Classes import Pathway
from biopax_tools.Objects.Classes import PathwayStep
from biopax_tools.Objects.Classes import Protein
from biopax_tools.Objects.Classes import Catalysis
from biopax_tools.Objects.Classes import Complex
from biopax_tools.Objects.Classes import Control
from biopax_tools.Objects.Classes import SmallMolecule
from biopax_tools.Objects.Classes import BiochemicalReaction
from biopax_tools.Objects.Classes import Stoichiometry
from biopax_tools.Objects.Classes import FragmentFeature
# from biopax_tools.Objects.Classes import ModificationFeature
from biopax_tools.Objects.Classes import SequenceInterval
from biopax_tools.Objects.Classes import SequenceSite


class Parser(object) :
    def parse(self,xmlFilePath,verbose) :
        fileName = os.path.split(xmlFilePath)[-1]
        bioPax = BioPax(fileName = fileName)

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
        self.process(bioPax,root,ns,verbose)
        return bioPax
        
    def process(self,bioPax,root,ns,verbose=False) :
        self.addPathways(bioPax,root,ns,verbose)
        self.addPathwaySteps(bioPax,root,ns,verbose)
        self.addBiochemicalReactions(bioPax,root,ns,verbose)        
        self.addProteins(bioPax,root,ns,verbose)
        self.addSmallMolecules(bioPax,root,ns,verbose)
        self.addComplexes(bioPax,root,ns,verbose)
        self.addCatalysis(bioPax,root,ns,verbose)
        self.addControls(bioPax,root,ns,verbose)
        self.addStoichiometries(bioPax,root,ns,verbose)
        self.addFragmentFeatures(bioPax,root,ns,verbose)
        self.addSequenceIntervals(bioPax,root,ns,verbose)
        self.addModificationFeatures(bioPax,root,ns,verbose)
        self.addSequenceSites(bioPax,root,ns,verbose)
    
    def addPathways(self,bioPax,root,ns,verbose=False) :
        pathways = root.findall('bp:Pathway',ns)

        for pw in pathways :

            rdfID = pw.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            pathwayComponents = pw.findall('bp:pathwayComponent',ns)
            organism = pw.find('bp:organism',ns).get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
            
            for biosource in root.findall("bp:BioSource",ns) :
                if biosource.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID") in organism :
                    organism = root.find("bp:BioSource",ns).find("bp:name",ns).text

            name = pw.findall('bp:name',ns)
            displayName = pw.find('bp:displayName',ns).text
            comment = pw.findall('bp:comment',ns)
            xref = pw.findall('bp:xref',ns)
            dataSource = pw.find('bp:dataSource',ns)
            pathwaySteps = pw.findall('bp:pathwayOrder',ns)
            
            newPathway = Pathway(rdfID, pathwayComponents, pathwaySteps, organism, name, displayName, comment, xref,dataSource)
            bioPax.addPathway(newPathway)
            if verbose :
                print(ToString(newPathway))
            
    def addPathwaySteps(self,bioPax,root,ns,verbose=False) :
        pathwaySteps = root.findall("bp:PathwayStep",ns)
        for pathwayStep in pathwaySteps :
            rdfID = pathwayStep.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            stepProcess = pathwayStep.findall("bp:stepProcess",ns) #Pathway / BiochemicalReaction / Catalysis / Control
            nextSteps = pathwayStep.findall("bp:nextStep",ns) #PathwayStep

            newPathwayStep = PathwayStep(rdfID,stepProcess,nextSteps)
            bioPax.addPathwayStep(newPathwayStep)
            if verbose :
                print(ToString(newPathwayStep))
    def addBiochemicalReactions(self,bioPax,root,ns,verbose=False) :
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
            if verbose :
                print(ToString(newBiochemicalReaction))
    def addProteins(self,bioPax,root,ns,verbose=False) :
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
            if verbose :
                print(ToString(newProtein))
    def addSmallMolecules(self,bioPax,root,ns,verbose=False) :
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
            bioPax.addSmallMolecule(newSmallMolecule)
            if verbose :
                print(ToString(newSmallMolecule))
    def addComplexes(self,bioPax,root,ns,verbose=False) :
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
            if verbose :
                print(ToString(newComplex))
    def addCatalysis(self,bioPax,root,ns,verbose=False) :
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
            if verbose :
                print(ToString(newCatalysis))
    def addControls(self,bioPax,root,ns,verbose=False) :
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
            if verbose :
                print(ToString(newControl))
    def addStoichiometries(self,bioPax,root,ns,verbose=False) :
        stoichiometries = root.findall("bp:Stoichiometry",ns)
        for stoichiometry in stoichiometries :
            rdfID = stoichiometry.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            stoichiometricCoefficient = stoichiometry.find("bp:stoichiometricCoefficient",ns)
            physicalEntity = stoichiometry.find("bp:physicalEntity",ns)

            newStoichiometry = Stoichiometry(rdfID, stoichiometricCoefficient, physicalEntity)
            bioPax.addStoichiometry(newStoichiometry)
            if verbose :
                print(ToString(newStoichiometry))
    def addFragmentFeatures(self,bioPax,root,ns,verbose=False) :
        features = root.findall("bp:FragmentFeature",ns)
        for feature in features :
            rdfID = feature.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            featureLocation = feature.find("bp:featureLocation",ns)

            newFeature = FragmentFeature(rdfID,featureLocation)
            bioPax.addFragmentFeature(newFeature)
            if verbose :
                print(ToString(newFeature))
    def addModificationFeatures(self,bioPax,root,ns,verbose=False) :
        """ Considered as FragmentFeatures """
        modificationFeatures = root.findall("bp:ModificationFeature",ns)
        for modification in modificationFeatures :
            rdfID = modification.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            featureLocation = modification.find("bp:featureLocation",ns)
            # add if necessary :
            # modificationType = modification.find("bp:modificationType",ns)
            # newFeature = ModificationFeature(rdfID,featureLocation,modificationType)

            newFeature = FragmentFeature(rdfID,featureLocation)
            bioPax.addFragmentFeature(newFeature)
            if verbose :
                print(ToString(newFeature))
    def addSequenceIntervals(self,bioPax,root,ns,verbose=False) :
        intervals = root.findall("bp:SequenceInterval",ns)
        for sequenceInterval in intervals :
            rdfID = sequenceInterval.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            sequenceIntervalBegin = sequenceInterval.find("bp:featureLocation",ns)
            sequenceIntervalEnd = sequenceInterval.find("bp:featureLocation",ns)
            # .get("{http://www.biopax.org/release/biopax-level3.owl#}resource")

            newSequenceInterval = SequenceInterval(rdfID, sequenceIntervalBegin, sequenceIntervalEnd)
            bioPax.addSequenceInterval(newSequenceInterval)
            if verbose :
                print(ToString(newSequenceInterval))
    def addSequenceSites(self,bioPax,root,ns,verbose=False) :
        sequenceSites = root.findall("bp:SequenceSite",ns)
        
        for sequenceSite in sequenceSites :
            rdfID = sequenceSite.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID")
            sequencePosition = sequenceSite.find("bp:sequencePosition",ns)
            positionStatus = sequenceSite.find("bp:positionStatus",ns)

            newSequenceSite = SequenceSite(rdfID,sequencePosition,positionStatus)
            bioPax.addSequenceSite(newSequenceSite)
            if verbose :
                print(ToString(newSequenceSite))
    

