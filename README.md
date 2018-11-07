# SimplePlotter App
## Requirements
1. Download and install [Python 3.7.1](https://www.python.org/downloads/).
2. After successful installation, open command prompt, type ```pip install plotly``` and press Enter. This will download and install PlotLy library.<br>
3. After installation is finished, double click Main.py to launch application.
## Usage
1. For now application is able to plot analytical and numerical solutions of ```y' = 4x - 2y```, absolute global truncation error of numerical methods and dependence of their errors from amount of steps.
2. Application supports Euler, Improved Euler and Runge-Kutta methods. Application plots them on one sheet, you can hide uninterested methods by clicking on its label in legend.
3. All made plots are saved in ```<app_directory>/plots``` directory.
4. Do not mark ```Plots of function for every N``` and ```Plots of absolute errors for every N``` for big ranges of amount of steps.
## Code
1. Code is divided in several parts.
2. First is ```Main.py```. The main executable file, runs application. Dependent from ```Globals.py``` and ```Interface.py```.
3. Second is ```Globals.py```. This file contains all common global variables and initializer for numerical methods. Dependent from ```Methods.py```.
4. Next is ```InterfaceClasses.py```. This file contains all useful classes and functions for GUI. The main class is ```GUIObjext```. Dependent from *tkinter* library.
5. ```Interface.py``` is dependent from ```Interfacelasses.py```, ```Globals.py``` and other files. It contains function that fills UI window and initializer of GUI.
6. ```Methods.py``` contains functions of all supported numerical methods. Independent.
7. ```Function.py``` contains initializer of IVP, functions of analytical solution for ```y' = 4x - 2y``` and its first derivative. Dependent from ```Globals.py``` and *math* library.
8. ```Kernel.py``` is evaluated when user presses button ```Plot```. This file proceeds every numerical method and obtains analytical and numerical solutions for given initial conditions. Dependent from ```Globals.py```, ```Function.py``` and ```Plotter.py```.
9. ```Plotter.py```is dependent from *plotly* library. Contains the main plotting function.
10. And the last one, ```Extencions.py```. Independent, contains some additional functions that are not related to subjects of other files.
