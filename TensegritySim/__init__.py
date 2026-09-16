"""
TensegritySim Package

This package provides tools for simulating and visualizing tensegrity structures.
"""

from importlib.metadata import PackageNotFoundError, version

from .data_structures import Node, Connection, Surface, Tensegrity
from .yaml_parser import YamlParser
from .visualization import Visualization
from .tensegrity_solver import TensegritySolver

__all__ = ["Node", "Connection", "Surface", "Tensegrity", "YamlParser", "Visualization", "TensegritySolver"]

try:
    __version__ = version("TensegritySim")
except PackageNotFoundError:
    # The source tree may be imported before the package is installed.
    __version__ = "0+unknown"
