class CPA_int:
    def __init__(self, init_n):
        self.n = init_n

    def __add__(self, other):
        return CPA_int(self.n + other.n)