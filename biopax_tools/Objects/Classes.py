#!usr/bin/env python3.6

import os
import sys

class BioPax(object) :
    def __init__(self,fileName = ""):
        self.fileName = fileName
        self.PathwayCollection = {}
        self.PathwayStepCollection = {}
        self.ProteinCollection = {}
        self.UnificationXrefCollection = {}
        self.ComplexCollection = {}
        self.SmallMoleculeCollection = {}
        self.BiochemicalReactionCollection = {}
        self.ControlCollection = {}
        self.CatalysisCollection = {}
        self.StoichiometryCollection = {}        
        self.FragmentFeatureCollection = {}
        self.SequenceIntervalCollection = {}
        self.SequenceSiteCollection = {}
        
    def addPathway(self,pathway) :
        if not pathway.rdfID in self.PathwayCollection :
            self.PathwayCollection[pathway.rdfID] = pathway
        else :
            print("gestion d'erreur pathway")
    def addPathwayStep(self,pathwayStep) :
        if not pathwayStep in self.PathwayStepCollection :
            self.PathwayStepCollection[pathwayStep.rdfID] = pathwayStep
        else :
            print("gestion d'erreur pathwaystep ")
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
    def addStoichiometry(self,stoichiometry):
        if not stoichiometry.rdfID in self.StoichiometryCollection :
            self.StoichiometryCollection[stoichiometry.rdfID] = stoichiometry
        else :
            print("gestion d'erreur stoichiometry")
    def addFragmentFeature(self,fragmentFeature) :
        if not fragmentFeature.rdfID in self.FragmentFeatureCollection :
            self.FragmentFeatureCollection[fragmentFeature.rdfID] = fragmentFeature
        else :
            print("gestion d'erreur fragmentFeature")
    def addSequenceInterval(self,sequenceInterval) :
        if not sequenceInterval in self.SequenceIntervalCollection :
            self.SequenceIntervalCollection[sequenceInterval.rdfID] = sequenceInterval
        else :
            print("gestion d'erreur sequenceInterval")
    def addSequenceSite(self,sequenceSite) :
        if not sequenceSite in self.SequenceSiteCollection :
            self.SequenceSiteCollection[sequenceSite.rdfID] = sequenceSite
        else :
            print("gestion d'erreur sequenceSite")
    
class Tag(object) :
    def __init__(self,rdfID,displayName,comment,xref,dataSource) :
        self.rdfID = rdfID
        if hasattr(displayName,'text') :
            self.displayName = displayName.text
        else :
            self.displayName = displayName
        self.xref = []
        for ref in xref :
            self.xref.append(ref.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#"))
        self.comment = []
        for com in comment :
            self.comment.append(com.text)
        self.dataSource = dataSource.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#")
    def __repr__(self):
        comment = """COMMENT : """
        for com in self.comment :
            comment = comment+com+"\n"

        xref = """XREF : \n"""
        for ref in self.xref :
            xref = xref+"\t\t"+ref+"\n"

        s = str("""
        ##########################################################
        # %s : %s
        ##########################################################

        %s
        %s
        DATASOURCE : %s\n"""%(self.rdfID,self.displayName,comment,xref,self.dataSource))
        return s
class UnificationXref(object) :
    def __init__(self,rdfID,bd,ID,comment):
        self.rdfID = rdfID
        self.bd = bd
        self.id = ID
        #idVersion
        self.comment = comment
class Entity(Tag) :
    def __init__(self,rdfID,name,cellularLocation,displayName,comment,xref,dataSource) :
        if cellularLocation != "" :
            self.cellularLocation = cellularLocation.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#") 
        else :
            self.cellularLocation = cellularLocation
        self.name = []
        if name != [] :
            for n in name :
                self.name.append(n.text)
        Tag.__init__(self,rdfID,displayName,comment,xref,dataSource)

class SmallMolecule(Entity):
    def __init__(self,rdfID,entityReference,name,cellularLocation,displayName,comment,xref,dataSource):
        self.entityReference = entityReference
        Entity.__init__(self,rdfID,name,cellularLocation,displayName,comment,xref,dataSource)
class Protein(Entity):
    def __init__(self,rdfID,cellularLocation,displayName,comment,xref,dataSource,entityReference=None,feature=[], name=[],memberPhysicalEntities = []) :
        if memberPhysicalEntities != [] :
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
        if memberPhysicalEntities != [] :
            self.memberPhysicalEntities = []
            for member in memberPhysicalEntities :
                self.memberPhysicalEntities.append(member)
        else :
            self.componentStoichiometries = []
            self.components = []
            for component in componentStoichiometries :
                self.componentStoichiometries.append(component.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#"))
            for component in components :
                self.components.append(component.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#"))
class Pathway(Entity):
    def __init__(self,rdfID,pathwayComponents,pathwaySteps,organism,name,displayName,comment,xref,dataSource) :
        cellularLocation=""
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
        self.conversionDirection = conversionDirection.text
        self.left = []
        self.right = []
        for element in left :
            self.left.append(element.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#"))
            
        for element in right :
            self.right.append(element.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#"))
        Tag.__init__(self,rdfID,displayName,comment,xref,dataSource)
        #eCNumber
class Control(Tag) :
    def __init__(self,rdfID,controller,controlled,controlType,xref,dataSource):
        self.controller = controller.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#")
        self.controlled = controlled.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource').strip("#")
        self.controlType = controlType
        displayName = ""
        comment = []
        Tag.__init__(self,rdfID,displayName,comment,xref,dataSource)
class Catalysis(Control) :
    def __init__(self,rdfID,controller,controlled,controlType,xref,dataSource) :
        Control.__init__(self,rdfID,controller,controlled,controlType,xref,dataSource)
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
        FragmentFeature.__init__(self,rdfID,localisation)
        self.modificationType = modificationType