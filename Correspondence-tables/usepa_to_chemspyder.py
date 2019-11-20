"""Generate the .ttl from the correspondence tables.
Handcrafted as not available elsewhere."""

import pandas as pd
from pathlib import Path

data_dir = Path.cwd() / 'data' / 'final_tables' / 'tables'
# first version

def generate_usepa_to_chemspyder_correspondence(output_base_dir):
    '''handcrafted data to generate ttl from csv file'''
    print(f'files will be stored in {data_dir}')

