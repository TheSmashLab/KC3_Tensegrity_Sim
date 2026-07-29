# YAML Reference <!-- omit from toc -->
## Purpose and Scope

This document specifies the YAML-based configuration interface used to define tensegrity models for simulation. Each parameter corresponds directly to quantities defined in the accompanying thesis and journal paper.  

The YAML files serve as the *scientific interface* to the simulation framework, enabling reproducible specification of geometry, connectivity, material behavior, constraints, and actuation.

The config file is a YAML file defining:
- [Nodes](#nodes)
- [Connections](#connections)
- [Builders](#builders)
- [Pins](#pins)
- [Control](#control)
- [Surface](#surface)
  - [Type](#type)
  - [Linked Nodes](#linked-nodes)

These sections can be defined in any order in the YAML file, but it is easiest to logically go through them in the order defined above.

There are sample config files in the `yaml` directory.

## Nodes
**Theoretical correspondence:**  
Node coordinates correspond to the position vectors $\mathbf{x}_i$ defined in Chapter 3 of the thesis.

Nodes are the points that bars and strings connect at.

Nodes have a name and initial x, y, z positions.  
A node named `Node1` with x = 1, y = 2, and z = 0, it would look like:

```yaml
nodes:
    Node1: [1, 2, 0]
```

The Tensegrity class sets the number of dimensions to 2 or 3 based on the number of coordinates given for the nodes. If all nodes have 3 coordinates, the structure is solved in 3D space. If any node is defined with only two coordinates, the structure is solved in two-dimensional space.

## Connections
Connections are how the nodes are connected to each other. An arbitrary number of connection types may be defined, each associated with a corresponding [Builders](#builders) specification.

A connection type named `strings` with a connection between `Node1` and `Node2` looks like:

```yaml
connections:
    strings:
        - [Node1, Node2]
```

Connections can also optionally be named (for later specifying connections to control).

```yaml
connections:
    strings:
        - string1: [Node1, Node2] # Named connection
        - [Node2, Node3] # Unnamed connection
```

String connections (as defined in the builders section) can pass through multiple nodes. They are assumed to frictionlessly pass through nodes and therefore always have the same tension along it's entire length.

```yaml
connections:
    strings:
        - string1: [Node1, Node2, Node5, Node6]
```

## Builders
Builders are the connection properties that define the strings or bars that hold the nodes together.
A builder must have a name matching a connection type in the `Connections` section.

For the `string` connection type with a stiffness (k) of 100N/m and the unstretched length of the string 95% of the currently defined length between nodes:

```yaml
builders:
    strings:
        stiffness: 100
        type: string
        initial_length_ratio: 0.95
```
**Theoretical correspondence:**  
The stiffness parameter corresponds to the axial stiffness $k$ used in the constitutive model described in Section 3.2 of the thesis. Units are consistent across all simulations but are not enforced by the solver.

If the unstretched length of the string is unknown but the tension is known, Hooke's Law can be used to calculate the initial length: $F = k * (l_s - l)$ where $l_s$ is the stretched length of the string (distance between it's nodes) and $l$ is the unstretched length.

Bars are defined in the builder's sections just like strings. The `initial_length_ratio` is normally left out because bars are usually significantly stiff enough it is assumed to be 1

```yaml
builders:
    bars:
        stiffness: 10000
        type: bar
```
**Important**: The name of each builder can be what ever the user desires (bars, strings, high_tension_strings, blue_string, red_springs, etc), but the defined type in each must be exactly `bar` or `string`

## Pins
In 2D space the solved structure can float anywhere in the XY plane with any rotation unless we pin nodes (to define a place in XY space the structure is fixed to)

A pin needs a node name and a list of True/False values, with True indicating that the node is translationally pinned in that direction. To pin `Node1` in the x and y directions:
```yaml
pin:
  Node1: [True, True, False]
```

## Control
The `control` section defines which strings are able to be controlled (change length).

To define a control string the name of the connections need to be defined. For instance if the connection `String1` is being controlled:
```yaml
control:
  - String1
```

## Surface
### Type
The only type of surface currently implemented is a cylinder. A radius must be specified for the radius of the cylinder to wrap the tensegrity around.

The structure is wrapped around a $\hat{k}$ axis. In other words the x-axis wraps the circumference of the cylinder with a set radius, r. Future extensions may allow spatially varying surface geometry; however, only constant-radius cylindrical surfaces are currently supported.

### Linked Nodes
The linked nodes section takes pairs of nodes to be connected to each other on opposite sides of the cylinder.

```yaml
surface:
  cylinder:
    radius: 3.5

  linked_nodes:
    - [Node1, Node7]
    - [Node4, Node8]
    - [Node9, Node12]
```
The only currently defined surface for linking nodes around is a cylinder.

## Reproducibility Notes

All YAML files used to generate figures and results in the accompanying journal paper are provided in the `yaml/` directory of the repository.  

Each file fully specifies the model state and control parameters required to reproduce the corresponding simulation results, without reliance on hard-coded values.

Configuration file names correspond to figures and case studies presented in the journal paper where applicable.

