# Fielparser Projekt

## Installation

uv sync
pre-commit install
pre-commit run --all-files

## Nutzung als selbststehendes Programm
Der folgende Aufruf funktioniert nur deshalb, weil `__main__.py`
implementiert ist (siehe __main__.py)

    uv run -m fileparser example.txt


## Nutzung als Import
Wenn das Projekt zb. via PyPI oder Github installiert wird,
dann soll es so genutzt werden:

    from fileparser import parse

(der direkte Import von parse geht deshalb, 
weil wir in fileparser/__init__.py die parse-Funktion importiert haben)

## Lokale Tests ausführen

    uv run pytest -v -s


## Aus github installieren (Main Branch)

pip install git+https://github.com/bobjack34/fileparser.git@main