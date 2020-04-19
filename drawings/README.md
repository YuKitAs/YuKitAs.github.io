# README

## Adding Drawings

1. Add new drawings into `drawings/resources/{sketch, digital}` with proper size.

2. Run the following script to update `manifest.json`:

  ```console
  $ scripts/add-drawings.py
  ```

  The default year is the current year, update it manually if needed.

## Validate Manifest

Make sure `ajv-cli` is installed and run:

```console
$ ajv -s manifest_schema.json -d manifest.json
```
