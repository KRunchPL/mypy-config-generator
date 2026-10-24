# Mypy Configuration Generator

Tool that generates [`mypy`](https://mypy.readthedocs.io/) configuration with all available options.

## Usage

```console
mypy-config-generator [--config adjustments.toml]
```

The command will download the settings HTML page, analyze it, and generate two `ini` files. Both `ini` files will contain all available `mypy` options along with their descriptions. The options will be organized into sections, similar to how they are presented in the documentation. The difference between the two files is that one will have all settings set to their default values, while the other will have values adjusted according to provided config file.

For an example of `adjustments.toml` file, see [krunch_pl_config.toml](./krunch_pl_config.toml).

Output files will be saved in the `workdir` folder as `settings.html`, `default.ini` (default values) and `adjusted.ini`.

On the repository, the `workdir` folder contains result of the above command for latest mypy version I have been using.

## Additional documentation

[Development documentation](README-DEV.md)

[Changelog](CHANGELOG.md)
