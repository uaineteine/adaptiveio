from setuptools import setup, find_packages

requirements = ['pyspark', 'pandas']
long_description = '# adaptiveio\n\n![Python Version](https://img.shields.io/badge/python-3.10+-blue) ![Version 2.0.1](https://img.shields.io/badge/version-2.0.1-brightgreen)\n\n## Description\n\nThe adaptiveio package provides tools for flexible and auditable data table management. It includes modules for:\n\n- Handling pathing (`pathing.py`)\n- Reading and writing tables in various formats (`jsonio.py`, `textio.py`)\n- Centralized initialization and interface (`__init__.py`)\n\nThe package is designed to support transparent data operations, structured event logging, and easy integration into data pipelines. It enables users to load, process, and track text and JSON in different environments.\n\n## Purpose\n\nThis package helps you read and write data in cloud and non-cloud environments in an agnostic way.\n\n## Features\n\n- Load and save tables in JSON and text formats\n- Track metadata and maintain audit trails for all operations\n- Simple integration into Python data workflows\n- Designed for transparency and reproducibility\n\n## Getting Started\n\n1. Build the package:\n   ```bash\n   python build.py\n   ```\n\n## Modules\n\n- `adaptiveio/pathing.py`: Identify and normalise pathing types\n- `adaptiveio/jsonio.py`: Read and write JSON tables\n- `adaptiveio/textio.py`: Read and write text tables\n- `adaptiveio/__init__.py`: Centralized interface\n\n## Documentation\n\nSee the `docs/` folder for usage instructions and API documentation.\n\n## License\n\nSee the repository for license details.\n'

setup(
    name="adaptiveio",
    version="2.0.1",
    author="",
    author_email="",
    description="A python package of a working transforms framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(include=["adaptiveio", "adaptiveio.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=requirements
)
