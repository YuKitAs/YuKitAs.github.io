# README

## Adding Photos to an Existing Category

1. **Add new resources**

    Copy `.jpg` photos into `photos/resources/<name>` (`*-raw.jpg`: 800x600; `*.jpg`: 250x250).

2. **Update manifest**

    Run the `add-photos.py` script to append a specified number of photos for the category into the manifest:

    ```console
    $ scripts/add-photos.py <number> -n <name> -d <date> -l <location>
    ```
    `number` (_required_) should be an positive integer; `name` (_required_) should be singluar, e.g. "fox"; `date` should be in format `yyyy-mm-dd`, e.g."2016-03-13"; an example for `location` is "Karlsruhe, Germany".

## Adding Photos for an New Category

1. **Add new resources**

    Copy `.jpg` photos into `photos/resources/<name>` (`*-raw.jpg`: 800x600; `*.jpg`: 250x250).

2. **Update manifest**

    A singular to plural mapping must be added into `singular2plural`, e.g. "bonbon,bonbons".

    Run the `add-photos.py` script to create a new category in the manifest together with a specified number of photos:

    ```console
    $ scripts/add-photos.py <number> -n <name> -d <date> -l <location>
    ```

    `number` should be an positive integer; `name` should be singluar, e.g. "bon"; `date` should be in format `yyyy-mm-dd`, e.g."2016-03-13"; an example for `location` is "Karlsruhe, Germany".

    The field `description` in the generated `manifest.json` is a HTML string that can be manually updated.

3. **Create a HTML page**

    Run the `create-page.sh` script to generate a HTML file for the new category which can be browsed at `/photos/<name>`:

    ```console
    $ ./scripts/create-page.sh <name>
    ```
    `name` should be plural, e.g. "squirrels".

## Modifying HTML Template

The template can be found in `./scripts/html-template.sh`. After modification, run the `recreate-all-pages.sh` script to regenerate all the HTML pages for each category.

```console
$ ./scripts/recreate-all-pages.sh
```

## Validate Manifest##

Make sure `ajv-cli` is installed.

```console
$ ajv -s manifest_schema.json -d manifest.json
```
