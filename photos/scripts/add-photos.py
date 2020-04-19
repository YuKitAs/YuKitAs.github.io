#!/usr/bin/env python3

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)
parser.add_argument('-n', '--name', required=True)
parser.add_argument('-d', '--date', default='')
parser.add_argument('-l', '--location', default='')
args = parser.parse_args()

photos_num = args.number

photo_info = {
    'name': args.name.lower(),
    'date': args.date,
    'location': args.location,
    'camera': 'Canon EOS 60D'
}

MANIFEST_FILE = 'manifest.json'

def get_plural(singular):
    with open('singular2plural') as mapping_file:
        mapping_lines = mapping_file.readlines()

    mappings = {}
    for mapping_line in mapping_lines:
        mapping = mapping_line.split(',')
        mappings[mapping[0]] = mapping[1].rstrip()

    if singular not in mappings:
        print('Plural form of "{}" not found!'.format(singular))
        return None

    return mappings[singular]


def create_photo(id):
    return {'id': id, 'name': '{}-{}'.format(photo_info['name'], id), 'date': photo_info['date'],
            'location': photo_info['location'], 'camera': photo_info['camera']}


def create_category(cat_name):
    new_photos = []
    for i in range(1, photos_num + 1):
        new_photos.append(create_photo(i))

    return {'name': cat_name, 'description': '', 'photos': new_photos}


def append_photos_to_category(category):
    num = len(category['photos'])
    for i in range(num + 1, num + photos_num + 1):
        category['photos'].append(create_photo(i))

    return category


if __name__ == '__main__':
    plural_name = get_plural(photo_info['name'])
    if not plural_name:
        exit(0)

    with open(MANIFEST_FILE) as manifest_file:
        with open(MANIFEST_FILE + '.backup', 'w+') as backup_file:
            backup_file.write(manifest_file.read())

    with open(MANIFEST_FILE) as manifest_file:
        manifest = json.load(manifest_file)

    data = manifest['data']

    for cat in data:
        if cat['name'] == plural_name:
            print('Adding to existing category "{}"...'.format(plural_name))
            cat = append_photos_to_category(cat)
            break
    else:
        print('Creating new category "{}"...'.format(plural_name))
        data.append(create_category(plural_name))

    manifest['data'] = data
    print(json.dumps(manifest, indent=2))

    with open(MANIFEST_FILE, 'w+') as new_manifest_file:
        json.dump(manifest, new_manifest_file, indent=2)
