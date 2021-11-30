# Ontoviz

[![image](https://img.shields.io/pypi/v/ontoviz.svg)](https://pypi.python.org/pypi/ontoviz)

[![image](https://github.com/WWU-AMM/ontoviz/workflows/pytest/badge.svg)](https://github.com/WWU-AMM/ontoviz/actions)

[![Documentation Status](https://readthedocs.org/projects/ontoviz/badge/?version=latest)](https://ontoviz.readthedocs.io/en/main/?badge=main)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Ontology visualization with Python


## Installation

```
python -m pip install ontoviz
```


## Example

```
    ontoviz_to_dot -o test.dot test.ttl -O ontology.ttl
    dot -Tpng -o test.png test.dot
```

-   Use `-o` to indicate the path of output file
-   Use `-O` to indicate the input ontology (Optional).
-   Use `-C` to indicate the configuration file (Optional).
    -   `max_label_length`: config the max length of labels. If the text exceeds the length, exceeded part will be replaced with "&#x2026;". Default value is `0`.
    -   `blacklist`: config the predicate that you don't want to see in the graph.
    -   `class_inference_in_object`: config the predicate that can inference the object is a `Class`, even if the class doesn't defined in the ontology.
    -   `label_property`: config the predicate that used for labeling nodes, if such a label exists, it will display inside the node.
    -   `tooltip_property`: config the predicate that contains the tooltip texts.
    -   `bnode_regex`: a list of regexes, if an uri matches, then it will be dispaly as a blank node without its uri nor label. It can be useful if you have a lot of reifications.
    -   `colors`: config the colors of nodes

        -   `class`, `literal`, `instance` can accept HEX value(e.g. `"#ff0000"` ), MATLAB style(e.g. `"r"` ), and color name (e.g. `"red"` ).

            "colors": {
              "class": "#ff0000",
              "literal": "r",
              "instance": "red",
            }

        -   `instance` can also accept a dict value to specify the color of each class instance. And use `"default"` to to set color for undefined instances.

            "instance": {
              "https://tac.nist.gov/tracks/SM-KBP/2018/ontologies/SeedlingOntology#Facility": "#a6cee3",
              "default": "#ffff99"
            }

        -   `filled`: config whether fill the node, default value: `true`.
-   Classes defined in the ontology will be omitted in the output graph. This action can be switched with argument `-V`.


### Useful Graphviz flags

-   `-K` to specify which [layout algorithm](https://graphviz.gitlab.io/_pages/pdf/dot.1.pdf) to use. E.g. `-Kneato` and `-Ksfdp` . Notice that inorder to use `sfdp` layout algorithm, you will need to build your graphviz with [GTS](http://gts.sourceforge.net).
-   `-T` to specify the [output format](https://graphviz.gitlab.io/_pages/doc/info/output.html).
-   `-G` to set a [graph attribute](https://graphviz.gitlab.io/_pages/doc/info/attrs.html). E.g. `-Goverlap=prism`


## Requirements

All the minimal Python requirements are installed during
```
python -m pip install ontoviz
```

For a development setup do
```
git clone https://github.com/WWU-AMM/ontoviz
cd ontoviz
virtualenv venv
. venv/bin/activate
python -m pip install -e .[full]
pre-commit install
```
This will also install tools for documentation building and testing

In order to convert `dot` into `png` or `svg` image, you will need [Graphviz](https://www.graphviz.org).


## Testing

Simply run `pytest` from the repository root. All tests are also run automatically by github actions on push/PR.
