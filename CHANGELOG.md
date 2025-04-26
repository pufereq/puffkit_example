# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - 2025-04-26

### Bug Fixes

- [`1b4287e`](https://github.com/pufereq/template-repo/commit/1b4287e367c933a608ec141c7e42721887303d3e) **widget_test_scene.py**: fix button state showing label logic

### Features

- [`1f61fdd`](https://github.com/pufereq/template-repo/commit/1f61fdddeb44455fb4c116b333f81b614d5bc257) **widget_test_scene.py**: add TextInputWidget to WidgetTestScene

### Miscellaneous Tasks

- [`5cc86ef`](https://github.com/pufereq/template-repo/commit/5cc86ef3b9fd29f067da2f07326219b0215885d7) correct token
- [`928b3ee`](https://github.com/pufereq/template-repo/commit/928b3ee3eff6c4f0c69bef11cea4910cdcb8bc2e) fix workflows to recurse submodules
- [`8489efc`](https://github.com/pufereq/template-repo/commit/8489efcba0f41c6f3d87394ce965f2729cc55edc) get working workflows from puffkkit

### Styling

- [`d232904`](https://github.com/pufereq/template-repo/commit/d2329044a7ac91b2d22ae45d757e4deb45180a68) **app.py**: ignore typing error of lambda function

### Build

- [`eca6678`](https://github.com/pufereq/template-repo/commit/eca66782ba97decfc5413855ea28a076d86bdcbf) **pdm.lock**: update puffkit to 0.10.1-post.3
- [`2006948`](https://github.com/pufereq/template-repo/commit/2006948a8d0a830a43dcd7572f160277ad0c4acc) **puffkit**: update puffkit to 0.10.1-post.3
- [`023644b`](https://github.com/pufereq/template-repo/commit/023644b97c8edaeb0c105136d6a0a74c87824da9) **tasks.json**: correct problemMatcher to python

## [0.2.0] - 2025-04-06

### Features

- [`000b22c`](https://github.com/pufereq/template-repo/commit/000b22ce079151527de565e154dcd8f405214e67) **app.py**: add WidgetTestScene
- [`c69921b`](https://github.com/pufereq/template-repo/commit/c69921bc4acbd743b03d0ac7d3a970bbbccbfe05) **widget_test_scene.py**: make WidgetTestScene pretty and include PkButtonWidget
- [`d4d2fb3`](https://github.com/pufereq/template-repo/commit/d4d2fb358c64fb80bd1b7a4c7caafc6d1a087917) **widget_test_scene.py**: add `WidgetTestScene`

### Miscellaneous Tasks

- [`82313f0`](https://github.com/pufereq/template-repo/commit/82313f0fd2ab1dcb33c7f04a938ddb5a80c4489a) **puffkit.code-workspace**: add workspace to make developing puffkit easier
- [`fec9b79`](https://github.com/pufereq/template-repo/commit/fec9b79cca557c60e7886bd0de7408b63edc06ae) **launch.json**: install depedencies on debug start
- [`da509a1`](https://github.com/pufereq/template-repo/commit/da509a105768ba69838f613879c7b5f272535076) **pdm.lock**: update depedencies
- [`f9acfae`](https://github.com/pufereq/template-repo/commit/f9acfaefe9ebe36adcde41837f837fd8c0f0159e) **pdm.lock**: update depedencies

### Testing

- [`1d28544`](https://github.com/pufereq/template-repo/commit/1d28544dff83a4e613221326aae7cf54e5672360) **__init__.py**: add empty test directory

### Build

- [`fe4fad5`](https://github.com/pufereq/template-repo/commit/fe4fad58fb15794e55af76bdae6fd1f14b15608d) **tasks.json**: add task to install deps
- [`82b15b3`](https://github.com/pufereq/template-repo/commit/82b15b33278cea340896a803285426fbba7cb34d) **puffkit**: update puffkit to 0.9.0
- [`8b8994b`](https://github.com/pufereq/template-repo/commit/8b8994be489b5f240872e073be7e7ab5a360ac03) **puffkit**: update puffkit to 0.7.0

## [0.1.0] - 2024-12-12

### Documentation

- [`4516744`](https://github.com/pufereq/template-repo/commit/4516744fefbc2f2e238ab86ef515acf7ca3147fb) **README.md**: change name of project to adapt to repo rename
- [`be02fc1`](https://github.com/pufereq/template-repo/commit/be02fc13847a8c9b06a3d2010e5960c83004972e) **README.md**: add README.md

### Features

- [`0633103`](https://github.com/pufereq/template-repo/commit/063310338a0b95a4247f4350c6f48be43f2f3d0f) **__main__.py**: add main start module
- [`82055f3`](https://github.com/pufereq/template-repo/commit/82055f3bfa596cef6cefc75fe2646eea685675d2) **puffkit_example/__init__.py**: add `__init__.py` to package
- [`18ca10a`](https://github.com/pufereq/template-repo/commit/18ca10abbc6a9a135fb562fe085b85a0e21cfe1c) **app.py**: add `ExampleApp`

### Miscellaneous Tasks

- [`378ab26`](https://github.com/pufereq/template-repo/commit/378ab2693aa0b75130d0986de6f9c9b0e98b1fa7) **release.yaml**: recurse submodules on checkout
- [`d82eb4b`](https://github.com/pufereq/template-repo/commit/d82eb4bb3758937d93f1f625999bfa2f64be847c) **release.yaml**: remove unfinished code
- [`6239d4b`](https://github.com/pufereq/template-repo/commit/6239d4bf18dcfec4a27a9a180914ed60bcb46748) **.vscode**: add `.vscode`
- [`1c41f4c`](https://github.com/pufereq/template-repo/commit/1c41f4c8c821d33785168475262b54c88340e976) **.gitignore**: add PDM-specific entries to gitignore

### Build

- [`b614852`](https://github.com/pufereq/template-repo/commit/b61485234d2f09deffd652dd63a0da32c70e26d1) **pyproject.toml**: rename the project to use an underscore instead of hyphen
- [`1c8cf9b`](https://github.com/pufereq/template-repo/commit/1c8cf9b27a1ff55f57f631149eeb083e35bf680f) **pyproject.toml**: fix wrong path in semantic_release options
- [`79a30e8`](https://github.com/pufereq/template-repo/commit/79a30e855c2462dd7f4783cdb61ce3b3e0b3f138) **puffkit**: update puffkit to 0.5.0
- [`ece8f9d`](https://github.com/pufereq/template-repo/commit/ece8f9de49e6b73ee9a43cfe1a41f7dc3959fdf8) **pyproject.toml**: fix typo
- [`947897b`](https://github.com/pufereq/template-repo/commit/947897b604af53221a509ebe8830b29af5ff5551) **pyproject.toml**: add a script to easily run the app
- [`4034f4e`](https://github.com/pufereq/template-repo/commit/4034f4ef382b0757cec3370ec1d0ad823346d73d) **pdm.lock**: add PDM lockfile
- [`3f52b20`](https://github.com/pufereq/template-repo/commit/3f52b201139738c707d7fc4903fa04103bd96957) **pyproject.toml**: add pyproject.toml
- [`721c4f4`](https://github.com/pufereq/template-repo/commit/721c4f46f531f528b1d47f612024c59b6d8a2aac) **puffkit**: add `puffkit` submodule

<!-- generated by git-cliff -->
