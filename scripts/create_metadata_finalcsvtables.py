"""create metadata of final csv tables used later on ttl files

the kind of stuff we need in metadata:

license
creator
description
date modified
publisher
title
preferredNamespaceUri
versionInfo

"""
import frictionless
from tableschema import Table
from pathlib import Path

# based on : https://github.com/frictionlessdata/tableschema-py

p = Path('../correspondence_tables/data/final_tables/csv').glob('*.csv')
files = [file for file in p if file.is_file()]

# for the moment just a rough characterization. Metadata fields missing
for file in files:
    assert file.is_file()
    table = Table(file)
    table.infer()
    table.schema.save(file.parent / f"{file.stem}_schema.json")
    
    # define as a resource instead (here we can add more metadata)
    # https://github.com/frictionlessdata/frictionless-py/blob/master/docs/target/describing-data/README.md
    
    frictionless.describe_resource(file)
    