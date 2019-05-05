# README

* `name` in the following context should be plural, e.g. "squirrels".
* `date` should be in format `yyyy-mm-dd`, e.g."2016-03-13".
* An example for `location` is "Karlsruhe, Germany".
* Optional descriptions can be added into `<div class="description"></div>`.

**Add new resources**

Copy `.jpg` photos into `photos/resources/<name>` (`*-raw.jpg`: 800x600; `*.jpg`: 250x250)

**Create a HTML page**

```console
$ ./scripts/create-page.sh <name>
```

This script will generate a HTML file for a specified category which can be browsed at `/photos/<name>`.

**Recreate all HTML pages**

```console
$ ./scripts/recreate-all-pages.sh
```

This script can be used to regenerate all the existing HTML files after modifying the template in `./scripts/html-template.sh`.

**Update manifest**

For a new category, a singular to plural mapping must be added into `singular2plural` before running the following script, e.g. "bonbon,bonbons".

```console
$ scripts/add-photos.py <number> -n <name> -d <date> -l <location>
```

Append a specified number of photos for a category into the manifest; a new category will be created if it doesn't exist yet.

**Validate manifest**

Make sure `ajv-cli` is installed.

```console
$ ajv -s manifest_schema.json -d manifest.json
```
