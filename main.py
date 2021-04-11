from IsingModel3d import IsingModel3d
import random


def main():
    model = IsingModel3d(10, 10, 10, lambda x, y, z: random.randint(0, 1))
    model.animation()


if __name__ == "__main__":
    main()
