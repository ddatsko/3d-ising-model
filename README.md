# Ising model Python implementation with visualization

# Usage
To use the code you need **Python 3.9+** \
To install the requirements just run
``` pip install -r requirements.txt ``` \
To run visualization just run the IsingModel3d ```run_simulation``` method. This way no graphs are created, you can just see the visualization. \
The model is updated in runtime and you can rotate and move the camera \
Example of the visualization:
![Peek 2021-04-26 01-26](https://user-images.githubusercontent.com/35429810/116011574-72395b00-a62e-11eb-847b-26cf5034d64c.gif)




# Structure
There are 2 classes in the code: IsingModel and IsingModel3d. The latter inherits IsingModel and implements additional visualization

# Implementation
The model is implemented without any libraries that can improve the performance (like NumPy) \
Visualization is done with **pyqtgraph** Python library

# Examples of usage
### Magnetism after each simulation step on temperature 4
![temp_4_magnetism_progression](https://user-images.githubusercontent.com/35429810/116011661-c7756c80-a62e-11eb-8ade-4fb9ec86cad5.png)
### Dots representing temperature and final magnetism after 1000 simulation iterations:
![final_magnetism_each_simulation](https://user-images.githubusercontent.com/35429810/116011694-e7a52b80-a62e-11eb-9434-77911213aedb.png)
