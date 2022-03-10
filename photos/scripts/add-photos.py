#!/usr/bin/env python3

# Update manifest.json according to (locally) existing category directory and photos.

import argparse
import json
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument('name', type=str)
parser.add_argument('-n', '--number', type=int, default=0)
parser.add_argument('-d', '--date', default='')
parser.add_argument('-l', '--location', default='')
parser.add_argument('-c', '--camera', default='Canon EOS 60D')
parser.add_argument('--dryrun', action='store_true', default=False)
args = parser.parse_args()

photo_info = {
    'name': args.name.lower(),
    'date': args.date,
    'location': args.location,
    'camera': args.camera
}

dryrun = args.dryrun

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


PHOTO_NAME = photo_info['name']
CAT_NAME = get_plural(PHOTO_NAME)


def get_all_photos_num():
    # count photo files named like 'squirrel-42.jpg'
    photos = list(filter(lambda f: re.findall('^{}-[1-9][0-9]*\\..*$'.format(PHOTO_NAME), f),
                         os.listdir(os.path.join(os.getcwd(), 'resources', CAT_NAME))))
    return len(photos)


def create_photo(numeric_id):
    return {'id': numeric_id, 'name': '{}-{}'.format(photo_info['name'], numeric_id), 'date': photo_info['date'],
            'location': photo_info['location'], 'camera': photo_info['camera']}


def create_category():
    new_photos = []
    new_photos_num = args.number if args.number > 0 else get_all_photos_num()
    print('Adding new photos: {}'.format(new_photos_num))
    for i in range(1, new_photos_num + 1):
        new_photos.append(create_photo(i))

    return {'name': CAT_NAME, 'description': '', 'photos': new_photos}


def append_photos_to_category(category):
    num = len(category['photos'])
    print('Existing photos: {}'.format(num))
    new_photos_num = args.number if args.number > 0 else (get_all_photos_num() - num)
    print('Adding new photos: {}'.format(new_photos_num))
    for i in range(num + 1, num + new_photos_num + 1):
        last_index = category['photos'][-1]['id']
        category['photos'].append(create_photo(last_index + 1))

    return category


if __name__ == '__main__':
    if not CAT_NAME:
        exit(0)

    with open(MANIFEST_FILE) as manifest_file:
        with open(MANIFEST_FILE + '.backup', 'w+') as backup_file:
            backup_file.write(manifest_file.read())

    with open(MANIFEST_FILE) as manifest_file:
        manifest = json.load(manifest_file)

    data = manifest['data']

    for cat in data:
        if cat['name'] == CAT_NAME:
            print('Adding to existing category "{}"...'.format(CAT_NAME))
            cat = append_photos_to_category(cat)
            print(json.dumps(cat, indent=2))
            break
    else:
        print('Creating new category "{}"...'.format(CAT_NAME))
        data.append(create_category())
        print(json.dumps(data[-1], indent=2))

    if not dryrun:
        manifest['data'] = data

        with open(MANIFEST_FILE, 'w+') as new_manifest_file:
            json.dump(manifest, new_manifest_file, indent=2)
