from os import stat


import click
import yaml
from pathlib import Path
from datetime import date
import logging

log = logging.getLogger(__name__)


def update_citation_cff(release):
    # TODO: update author list according to PIG 24
    citation_path = Path(__file__).parent / "CITATION.cff"

    with citation_path.open("r") as f:
        data = yaml.safe_load(f)
    
    data["date-released"] = date.today()
    data["version"] = release

    with citation_path.open("w") as f:
        log.info(f"Writing {f}")
        yaml.safe_dump(data, f)


@click.option("--release", help="Release tag")
def cli(release):
    update_citation_cff(release=release)
    

if __name__ == "__main__":
    cli()
    print("Please review and commit the chnages now.")





