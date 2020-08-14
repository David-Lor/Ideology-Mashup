# IdeologyMashup

Mashup tool to generate ideologies by combining two ideologies or philosophies.

## Ideologies definition

Ideologies are defined on the [ideologies.yaml](ideologies.yaml) file, following the structure of the given examples.

Each ideology can have a `name` and/or a `prefix` (can have one of them or both).
The mashup is done by mixing all prefixes with all names, but a prefix and a name of a same ideology won't be mixed.

For example, given the following YAML file:
```yaml
ideologies:
  - name: socialism
    prefix: social
  - prefix: anti
  - name: democracy
```

Will result in:
```
Social-Democracy
Anti-Democracy
Anti-Socialism
```

## Usage

Until no CLI interface is provided, the mashup can be done running the following command:

```bash
# Assuming we are on project root path, and having a valid ideologies.yaml file:
python tools/generate_mashed_ideologies.py
# A file mashed_ideologies.txt is created
```

## Requirements

- Python >= 3.6
- Requirements listed on [requirements.txt](requirements.txt)

## Changelog

- 0.0.1 - Initial release

## TODO

- Add CLI interface
- Add a picture for each ideology
- Export mashed ideologies on ndjson
