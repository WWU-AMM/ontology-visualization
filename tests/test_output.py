from tempfile import NamedTemporaryFile
import random

from ontoviz.graph import OntologyGraph
from ontoviz.utils import Config


def runmodule(filename):
    import pytest
    import sys

    sys.exit(pytest.main(sys.argv[1:] + [filename]))


def test_output(file_regression, shared_datadir):
    rng = random.Random()
    rng.seed(123)
    config = Config(shared_datadir / 'config.json')
    ttl = shared_datadir / 'test.ttl'
    og = OntologyGraph(files=[ttl], config=config, format='ttl', ontology=None, rng=rng)

    with NamedTemporaryFile() as out:
        og.write_file(out.name)
        out.seek(0)
        file_regression.check(out.read().decode(), extension='.dot')


if __name__ == "__main__":
    runmodule(filename=__file__)
