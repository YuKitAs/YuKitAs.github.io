# README


* `name_pl`: the plural form of category name, e.g. "squirrels"
* `name_sing`: the singular form of category name, e.g. "squirrel"

## Adding Photos to an Existing Category

1. **Add new resources**

    Copy `.jpg` photos into `photos/resources/<name_pl>` (`<name_sing>-<id>.jpg`: 800x600; `*<name_sing>-<id>-thumbnail.jpg`: 250x250; case-sensitive).

2. **Update manifest**

    Run the `add-photos.py` script to append a specified number of photos for the category into the manifest:

    ```console
    $ scripts/add-photos.py <number> -n <name_sing> -d <date> -l <location>
    ```

    * `number`: required, an positive integer
    * `name_sing`: required
    * `date`: in format `yyyy-mm-dd`, e.g. "2016-03-13"
    * `location`: e.g. "Karlsruhe, Germany"

## Adding Photos for an New Category

1. **Add new resources**

    Copy `.jpg` photos into `photos/resources/<name_pl>` (`<name_sing>-<id>.jpg`: 800x600; `*<name_sing>-<id>-thumbnail.jpg`: 250x250; case-sensitive).

2. **Update manifest**

    A singular to plural mapping must be added into `singular2plural` separated by comma: `<name_sing>,<name_pl>`.

    Run the `add-photos.py` script to create a new category in the manifest together with a specified number of photos:

    ```console
    $ scripts/add-photos.py <number> -n <name_sing> -d <date> -l <location>
    ```

    * `number`: required, an positive integer
    * `name_sing`: required
    * `date`: in format `yyyy-mm-dd`, e.g. "2016-03-13"
    * `location`: e.g. "Karlsruhe, Germany"

    The field `description` in the generated `manifest.json` is a HTML string that can/should be manually updated.

3. **Create a HTML page**

    Run the `create-page.sh` script to generate a HTML file for the new category which can be browsed at `/photos/<name>`:

    ```console
    $ ./scripts/create-page.sh <name_pl>
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
