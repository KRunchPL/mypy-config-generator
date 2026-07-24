# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-07-25

### Changed

- Support for configuration file
- In `adjusted.ini`, `strict` flag is no longer enabled, instead specific flags are
- Rewriting for typer

### Removed

- There is no way to run just one of commands anymore
- KRunchPL overrides are no longer included by default

## [1.0.0] - 2025-02-08

### Added

- Downloading `mypy` settings page and generating `mypy` file with all available options set to their default values. The file also contains options' descriptions as fields comments.
- Generating config with adjusted values.
