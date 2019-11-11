#!usr/bin/env python3.6
import json
import os
import sys

class BioPax(object) :
    def __init__(self):
        self.ProteinCollection = {}
        self.UnificationXrefCollection = {}
        self.SmallMoleculeCollection = {}
        self.ComplexCollection = {}
        self.PathwayCollection = {}
        self.PathwayStepCollection = {}
        self.BiochemicalReactionCollection = {}
        self.ControlCollection = {}
        self.CatalysisCollection = {}
        self.StoichiometryCollection = {}
        self.SequenceIntervalCollection = {}
        self.SequenceSiteCollection = {}
        self.FragmentFeatureCollection = {}
        self.ModificationFeatureCollection = {}

    def addPathway(self,pathway) :
        if not pathway.rdfID in self.PathwayCollection :
            self.PathwayCollection[pathway.rdfID] = pathway
        else :
            print("gestion d'erreur pathway")
    def addProtein(self,protein) :
        if not protein.rdfID in self.ProteinCollection :
            self.ProteinCollection[protein.rdfID] = protein
        else :
            print("gestion d'erreur protein")
    def addComplex(self,cplx) :
        if not cplx.rdfID in self.ComplexCollection :
            self.ComplexCollection[cplx.rdfID] = cplx
        else :
            print("gestion d'erreur complex")
    def addSmallMolecule(self,smallMolecule) :
        if not smallMolecule.rdfID in self.SmallMoleculeCollection :
            self.SmallMoleculeCollection[smallMolecule.rdfID] = smallMolecule
        else :
            print("gestion d'erreur smallMolecule")
    def addControl(self,control) :
        if not control.rdfID in self.ControlCollection :
            self.ControlCollection[control.rdfID] = control
        else :
            print("gestion d'erreur control")
    def addCatalysis(self,catalysis) :
        if not catalysis.rdfID in self.CatalysisCollection :
            self.CatalysisCollection[catalysis.rdfID] = catalysis
        else :
            print("gestion d'erreur catalysis")
    def addBiochemicalReaction(self,biochemicalReaction) :
        if not biochemicalReaction.rdfID in self.BiochemicalReactionCollection :
            self.BiochemicalReactionCollection[biochemicalReaction.rdfID] = biochemicalReaction
        else :
            print("gestion d'erreur biochemicalReaction")      
    
class Tag(object) :
    def __init__(self,rdfID,displayName,comment,xref,dataSource) :
        self.rdfID = rdfID
        self.displayName = displayName
        self.comment = comment
        self.xref = xref
        self.dataSource = dataSource
class UnificationXref(object) :
    def __init__(self,rdfID,bd,ID,comment):
        self.rdfID = rdfID
        self.bd = bd
        self.id = ID
        #idVersion
        self.comment = comment
class Entity(Tag) :
    def __init__(self,rdfID,name,cellularLocation,displayName,comment,xref,dataSource) :
        self.cellularLocation = cellularLocation        
        self.name = name
        Tag.__init__(self,rdfID,displayName,comment,xref,dataSource)
class SmallMolecule(Entity):
    def __init__(self,rdfID,entityReference,name,cellularLocation,displayName,comment,xref,dataSource):
        self.entityReference = entityReference
        Entity.__init__(self,rdfID,name,cellularLocation,displayName,comment,xref,dataSource)
class Protein(Entity):
    def __init__(self,rdfID,cellularLocation,displayName,comment,xref,dataSource,entityReference=None,feature=None, name=None,memberPhysicalEntities = None) :
        if memberPhysicalEntities != None :
            self.memberPhysicalEntities = []
            for member in memberPhysicalEntities :
                self.memberPhysicalEntities.append(member) 
        else :
            self.entityReference = entityReference
            self.feature = feature
        Entity.__init__(self,rdfID,name,cellularLocation,displayName,comment,xref,dataSource)
class Complex(Entity):
    def __init__(self,rdfID,name,cellularLocation,displayName,comment,xref,dataSource,memberPhysicalEntities,componentStoichiometries,components):
        Entity.__init__(self,rdfID,name,cellularLocation,displayName,comment,xref,dataSource)
        if memberPhysicalEntities != None :
            self.memberPhysicalEntities = []
            for member in memberPhysicalEntities :
                self.memberPhysicalEntities.append(member)
        else :
            self.componentStoichiometries = componentStoichiometries
            self.components = components
class Pathway(Entity):
    def __init__(self,rdfID,pathwayComponents,pathwaySteps,organism,name,displayName,comment,xref,dataSource) :
        cellularLocation=None
        self.organism = organism

        Entity.__init__(self,rdfID,name,cellularLocation,displayName,comment,xref,dataSource)
        self.pathwayComponents = pathwayComponents
        self.pathwaySteps = pathwaySteps
class PathwayStep(object) :
    def __init__(self,rdfID,stepProcess,nextStep) :
        self.rdfID = rdfID
        self.stepProcess = stepProcess
        self.nextStep = nextStep
class BiochemicalReaction(Tag):
     def __init__(self,rdfID,conversionDirection,left,right,displayName,comment,xref,dataSource) :
        self.conversionDirection = conversionDirection
        self.left = left
        self.right = right
        Tag.__init__(self,rdfID,displayName,comment,xref,dataSource)
        #eCNumber
class Control(Tag) :
    def __init__(self,rdfID,controller,controlled,controlType,xref,dataSource):
        self.controller = controller
        self.controlled = controlled
        self.controlType = controlType
        displayName = None
        comment = None
        Tag.__init__(self,rdfID,displayName,comment,xref,dataSource)
class Catalysis(Control) :
    def __init__(self,rdfID,controller,controlled,controlType,xref,dataSource) :
        super.__init__()


class Stoichiometry(object) :
    def __init__(self,rdfID,stoichiometricCoefficient,physicalEntity) :
        self.rdfID = rdfID
        self.stoichiometricCoefficient = stoichiometricCoefficient
        self.physicalEntity = physicalEntity

class SequenceInterval(object):
    def __init__(self,rdfID,begin,end) :
        self.rdfID = rdfID
        self.sequenceIntervalBegin = begin
        self.sequenceIntervalEnd = end
class SequenceSite(object) :
    def __init__(self,rdfID,sequencePosition,positionStatus) :
        self.rdfID = rdfID
        self.sequencePosition = sequencePosition
        self.positionStatus = positionStatus

class FragmentFeature(object):
    def __init__(self,rdfID,localisation) :
        self.rdfID = rdfID
        self.featureLocation = localisation
class ModificationFeature(FragmentFeature):
    def __init__(self,rdfID,localisation,modificationType) :
        super().__init__()
        self.modificationType = modificationType