#!/usr/bin/env python3

import json
import os
import re
from datetime import datetime

MANIFEST_FILE = 'manifest.json'
SKETCH = 'sketch'
DIGITAL = 'digital'
DRAWINGS = 'drawings'

drawings = {SKETCH: [], DIGITAL: []}


# helpers
def _get_filename(file):
    return file.name.split('.')[0]


def _atoi(text):
    return int(text) if text.isdigit() else text


def _natural_keys(text):
    return [_atoi(c) for c in re.split('-', text)]


def read_files(cat):
    with os.scandir('resources/' + cat) as files:
        for file in files:
            drawings[cat].append(_get_filename(file))

        drawings[cat].sort(key=_natural_keys)


def create_drawing_entry(name):
    return {'id': int(name.split('-')[1]), 'name': name, 'year': datetime.now().year.__str__()}


def append_drawings(cat):
    name = cat['name']

    print('Adding to {}...'.format(name))

    if len(drawings[name]) > len(cat[DRAWINGS]):
        new_names = drawings[name][-(len(drawings[name]) - len(cat[DRAWINGS])):]
        for name in new_names:
            cat[DRAWINGS].append(create_drawing_entry(name))


if __name__ == '__main__':
    with open(MANIFEST_FILE) as manifest_file:
        with open(MANIFEST_FILE + '.backup', 'w+') as backup_file:
            backup_file.write(manifest_file.read())

    with open(MANIFEST_FILE) as manifest_file:
        manifest = json.load(manifest_file)

    data = manifest['data']

    read_files(SKETCH)
    read_files(DIGITAL)

    for cat in data:
        append_drawings(cat)

    manifest['data'] = data
    print(json.dumps(manifest, indent=2))

    with open(MANIFEST_FILE, 'w+') as new_manifest_file:
        json.dump(manifest, new_manifest_file, indent=2)
