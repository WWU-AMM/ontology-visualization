from tempfile import NamedTemporaryFile

from ontoviz.graph import OntologyGraph
from ontoviz.utils import Config


def test_output(file_regression, shared_datadir):
    config = Config(shared_datadir / 'config.json')
    ttl = shared_datadir / 'test.ttl'
    og = OntologyGraph(files=[ttl], config=config, format='ttl', ontology=None)

    with NamedTemporaryFile() as out:
        og.write_file(out.name)
        out.seek(0)
        file_regression.check(out.read().decode(), extension='.dot')
