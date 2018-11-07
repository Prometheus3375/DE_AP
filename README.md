# SimplePlotter App
## Requirements
1. Download and install [Python 3.7.1](https://www.python.org/downloads/).
2. After successful installation, open command prompt, type ```pip install plotly``` and press Enter. This will download and install PlotLy library.
3. After installation is finished, double-click Main.py to launch the application.
## Usage
1. For now, the application is able to plot analytical and numerical solutions of ```y' = 4x - 2y```, absolute global truncation error for every numerical method and dependence of their errors from the number of steps.
2. The application supports Euler, Improved Euler, and Runge-Kutta methods. Application plots them on one sheet, you can hide uninterested methods by clicking on its label in the plot legend.
3. All made plots are saved in ```<app_directory>/plots``` directory.
4. Do not mark ```Plots of function for every N``` and ```Plots of absolute errors for every N``` for large ranges of step values.
## Options
1. *x0* and *y0* – to solve the initial value problem it is necessary to specify initial conditions. In addition, *x0* specifies left bound of plotting. Both *x0* and *y0* must be real numbers. Do not use big *x0* values to avoid overflow.
2. *X* – specifies the right bound of plotting. Must be a real number and greater than *x0*.
3. *Number of steps* – this section allows choosing between 2 different modes: *Single value* and *Range of values*.
4. *Single value* – specifies the number of steps and makes a plot of function for given *N* and initial conditions. By default, the plot opens automatically, but it is possible to toggle this feature. There is an option for plotting absolute errors of numerical methods on each step. *N* must be a positive integer.
5. *Range of values* – specifies a range of step values by taking left and right bounds and plots dependence of maximum absolute error for every number of steps. Both bounds must be positive integers and right bound must be greater than left one. It’s also possible to make plots of function and absolute errors for every *N*, but these options are not recommended for large ranges.
## Code
1. The code is divided into several parts.
2. First is ```Main.py```. The main executable file, it initializes necessary data and interface. It is dependent on```Globals.py``` and ```Interface.py```.
3. Second is ```Globals.py```. This file contains all common global variables and initializer for numerical methods (```InitData()```). It is dependent on ```Methods.py```.
4. Next is ```InterfaceClasses.py```. This file contains all useful classes and functions for GUI. The main class is ```GUIObjext```. It is dependent on ***tkinter*** library.
5. ```Interface.py``` is dependent on```Interfacelasses.py```, ```Globals.py``` and other files. It contains a function that fills UI window, a function that checks entered values and initializer for the interface (```InitInterface()```).
6. ```Methods.py``` contains functions of all supported numerical methods. Independent.
7. ```Function.py``` contains initializer of IVP, functions of the analytical solution for ```y' = 4x - 2y``` and its first derivative. It is dependent on```Globals.py``` and ***math*** library.
8. ```Kernel.py``` is evaluated when a user presses button ```Plot```. This file proceeds every numerical method and obtains analytical and numerical solutions for given initial conditions. The main function is ```Execute(...)``` It is dependent on ```Globals.py```, ```Function.py``` and ```Plotter.py```.
9. ```Plotter.py``` is dependent on ***plotly*** library. Contains the main plotting function.
10. And the last one, ```Extencions.py```. Independent, it contains some additional functions that are not related to subjects of other files.
