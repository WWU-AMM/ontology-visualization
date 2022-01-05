from tempfile import NamedTemporaryFile
import pytest

from ontoviz.graph import OntologyGraph
from ontoviz.utils import Config


def runmodule(filename):
    import pytest
    import sys

    sys.exit(pytest.main(sys.argv[1:] + [filename]))


@pytest.mark.xfail(msg="Still failing, see https://github.com/WWU-AMM/ontoviz/pull/4")
def test_output(file_regression, shared_datadir):
    config = Config(shared_datadir / 'config.json')
    ttl = shared_datadir / 'test.ttl'
    og = OntologyGraph(files=[ttl], config=config, format='ttl', ontology=None)

    with NamedTemporaryFile() as out:
        og.write_file(out.name)
        out.seek(0)
        file_regression.check(out.read().decode(), extension='.dot')


if __name__ == "__main__":
    runmodule(filename=__file__)
