# Tensegrity Sim

This repository contains a simulation framework for tensegrity structures. It supports continuous cables and 2D, 2.5D, and 3D structures.

## Research Context

Tensegrity Sim is a Python-based simulation framework developed to support research on tensegrity mechanisms, with an emphasis on continuous cable models and mixed-dimensional (2D, 2.5D, and 3D) structures.  

The software is designed to support reproducible simulation of static equilibrium configurations under prescribed control inputs, and to facilitate extension toward optimization, control, and hardware-in-the-loop experimentation.

This software implements the models and numerical methods described in:

> Brown, A. *Modeling and Simulation of Tensegrity Structures with Continuous Cables*. Brigham Young University, 2025.
>
> Brown et al. “TensegritySim Python Package Using Virtual Work.” Submitted to the *ASME Journal of Mechanisms and Robotics*.

Configuration files used by the project are provided in the `yaml` directory. See the [reproducibility guide](REPRODUCIBILITY.md) for the environment, commands, and the paper-to-configuration mapping that should be completed before publication.

## Reproducibility and Usage

To get started with development, clone the repo and install the dependencies.

Python 3.9–3.12 is supported. We recommend using a virtual environment to keep this project's dependencies separate from the system Python installation:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

To run the project:
```bash
python3 main.py <path/to/yaml/config>
```
Sample YAML configuration files are provided in the `yaml` directory. See the [simulation setup](docs/sphinx/content/setup.md) and [YAML reference](docs/sphinx/content/yaml.md) for details.

The program opens Matplotlib windows and then accepts control-length changes interactively in the terminal. Enter `q` to quit. The optional structure-building GUI can be launched with:

```bash
python GUI/GUI_frontend.py
```

## Installation

To use the project as a library, run `python -m pip install .` from the repository root. This installs the `TensegritySim` module so it can be imported by other projects.

For development, install the package and test dependencies in editable mode and run the tests:

```bash
python -m pip install -e ".[test]"
python -m pytest -q
```

## Citation

Use the repository's **Cite this repository** menu, which is generated from [`CITATION.cff`](CITATION.cff). Cite a tagged, archived release rather than the moving `main` branch when a release DOI becomes available.

## Definitions and Conventions (as used in this project)
Strings - Strings are connection types that only carry tension, they lengthen as force is applied  
Bar - A bar can carry either tension or compression, but does not change length  
Forces - Tensions are positive values and compression forces in connections are negative.

## Modeling Assumptions

The simulation framework adopts the following modeling conventions:

- Strings carry tension only and may change length under load.
- Bars may carry tension or compression and are assumed to be inextensible.
- Tension forces are represented as positive values; compression forces are negative.
- Equilibrium configurations are computed using numerical optimization.

These assumptions are consistent with those described in the accompanying paper.

## Limitations

The solver assumes quasi-static equilibrium and may not converge for highly overconstrained or ill-conditioned configurations.

## Scope of Implementation

The current implementation supports static equilibrium analysis of tensegrity structures with tension-only cable elements and inextensible bars. Dynamic effects, damping, and contact interactions are not included.

## Organization
`main.py` provides an example entry point for running simulations using YAML-defined models and control inputs.

### TensegritySim Module
The `TensegritySim` directory contains the Python package.
* `data_structures.py` contains the `Node`, `Connection`, `Surface`, and `Tensegrity` classes
* `yaml_parser.py` reads a YAML file and returns a `Tensegrity` object. See the [YAML reference](docs/sphinx/content/yaml.md)
* `visualization.py` shows the tensegrity structure using matplotlib
* `tensegrity_solver.py` uses an optimizer to solve for an updated structure

### yaml
The `yaml` directory contains sample YAML files for running the simulation.
