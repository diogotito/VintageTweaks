VintageTweaks
=============

I could configure [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous) to selectively enable some keys.

Or I could hack a bunch of key bindings and Python commands on top of the built-in _Vintage_ plugin to grab the subset of Vim features I actually enjoy, which are:

  - keyboard-driven navigation
  - <code>&lt;C-w&gt;</code> window management

I prefer Sublime's features more than Vim's for the rest, and I find that the more advanced Vim emulation packages are too close to Vim for my liking.

But maybe I should just try NeoVintageous for real, so I'm putting my _Vintage_-enhancing key bindings and commands in this package so that I can easily toggle them all at once.

Installation
------------

### Pre-requisites

Ensure [Origami](https://github.com/SublimeText/Origami) is installed for the `<C-w>` key bindings to work, as many of them are bound to Origami commands.
  - _Preferences_ > _Package Control_ > `Install Package`, `Origami`.

### Cloning

Clone this repo under your Packages directory.
You can open it via _Preferences_ > _Browse Packages..._
or discover its location by running `sublime.packages_path()` in the Console (<kbd>Ctrl</kbd> <kbd>`</kbd>)

```sh
git clone https://github.com/diogotito/VintageTweaks.git
```
