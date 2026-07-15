# Simultaneous E-Series Value Solver
The intention of this application is to automate the process of component value selection in real-world systems.<br/>
<br/>
This program solves systems of component-relationship equations for real-world [E-Series](https://wikipedia.org/wiki/E_series_of_preferred_numbers) values. The systems can be fully-determined or under-determined. Every combination of E-Series values is tested based on selected parameters, and the combination with the smallest error is found.

> [!NOTE]
> Requires Python 3.11 or later and SymPy 1.13.3 or later.<br/>
> If run without SymPy installed, a warning will be printed and the program will end.

## Running as a Script
This program is intended to be run as a script.<br/>
When running as a script, The program will prompt sequentially for each input.<br/>
<br/>
First, component names will be entered. Names must start with a letter, and letters and numbers can follow. Names can be of any length.<br/>
It is recommended to use standard schematic [component reference designators](https://wikipedia.org/wiki/Reference_designator).<br/>
When finished entering components, press `[ENTER]` on the empty input line.<br/>
<br/>

Next, component relationship equations are entered. These equations should be based on the topology of the circuit, and should reflect the desired effect for the circuit. They can be based on standard circuit equations for known topologies, or they can be found analytically through mesh/nodal circuit analysis. Use standard Python and SymPy algebraic operators. All equations must include an equals sign (`=`).<br/>
When finished entering component relationships, press `[ENTER]` on the empty input line.

### Valid Operators
| Operator | Example | Use |
| :---: | :---: | :---: |
| `+` | `A+B` | addition |
| `-` | `A-B` | subtraction |
| `*` | `A*B` | multiplication |
| `/` | `A/B` | division |
| `**` | `A**B` | exponentiation |
| `sqrt( )` | `sqrt(A)` | square root |
| `**(1/n)` | `A**(1/B)` | n-th root |
<br/>

Next, E-series are selected for each entered component. Only the number of the series should be entered. The program will proceed once every component has been associated with an E-Series.