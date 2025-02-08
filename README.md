# Mypy Configuration Generator

Tool that generates [`mypy`](https://mypy.readthedocs.io/) configuration with all available options.

## Usage

```console
python -m mypy_config_generator
```

The command will download the settings HTML page, analyze it, and generate two `ini` files. Both `ini` files will contain all available `mypy` options along with their descriptions. The options will be organized into sections, similar to how they are presented in the documentation. The difference between the two files is that one will have all settings set to their default values, while the other will have values adjusted to my personal preferences.

Output files will be saved in the `workdir` folder as `settings.html`, `mypy.ini` (default values) and `mypy_adjusted.ini`.

On the repository, the `workdir` folder contains result of the above command for latest mypy version I have been using.

## Additional documentation

[Development documentation](README-DEV.md)

[Changelog](CHANGELOG.md)
