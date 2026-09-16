# Contributing

Thank you for helping improve TensegritySim.

## Development setup

1. Fork and clone the repository.
2. Create and activate a Python 3.9–3.12 virtual environment.
3. Run `python -m pip install -e ".[test]"`.
4. Run `python -m pytest -q` before submitting a change.

## Pull requests

Keep each pull request focused and explain the motivation, implementation, and validation performed. Add or update tests when behavior changes. Update the README, YAML reference, or reproducibility guide when an interface or scientific assumption changes.

For changes that affect numerical results, include the configuration file, expected result, tolerances, and a comparison with the prior behavior. Do not commit virtual environments, caches, generated build directories, or large result files.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
