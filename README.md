# Ochi

![PyPI - License](https://img.shields.io/pypi/l/ochi?style=flat-square)

Ochi is a simple CLI to navigate Hacker News in the terminal made with the [Textualize/rich](https://github.com/Textualize/rich) and [pallets/click](https://github.com/pallets/click) packages. In the future, when the awesome [Textualize/textual](https://github.com/Textualize/textual) package launches its documentation I will update this project with a complete TUI.

[![asciicast](https://asciinema.org/a/527446.svg)](https://asciinema.org/a/527446)

## Installation
`ochi` is hosted on [PyPi](https://pypi.org/project/ochi/). So you can install it with:

```bash
pip install ochi
```

Or install it from its GitHub repository:

```bash
pip install git+https://github.com/daniarlert/ochi.git
```

> Note that you may need to run `pip3` instead of `pip` or use `python -m` depending on your setup.

## Usage

### Basic usage

The most simple way to start using `ochi` is by just running:

```bash
ochi
```

> To see all the flags `ochi` has available, use the `--help` flag.

By default, `ochi` fetchs and displays the latest 500 stories on the selected category which in this case is `top` (*topstories*). So a better way to start may be:

```bash
ochi --max 10

# Or

ochi -m 10
```

### Categories

To get stories from other categories just use the `-c` or `--category` flag:

```bash
ochi --category new

# Or

ochi -m 10 -c job
```

### Order by

You can order stories by its ID, Score or posted date and reverse its order if you want to:

```bash
ochi -m 10 --order-by date

# Or

ochi -m 10 --order-by date --reverse
```

## Futures
- Bookmarks/save stories.
- Configuration for colorschemes and defaults.
- View post with comments.
- View user profile.
