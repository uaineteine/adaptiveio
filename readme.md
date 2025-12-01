# adaptiveio

![Python Version](https://img.shields.io/badge/python-3.10+-blue) ![Version 2.0.3](https://img.shields.io/badge/version-2.0.3-brightgreen)

## Description

The adaptiveio package provides tools for flexible and auditable data table management. It includes modules for:

- Handling pathing (`pathing.py`)
- Reading and writing tables in various formats (`jsonio.py`, `textio.py`)
- Centralized initialization and interface (`__init__.py`)

The package is designed to support transparent data operations, structured event logging, and easy integration into data pipelines. It enables users to load, process, and track text and JSON in different environments.

## Purpose

This package helps you read and write data in cloud and non-cloud environments in an agnostic way.

## Features

- Load and save tables in JSON and text formats
- Track metadata and maintain audit trails for all operations
- Simple integration into Python data workflows
- Designed for transparency and reproducibility

## Getting Started

1. Build the package:
   ```bash
   python build.py
   ```

## Modules

- `adaptiveio/pathing.py`: Identify and normalise pathing types
- `adaptiveio/jsonio.py`: Read and write JSON tables
- `adaptiveio/textio.py`: Read and write text tables
- `adaptiveio/__init__.py`: Centralized interface

## Documentation

See the `docs/` folder for usage instructions and API documentation.

## License

See the repository for license details.
