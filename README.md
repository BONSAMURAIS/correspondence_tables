# Correspondence-tables
This is a work space for the correspondence tables working group for BONSAI hackathon 2019 [hackathon2019](https://github.com/BONSAMURAIS/hackathon-2019). The ongoig discussion of the group on this topic is [here](https://bonsai.groups.io/g/hackathon2019/topic/30417494?p=,,,20,0,0,0::relevance,,%23correspondencetables,20,2,0,30417494,ct=1&ct=1)

## Background
BONSAI will draw data from multiple sources, e.g. national supply-use tables, statistical databases etc. These have their own native classification to define products, activities, elementary flows or, generally speaking,  objects/activity flows.
The integration of these data requires correspondence tables. These establish a correspondence between the different names and classifications of flow-objects, activities and properties. 

## Group members

 * [Michele De Rosa](https://github.com/MicDr)
 * [Miguel Astudillo](https://github.com/mfastudillo)
 * [Brandon Kuczenski](https://github.com/bkuczenski)
 * [Chris Mutel](https://github.com/cmutel)
 * [Stefano Merciai](https://github.com/Stefano-MRC)
 * [Arthur Jakobs](https://github.com/jakobsarthur)
 * [Tiago Morais](https://github.com/tgmorais1)
 * [Massimo Pizzol](https://github.com/massimopizzol)

## Defining goals and objectives

The goal of this working group is to collect and classify correspondence tables between existing classifications, distinguishing between products, activities and elementary flows and to convert the correspondence tables in RDF format for entry into the database. 
<<<<<<< HEAD
All correpsondence tables shall be in machine-readable format. The correspondence tables currently available are stored as received in the folder `raw`. The final version after processed to a more usable format are available in the folder `final tables`. This folder also includes descriptors of each table created with the [frictionless data table schema](https://github.com/frictionlessdata/tableschema-py). The scripts processing the data are available on the folder `scripts`.
=======
All correspondence tables shall be in machine-readable format. The correspondence tables currently available are uploaded above.
>>>>>>> b1a464078a8111fb7cc8f349955f5822210a821d

In order to keep track of what correspondence tables are available, all developments on the correspondence tables (e.g. add new table, change status of existing file etc) shall be reported in the overview file above  [_Overview_of_available_correspondence_files](https://github.com/BONSAMURAIS/Correspondence-tables/blob/master/raw/_Overview_of_available_correspondence_files.csv)

## Hackathon Deliverables

These can be grouped into "before", "during", and "stretch" goals.

### Before the hackathon

* Collect and classify in this directory existing correspondence tables, distinguishing between activities, products and elementary flows tables (converted in csv) previously on the BONSAI goolge drive. (DONE) 
* Upload the converted tables in this directory and delete them from the goolge drive (after a month). (DONE)
* Add missing classification, if any.
* Discuss and provide recommendations on dealing with 1-N, N-1, M-N situations

### During the hackathon

Convert the correspondence tables in RDF format for entry into the database.

Create a metadata format for generated CSVs using `DataPackages` from [frictionless data](https://frictionlessdata.io/docs/using-data-packages-in-python/). See the example file `Bonsai_Datapackage_example.py` for a tutorial.

### Stretch goals

 Expand the correspondence tables converted in RDF format to allow traversing as many classifications as possible.
 
 
 

****Notes for the users:**

*Exiobase HSUTs/HIOT have 164 activities while MSUTs/MIOT have 163 activities. In the HSUTs/HIOT the activity "i40.2 - Manufacture of gas; distribution of gas" is divided into "i40.2.a - Manufacture of gas" and "i40.2.b - Distribution of gas"*
