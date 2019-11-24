#!usr/bin/env python3.6

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
from biopax_tools.Objects.Classes import SequenceInterval
from biopax_tools.Objects.Classes import SequenceSite
def ToString(element) :
    if type(element) == BioPax :
        return _bioPaxToString(element)
    if type(element) == Pathway :
        return _pathwayToString(element)
    if type(element) == PathwayStep :
        return _pathwayStepToString(element)
    if type(element) == Protein :
        return _proteinToString(element)
    if type(element) == Catalysis :
        return _catalysisToString(element)
    if type(element) == Complex :
        return _complexToString(element)
    if type(element) == Control :
        return _controlToString(element)
    if type(element) == SmallMolecule :
        return _smallMoleculeToString(element)
    if type(element) == BiochemicalReaction :
        return _biochemicalReactionToString(element)
    if type(element) == Stoichiometry :
        return _stoichiometryToString(element)
    if type(element) == FragmentFeature :
        return _fragmentFeatureToString(element)
    if type(element) == SequenceInterval :
        return _sequenceIntervalToString(element)
    if type(element) == SequenceSite :
        return _sequenceSiteToString(element)
def _bioPaxToString(bioPax):
    s = """
    ################
    # %s
    ################

    len(bioPax.PathwayCollection) = %d
    len(bioPax.PathwayStepCollection) = %d
    len(bioPax.ProteinCollection) = %d
    len(bioPax.UnificationXrefCollection) = %d
    len(bioPax.ComplexCollection) = %d
    len(bioPax.SmallMoleculeCollection) = %d
    len(bioPax.BiochemicalReactionCollection) = %d
    len(bioPax.ControlCollection) = %d
    len(bioPax.CatalysisCollection) = %d
    len(bioPax.StoichiometryCollection) = %d
    len(bioPax.FragmentFeatureCollection) = %d
    len(bioPax.SequenceIntervalCollection) = %d 
    len(bioPax.SequenceSiteCollection) = %d
    """%(bioPax.fileName,
    len(bioPax.PathwayCollection),
    len(bioPax.PathwayStepCollection),
    len(bioPax.ProteinCollection),
    len(bioPax.UnificationXrefCollection),
    len(bioPax.ComplexCollection),
    len(bioPax.SmallMoleculeCollection),
    len(bioPax.BiochemicalReactionCollection),
    len(bioPax.ControlCollection),
    len(bioPax.CatalysisCollection),
    len(bioPax.StoichiometryCollection),
    len(bioPax.FragmentFeatureCollection),
    len(bioPax.SequenceIntervalCollection), 
    len(bioPax.SequenceSiteCollection))
    return s
def _pathwayToString(pathway) :
    s = """
    ##############
    # %s : %s
    ##############
    organism : %s
    components : %d
    steps : %d
    """%(pathway.rdfID,pathway.displayName,pathway.organism,len(pathway.pathwayComponents),len(pathway.pathwaySteps))
    return s
def _pathwayStepToString(pathwayStep) :
    s = """
    ##############
    # %s
    ##############
    stepProcess = %d
    nextStep = %d
    """%(pathwayStep.rdfID,len(pathwayStep.stepProcess),len(pathwayStep.nextStep))
    return s
def _proteinToString(protein):
    s = """
    ##############
    # %s : %s
    ##############
    cellularLocation = %s
    """%(protein.rdfID,protein.displayName,protein.cellularLocation)
    return s
def _catalysisToString(catalysis):
    s = """
    ##############
    # %s  
    ##############
    controller = %s
    controlled = %s
    controlType = %s
    """%(catalysis.rdfID,catalysis.controller,catalysis.controlled,catalysis.controlType)
    return s
def _complexToString(cplx):
    s = """
    ##############
    # %s : %s 
    ##############
    cellularLocation = %s"""%(cplx.rdfID,cplx.displayName,cplx.cellularLocation)
    return s
def _controlToString(control):
    s = """
     ##############
    # %s  
    ##############
    controller = %s
    controlled = %s
    controlType = %s
    """%(control.rdfID,control.controller,control.controlled,control.controlType)
    return s
def _smallMoleculeToString(smallMolecule):
    s = """
    ##############
    # %s : %s 
    ##############
    cellularLocation = %s
    """%(smallMolecule.rdfID,smallMolecule.displayName,smallMolecule.cellularLocation)
    return s
def _biochemicalReactionToString(biochemicalReaction):
    s = """
    ##############
    # %s : %s 
    ##############
    """%(biochemicalReaction.rdfID,biochemicalReaction.displayName)
    return s
def _stoichiometryToString(stoichiometry) :
    s = """
    ##############
    # %s 
    ##############
    coefficient = %s
    entity = %s
    """%(stoichiometry.rdfID,stoichiometry.stoichiometricCoefficient,stoichiometry.physicalEntity)
    return s
def _fragmentFeatureToString(feature) :
    s = """
    ##############
    # %s
    ##############
    location = %s
    """%(feature.rdfID,feature.featureLocation)
    return s
def _sequenceIntervalToString(sequenceInterval) :
    s = """
    ##############
    # %s 
    ##############
    begin = %s
    end = %s
    """%(sequenceInterval.rdfID,sequenceInterval.sequenceIntervalBegin,sequenceInterval.sequenceIntervalEnd)
    return s
def _sequenceSiteToString(sequenceSite) :
    s = """
    ##############
    # %s
    ##############
    sequencePosition = %s
    positionStatus = %s
    """%(sequenceSite.rdfID,sequenceSite.sequencePosition,sequenceSite.positionStatus)
    return s