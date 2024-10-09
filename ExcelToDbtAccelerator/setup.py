import os
import sys
from setuptools import setup, find_packages

# Ensure Python version is 3.7 or higher
if sys.version_info < (3, 7):
    sys.exit('Sorry, Python < 3.7 is not supported')

def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'src', 'etda', 'version.py')
    with open(version_file, encoding='utf-8') as f:
        exec(f.read())
    return locals()['__version__']

# Core dependencies
INSTALL_REQUIRES = [
    "pandas>=1.0.0",
    "PyYAML>=5.1",
    "openpyxl>=3.0.0",
]

# Development dependencies
DEV_REQUIRES = [
    'pytest',
    'flake8',
    'black',
    'mypy',
]

# Classifiers
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

setup(
    name="ExcelToDbtAccelerator",
    version=get_version(),
    author="Gou Ali",
    author_email="abdellatif.gou-ali@artefact.com",
    description="Excel To DBT Accelerator - Automate DBT schema and documentation generation",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/abdelgou",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=CLASSIFIERS,
    python_requires=">=3.7",
    install_requires=INSTALL_REQUIRES,
    extras_require={'dev': DEV_REQUIRES},
    entry_points={
        "console_scripts": [
            "etda=etda.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)