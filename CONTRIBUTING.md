# Contributing

## Getting Started

Make sure you have [Poetry](https://python-poetry.org) installed. After cloning
the repo, create the environment with

```bash
poetry install
```

The `Makefile` contains commands for common tasks.

## Running Tests

```bash
make test
```

## Linting

```bash
make lint
```

## Shell

This will activate a virtual environment with the dependencies.

```bash
poetry shell
```

## Documentation

Edit the README as needed.

## Deployment

To deploy, make sure the dev requirements are installed. Then run:

```bash
make release
```

Alternatively, mark a new version with `bump2version` (do this in a shell) and
push the commit and tag with:

```bash
git push
git push --tags
```

GitHub Actions will then build and deploy the appropriate versions.
