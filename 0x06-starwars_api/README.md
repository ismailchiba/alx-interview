# Star Wars Characters Script

This script prints all characters of a specified Star Wars movie.

## Usage

The script takes one positional argument, which is the Movie ID. For example, `3` corresponds to "Return of the Jedi".

```bash
python script.py <Movie ID>
```

## Example

```bash
python script.py 3
```

This will display the names of all characters in "Return of the Jedi", one per line, in the same order as they appear in the `characters` list in the `/films/` endpoint of the Star Wars API.

## Requirements

- Python 3.x
- `requests` module

## Installation

To install the `requests` module, run:

```bash
pip install requests
```

## API

This script uses the [Star Wars API](https://swapi.dev/).

## Notes

- Ensure you have an active internet connection to fetch data from the Star Wars API.
- The script handles HTTP requests and parses JSON responses to retrieve character names.

## License

This project is licensed under the MIT License.