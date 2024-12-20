
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
setup(
    name="ripwrap",
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    install_requires=["pydantic", "pytesseract", "typer"],
    extras_require={  # Optional
        "dev": ["pip-tools", "mypy"]
    },
    package_dir={"": "src"},
)
