[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "guinotify"
description = "A tiny frontend for inotify"
authors = [ { name= "Michael John", email= "michael.john@gmx.at" } ]
readme = "README.md"
keywords = ["inotify", "notification", "trigger"]
license = {text = "GPL"}
classifiers = [
    "Programming Language :: Python :: 3",
]
dependencies = [
    "requests",
    'importlib-metadata; python_version>="3.8"',
]
dynamic = ["version"]

[project.optional-dependencies]
#pdf = ["ReportLab>=1.2", "RXP"]
#rest = ["docutils>=0.3", "pack ==1.1, ==1.3"]

[project.urls]
homepage = "https://github.com/amstelchen/guinotify"
repository = "https://github.com/amstelchen/guinotify"
documentation = "https://github.com/amstelchen/guinotify"

[project.scripts]
gameinfo = "guinotify.guinotify:main"

[tool.setuptools.dynamic]
version = {attr = "guinotify.VERSION"}