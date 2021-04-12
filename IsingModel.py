import random
import math


class IsingModel:
    def __init__(self, x_size: int, y_size: int, z_size: int, temperature: int, interaction: float,
                 initializer: callable((int, int, int)) = lambda x, y, z: 1):
        self.particles = [[[initializer(x, y, z) for z in range(z_size)] for y in range(y_size)] for x in range(x_size)]
        self.temperature = temperature
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size
        self.n = self.x_size * self.y_size * self.z_size
        self.j = interaction

    @classmethod
    def from_file(cls, filename: str) -> 'IsingModel':
        with open(filename, 'r') as file:
            x, y, z, temperature, interaction = list(map(int, file.readline().split()))
            model = IsingModel(x, y, z, temperature, interaction)
            for i in range(x):
                for j in range(y):
                    spins = list(map(int, file.readline().split()))
                    for k in range(z):
                        model[i, j, k] = spins[k]
            return model

    def get_magnetism(self) -> int:
        res = 0
        for i in range(self.n):
            res += self[i]
        return res


    def get_s(self, x: int, y: int, z: int):
        res = 0
        current = self.particles[x][y][z]
        for i in (-1, 1):
            for j in (-1, 1):
                for k in (-1, 1):
                    res += 1 if current == self.particles[x + i][y + j][z + k] else -1
        return -res * self.j


    def calculate_h(self, x: int, y: int, z: int):
        current = self.particles[x][y][z]
        res = 0
        for i in (-1, 1):
            for j in (-1, 1):
                for k in (-1, 1):
                    if self.particles[(x + i) % self.x_size][(y + j) % self.y_size][(z + k) % self.z_size] == current:
                        res += 1
                    else:
                        res -= 1
        return -self.j * res


    def make_simulation_step(self):
        for _ in range(self.n):
            x = random.randint(0, self.x_size - 1)
            y = random.randint(0, self.y_size - 1)
            z = random.randint(0, self.z_size - 1)
            h_old = self.calculate_h(x, y, z)
            h_new = -h_old
            delta_h = h_new - h_old
            if delta_h < 0:
                self.particles[x][y][z] *= -1
            else:
                prob = math.exp(-self.temperature * delta_h)
                if random.random() < prob:
                    self.particles[x][y][z] *= -1



    def _n_index_to_xyz(self, key: int) -> (int, int, int):
        x = key // (self.y_size * self.z_size)
        key %= self.y_size * self.z_size
        y = key // self.z_size
        z = key % self.z_size
        return x, y, z

    def __getitem__(self, key: tuple[int, int, int] or int):
        if isinstance(key, int):
            x, y, z = self._n_index_to_xyz(key)
        else:
            x, y, z = key
        return self.particles[x][y][z]

    def __setitem__(self, key: tuple[int, int, int] or int, value: 1 or -1):
        if isinstance(key, int):
            x, y, z = self._n_index_to_xyz(key)
        else:
            x, y, z = key
        self.particles[x][y][z] = value
