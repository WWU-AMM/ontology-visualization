import argparse

from ontoviz.graph import OntologyGraph
from ontoviz.utils import Config


def main():
    parser = argparse.ArgumentParser(description='Generate dot for the input ontology files')
    parser.add_argument('files', nargs='+', help='Input ontology files.')
    parser.add_argument('-f', '--format', dest='format', default='ttl', help='Input file format.')
    parser.add_argument('-o', '--output', dest='out', default='ontology.dot', help='Location of output dot file.')
    parser.add_argument('-O', '--ontology', dest='ontology', default=None, help='Provided ontology for the graph.')
    parser.add_argument('-C', '--config', dest='config', default=None, help='Provided configuration.')
    args = parser.parse_args()

    config = Config(args.config)
    og = OntologyGraph(args.files, config, args.format, ontology=args.ontology)
    og.write_file(args.out)


if __name__ == '__main__':
    main()
