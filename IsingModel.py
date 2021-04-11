class IsingModel:
    def __init__(self, x_size: int, y_size: int, z_size: int,
                 initializer: callable((int, int, int)) = lambda x, y, z: 1):
        self.particles = [[[initializer(x, y, z) for z in range(z_size)] for y in range(y_size)] for x in range(x_size)]
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size

    @classmethod
    def from_file(cls, filename: str) -> 'IsingModel':
        with open(filename, 'r') as file:
            x, y, z = list(map(int, file.readline().split()))
            model = IsingModel(x, y, z)
            for i in range(x):
                for j in range(y):
                    spins = list(map(int, file.readline().split()))
                    for k in range(z):
                        model[i, j, k] = spins[k]
            return model

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
        print(x, y, z)
        return self.particles[x][y][z]

    def __setitem__(self, key: tuple[int, int, int] or int, value: 1 or 0):
        if isinstance(key, int):
            x, y, z = self._n_index_to_xyz(key)
        else:
            x, y, z = key
        self.particles[x][y][z] = value
