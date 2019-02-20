# XmlMenu

Fast XML trigger menu reader in pure python for inspection and diagnosis utilities.

## Install

Install using pip (depends on `lxml`).

```bash
pip install git+https://github.com/arnobaer/xmlmenu.git
```

## Usage

Load a menu from XML file

```python
from xmlmenu import XmlMenu
menu = XmlMenu("L1Menu_Sample.xml")
```

Access menu meta information

```python
menu.name
'L1Menu_Sample'
menu.comment
'NO-Body expects the spanish inquisition!'
```

Iterate over algorithms

```python
for algorithm in menu.algorithms:
    print(algorithm.index, algorithm.name)
```

Filter algorithms by attributes

```python
for module in range(menu.n_modules):
    for algorithm in menu.algorithms.byModule(module):
        do_something(...)
```

### Command line

Dump content subset of menu in JSON format.

```bash
xmlmenu L1Menu_Sample.xml
```
