__all__ = (
    "generate_usepa_to_chemspyder_correspondence",
)
__version__ = (0, 1)

from pathlib import Path
data_dir = Path(__file__).parent / "data"

from .usepa_to_chemspyder import generate_usepa_to_chemspyder_correspondence


def generate_all(base_dir):
    # generate_usepa_to_chemspyder_correspondence(base_dir)
    print('hello bonsai')
