'''
'''

import re
import os
import logging
import itertools

#from rdflib import Graph, BNode, Namespace
from rdflib import URIRef, Literal, RDF

#from datachef.ids import simple_hashstring

from amara3 import iri

from versa import I, VERSA_BASEIRI, ORIGIN, RELATIONSHIP, TARGET

from bibframe import BFZ, BFLC

TYPE_REL = I(iri.absolutize('type', VERSA_BASEIRI))
WORKCLASS = iri.absolutize('Work', BFZ)
INSTANCECLASS = iri.absolutize('Instance', BFZ)
INSTANCEREL = iri.absolutize('hasInstance', BFZ)

def prep(stmt):
    '''
    Prepare a statement into a triple ready for rdflib
    '''
    s, p, o = stmt[:3]
    s = URIRef(s)
    #Translate v:type to rdf:type
    p = RDF.type if p == TYPE_REL else URIRef(p)
    o = URIRef(o) if isinstance(o, I) else Literal(o)
    return s, p, o


def process(source, target, to_ignore=None, logger=logging):
    '''
    Take an in-memory BIBFRAME model and convert it into an rdflib graph

    '''
    #Hoover up everything with a type
    for stmt in source.match(None, TYPE_REL, None):
        rid = stmt[ORIGIN]
        if not (to_ignore and rid in to_ignore):
            [ target.add(prep(stmt)) for stmt in source.match(rid) ]

    return
