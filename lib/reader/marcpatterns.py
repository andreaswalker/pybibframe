'''
Declarations used to elucidate MARC model
'''

#Just set up some flags
#BOUND_TO_WORK = object()
#BOUND_TO_INSTANCE = object()’

#Full MARC field list: http://www.loc.gov/marc/bibliographic/ecbdlist.html


MATERIALIZE = {
'100': ('creator', {'marcrType': 'Person'}),
'110': ('creator', {'marcrType': 'Organization'}),
'111': ('creator', {'marcrType': 'Meeting'}),

'130': ('uniformTitle', {'marcrType': 'Title'}),
'240a': ('uniformTitle', {'marcrType': 'Title'}),
'243a': ('uniformTitle', {'marcrType': 'Title'}),
'730': ('uniformTitle', {'marcrType': 'Title'}),
'830': ('uniformTitle', {'marcrType': 'Title'}),

'260a': ('place', {'marcrType': 'Place'}),
'260b': ('provider', {'marcrType': 'Organization'}),
'260e': ('place', {'marcrType': 'Place'}),
'260f': ('provider', {'marcrType': 'Organization'}),

'300': ('physicalDescription', {'marcrType': 'Measurement'}),

'600': ('subject', {'marcrType': 'Person'}),
'610': ('subject', {'marcrType': 'Organization'}),
'611': ('subject', {'marcrType': 'Meeting'}),

'630': ('uniformTitle', {'marcrType': 'Title'}),
'650': ('subject', {'marcrType': 'Topic'}),
'651': ('subject', {'marcrType': 'Geographic'}),
#'655': ('genre', {'marcrType': 'Genre'}),

'700': ('contributor', {'marcrType': 'Person'}),
'710': ('contributor', {'marcrType': 'Organization'}),
'711': ('contributor', {'marcrType': 'Meeting'}),
}


MATERIALIZE_VIA_ANNOTATION = {
#'852': ('institution', {'marcrType': 'Organization'}, {'marcrType': 'Holdings'}),
'852': ('institution', 'Holdings', {'holderType': 'Organization'},),
}


