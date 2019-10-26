__all__ = (
#    "generate_climate_change_uris",
    # "generate_electricity_grid_uris",
    # "generate_entsoe_uris",
    # "generate_exiobase_metadata_uris",
    # "generate_exiobase_us_epa_uris",
    # "generate_foaf_uris",
    # "generate_time_uris",
    # "generate_unit_uris",
    # "generate_us_epa_uris",
    # "generate_all",
    # "get_metadata",
    "generate_usepa_to_chemspyder_correspondance",
)
__version__ = (0, 1)

from pathlib import Path
data_dir = Path(__file__).parent / "data"

# from .climate_change import generate_climate_change_uris
# from .electricity_grid import generate_electricity_grid_uris
# from .entsoe import generate_entsoe_uris
# from .exiobase_metadata import generate_exiobase_metadata_uris
# from .exiobase_us_epa import generate_exiobase_us_epa_uris
# from .extract_metadata import get_metadata
# from .foaf import generate_foaf_uris
# from .time_uris import generate_time_uris
# from .unit_uris import generate_unit_uris
# from .us_epa_elem_flow_list import generate_us_epa_uris
from .usepa_to_chemspyder import generate_usepa_to_chemspyder_correspondance

def generate_all(base_dir):
    generate_usepa_to_chemspyder_correspondance(base_dir)
    # generate_climate_change_uris(base_dir)
    # generate_electricity_grid_uris(base_dir)
    # generate_entsoe_uris(base_dir)
    # generate_exiobase_metadata_uris(base_dir)
    # # generate_exiobase_us_epa_uris(base_dir)
    # generate_foaf_uris(base_dir)
    # generate_time_uris(base_dir)
    # generate_unit_uris(base_dir)
    # generate_us_epa_uris(base_dir)
