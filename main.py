from IsingModel3d import IsingModel3d
import random


def main():
    model = IsingModel3d(10, 10, 10, 0.3, 1, lambda x, y, z: 1)
    #model.animation()
    model.run_simulation(1000, visualize=True)


if __name__ == "__main__":
    main()
