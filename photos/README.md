# README

**Terms**

* `id`: an auto-increment numeric id for each photo in a category
* `cat_name`: the plural form of the category, e.g. "squirrels"
* `photo_name`: the singular form of the category, e.g. "squirrel"


## Adding New Photos

Copy `.jpg` files into `photos/resources/<cat_name>` (`<photo_name>-<id>.jpg`: 800x600; `*<photo_name>-<id>-thumbnail.jpg`: 250x250; case-sensitive).


## Adding Photos to an Existing Category

### Update manifest

Run the `add-photos.py` script to append a specified number of photos for the category into the manifest:

```console
$ scripts/add-photos.py <photo_name> -n <number> -d <date> -l <location> [--dryrun]
```

* `photo_name`: required
* `number`: optional, an positive integer; if not specified, all the new photos will be added.
* `date`: in format `yyyy-mm-dd`, e.g. "2016-03-13".
* `location`: e.g. "Karlsruhe, Germany".


## Adding Photos for an New Category

### Update manifest

A singular to plural mapping must be added into `singular2plural` separated by comma: `<photo_name>,<cat_name>`.

Run the `add-photos.py` script to create a new category in the manifest, the parameters are the same as above.


The field `description` in the generated `manifest.json` is a HTML string that can/should be manually updated.

### Create a HTML page

Run the `create-page.sh` script to generate a HTML file `<cat_name>.html` in the current directory for the new category:

```console
$ ./scripts/create-page.sh <cat_name>
```


## Modifying HTML Template

The template can be found in `./scripts/html-template.sh`. After modification, run the `recreate-all-pages.sh` script to regenerate all the HTML pages for each category.

```console
$ ./scripts/recreate-all-pages.sh
```


## Validate Manifest

Make sure `ajv-cli` is installed and run:

```console
$ ajv -s manifest_schema.json -d manifest.json
```
