# Mypy Configuration Generator

Tool that generates [`mypy`](https://mypy.readthedocs.io/) configuration with all available options.

## Usage

```console
python -m mypy_config_generator download
python -m mypy_config_generator generate
```

The first command will download the settings HTML page and the second will analyze it and generate `ini` file with all available options set to their defualt values. The file will also contain options descriptions as comments.

Output files will be saved in the `workdir` folder as `settings.html` and `mypy.ini`.

On the repository, the `workdir` folder contains result of the above commands for latest mypy version I have been using. It also contains `mypy_adjusted.ini` which contains latest configuration with values adjusted to my personal projects.

## Additional documentation

[Development documentation](README-DEV.md)

[Changelog](CHANGELOG.md)