FIELD_RENAMINGS = {
'010a': 'lccn',
#Don't do a simple field renaming of ISBN because
#'020a': 'isbn',
'022a': 'issn',
'034a': 'cartographicMathematicalDataScaleStatement', #Rebecca & Sally suggested this should effectively be a merge with 034a
'034b': 'cartographicMathematicalDataProjectionStatement',
'034c': 'cartographicMathematicalDataCoordinateStatement',
'050a': 'lcCallNumber',
'0503': 'material',
'082a': 'deweyNumber',

'100a': 'label',
'100b': 'numeration',
'100c': 'titles',
'100d': 'date',  #Note: there has been discussion about removing this, but we're no sure we get reliable ID.LOC lookups without it.  If it is removed, update augment.py 
'110a': 'label',
'110d': 'date',
'111a': 'label',
'111d': 'date',

'130a': 'label',
'240a': 'label',
'730a': 'label',
'830a': 'label',

'130l': 'language',
'041a': 'language',

'210a': 'abbreviatedTitle',
'222a': 'keyTitle',
'240d': 'legalDate',
'240h': 'Medium',
'240m': 'musicMedium',  	
'240r': 'musicKey',
'245a': 'title',
'245b': 'subtitle',
'245c': 'titleStatement',
'245f': 'titleInclusiveDates',
'245h': 'titleMedium',
'245k': 'designatedForm',
'245n': 'titleNumberParts',
'245p': 'titleNameParts',
'247a': 'formerTitle',
'250a': 'edition',
'250b': 'edition',
'254a': 'musicalPresentation',
'255a': 'cartographicMathematicalDataScaleStatement',
'255b': 'cartographicMathematicalDataProjectionStatement',
'255c': 'cartographicMathematicalDataCoordinateStatement',
'256a': 'computerFilecharacteristics',
'260a': 'label',
'260b': 'label',
'260c': 'date',
'260e': 'place',
'260f': 'label',
'260g': 'date',

'300a': 'extent',
'300b': 'physicalDesc',
'300c': 'dimensions',
'300e': 'accompanyingMaterial',
'300f': 'typeOfunit',
'300g': 'size',
'3003': 'materials',
'310a': 'publicationFrequency',
'310b': 'publicationDateFrequency',
'336a': 'contentCategory'
'337a': 'mediaCategory',
'338a': 'carrierCategory
'340a': 'physicalSubstance',
'340b': 'dimensions',
'340c': 'materialsApplied',
'340d': 'recordingTechnique',
'340e': 'physicalSupport',
'351a': 'orgazationMethod',
'351b': 'arrangement',
'351c': 'hierarchy',
'3513': 'materialsSpec',


'490a': 'seriesStatement',
'490v': 'seriesVolume',



'500a': 'note',
'501a': 'note',
'502a': 'dissertationNote',
'502b': 'degree',
'502c': 'grantingInstitution',
'502g': 'dissertationNote', 
'502o': 'dissertationID',
'504a': 'bibliographyNote',
'505a': 'contentsNote',
'506a': 'governingAccessNote',
'506b': 'jurisdictionNote',
'506c': 'physicalAccess',
'506d': 'authorizedUsers',
'506e': 'authorization',
'506u': 'uriNote',
'507a': 'representativeFractionOfScale',
'507b': 'remainderOfScale',
'508a': 'productionCredit',
'510a': 'citationSource', 
'510b': 'citationCoverage',
'510c': 'citationLocationWithinSource',
'510u': 'citationUri',
'511a': 'participantOrPerformer',
'513a': 'typeOfReport',
'513b': 'periodCoveredn',
'514a': 'dataQuality',
'515a': 'numberingPerculiarities', 
'516a': 'typeOfComputerFile',
'518a': 'dateTimePlace',
'518d': 'dateOfEvent',
'518o': 'otherEventInformation', 
'518p': 'placeOfEvent',
'520a': 'summary',
'520b': 'summaryExpansion',
'520c': 'assigningSource',
'520u': 'summaryURI',
'521a': 'targetAudience',
'521b': 'targetAudienceSource', 
'522a': 'geograhpicCoverage',
'525a': 'supplement',
'538a': 'systemDetails',
'526a': 'studyProgramName',
'526b': 'interestLevel',
'526c': 'readingLevel',
'561a': 'ownership', 
'583a': 'action',
'600a': 'label',
'600d': 'date',
'610a': 'label',
'610d': 'date',  #Note: there has been discussion about removing this, but we are not sure we get reliable ID.LOC lookups without it.  If it is removed, update augment.py 
'650a': 'label',
'650d': 'date',
'651a': 'label',
'651d': 'date',
'630a': 'uniformTitle',
'630l': 'language',

'630a': 'label',
'630h': 'medium',
'630v': 'formSubdivision',
'630x': 'generalSubdivision',
'630y': 'chronologicalSubdivision',
'630z': 'geographicSubdivision',

'650a': 'label',
'650c': 'locationOfEvent',
'650v': 'formSubdivision',
'650x': 'generalSubdivision',
'650y': 'chronologicalSubdivision',
'650z': 'geographicSubdivision',

'651a': 'label',
'651v': 'formSubdivision',
'651x': 'generalSubdivision',
'651y': 'chronologicalSubdivision',
'651z': 'geographicSubdivision',

'700a': 'label',
'700b': 'numeration',
'700c': 'titles',
'700d': 'date',  #Note: there has been discussion about removing this, but we are not sure we get reliable ID.LOC lookups without it.  If it is removed, update augment.py 
'710a': 'label',
'710d': 'date',
'711a': 'label',
'711d': 'date',

#'852a': 'institution',
'852a': 'label',
'852h': 'callNumber', #Need to verify this one, since it seems to contradict the rest of the 852 pattern
'852n': 'code',
'852u': 'link',
'852e': 'streetAddress',

'856u': 'link',
}


WORK_FIELDS = set([
'010',
'028',
'035',
'040',
'041',
'050a', #Note: should be able to link directly to authority @ id.loc.gov authority/classification/####
'082',
'100',
'110',
'111',
'111',
'130',
'210',
'222',
'240',
'243',
'245',
'245',
'246',
'247',
'310',
'310',
'321',
'321',
'362',
'490',
'500',
'502',
'504',
'508',
'510',
'511',
'513',
'514',
'518',
'520',
'521',
'522',
'583',
'600',
'610',
'611',
'630',
'650',
'651',
'700',
'710',
'711',
'730',
])


INSTANCE_FIELDS = set([
'020',
'022',
'055',
'060',
'070',
'086',
'210',
'222',
'250',
'254',
'255',
'256',
'257',
'260',
'263',
'300',
'310',
'340',
'351',
'306',
'340',
'336',
'337',
'338',
'351',
'506',
'507',
'515',
'516',
'525',
'538',
'561',
'850',
'852',
'856',
])


ANNOTATIONS_FIELDS = set([
'852h',
])

#HOLDINGS_FIELDS = set([
#'852',
#])

