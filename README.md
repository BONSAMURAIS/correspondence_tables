# Correspondence_tables
This is a work space for the correspondence tables working group for BONSAI

## Background
BONSAI will draw data from multiple sources, e.g. national supply-use tables, statistical databases etc. These have their own native classification to define products, activities, elementary flows or, generally speaking,  objects/activity flows.

The integration of these data requires correspondence tables. These establish a correspondence between the different classifications of flow-objects, activities and properties. These correspondance tables are sometimes available from data providers (e.g [UN Stats](https://unstats.un.org/unsd/trade/classifications/correspondence-tables.asp)). In other cases the correspondance tables are created by the group.

This repo contains the data and code to transform a series of correspondence table into a rdf files using ontologies compatible with bonsai. When possible, the code will generate the rdf files from the raw data as made available by the data provider.

## Installation
### manual

Call `python setup.py install` inside the repository:

```
git clone git@github.com:BONSAMURAIS/correspondence_tables.git
cd correspondence_tables
python setup.py install
```
## Usage

This functionality is not working yet, but eventually users can 
use the command line tool `correspondence_tables-cli` to regenerate
the rdf files using something like:

```
correspondence_tables-cli regenerate output
```

## Group members

 * [Michele De Rosa](https://github.com/MicDr)
 * [Miguel F. Astudillo](https://github.com/mfastudillo)
 * [Brandon Kuczenski](https://github.com/bkuczenski)
 * [Chris Mutel](https://github.com/cmutel)
 * [Stefano Merciai](https://github.com/Stefano-MRC)
 * [Arthur Jakobs](https://github.com/jakobsarthur)
 * [Tiago Morais](https://github.com/tgmorais1)
 * [Massimo Pizzol](https://github.com/massimopizzol)

## Goals and objectives  
The goal of this working group is to collect, validate and classify correspondence tables between existing classifications and to convert the correspondence tables into a RDF serialization format for entry into the BONSAI database.

## Working procedure

The correspondence tables currently available are stored as received in the folder `data\raw`. The raw data has often to be reformated into a standadised format and stored in the folder `data\intermediate` with their metadata encoded as a descriptor following the [frictionless data table schema](https://github.com/frictionlessdata/tableschema-py). From the _clean_ tables and their metadata the corresponding rdf file is created and stored in the folder `data\final`. 

# Overview of vocabulary used

In the RDF framework data is stored as statements of form subject-predicate-object. The existence of a predicate allows a more concise definition of the relation between the classifications. Here we provide an overview of the predicates used in correspondance tables.

**note:** in RDF subject object and predicate have unique identifiers (URIs), that makes the statements wordy for humans. The examples here are provided in Turtle serialization format. We use prefixes to make the sentences more readable.

prefixes:
- @prefix brdffo: <http://rdf.bonsai.uno/flowobject/us_epa_elem/> .
- @prefix owl: <http://www.w3.org/2002/07/owl#> .
- @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

**rdfs:label** it may be used to provide a human-readable version of the resource name

e.g. brdffo:Chemical-Structure.11148 rdfs:label "HFC-41" 

This means that what the chemical structure _11148_ is labelled as HFC-41, 

**OWL.SameAs** this predicate indicates that subject and object are the same thing 

e.g. : brdffo:Chemical-Structure.11148 owl:sameAs <http://www.chemspider.com/Chemical-Structure.11148> .

This links the taxonomy of US EPA elementary flows to substances in the chemspider taxonomy. This allows access to a wide wealth of [info](http://www.chemspider.com/Chemical-Structure.11148.html) available in Chemspider for the given substance.

**rdfs:subClassOf**

This means instances of one class are instances of another, e.g. HFC-41 is a subclass of HFC

Also, this predicate can be used to indicate that a class belongs to a specific classifications, such as "ISIC 4".

**bont:superClassOf**

We need to declare this predicate for the BONSAI ontology:

bont:superClassOf owl:inverseOf refs:SuperClassOf

The inverse of rdfs:subClassOf, allowing to import/export a correspondance table between two classifications as a csv-file with 3 columns (classification 1, predicate, Classification 2)
