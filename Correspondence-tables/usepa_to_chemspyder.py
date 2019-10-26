"""Generate the .ttl from the correspondance tables.
Handcrafted as not available elsewhere."""

from .graph_common import generate_generic_graph
import pandas as pd
from pathlib import Path

data_dir = Path.cwd() / 'data' / 'final_tables' / 'tables'
# first version

def generate_usepa_to_chemspyder_correspondance(output_base_dir):
    '''handcrafted data to generate ttl from csv file'''

    data = pd.read_csv(data_dir / 'usepa_to_chemspyder_uris.csv')
    output_base_dir = Path(output_base_dir)

    epa_ns = Namespace(uri)

    g = add_common_elements(
        Graph(),
        base_uri=uri, # I don't think we need this
        title="US EPA Elementary Flow List",
        description="to be read from the metadata",
        author="Miguel F. Astudillo",
        version="0.1 (2019-10-26)",
    )
    g.bind('brdffo', uri)

    for label, code in data.values:
        node = URIRef(epa_ns[code])
        g.add((node, RDF.type, NS.nb.FlowObject))
        g.add((node, OWL.sameAs, URIRef("http://www.chemspider.com/{}".format(code))))
        g.add((node, RDFS.label, Literal(label)))

    write_graph(
        output_base_dir / "flowobject" / "us_epa_elem",
        g
    )

