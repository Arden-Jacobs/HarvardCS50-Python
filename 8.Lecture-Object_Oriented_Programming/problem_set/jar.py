class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        msg = "🍪" * self.size
        return f"{msg}"

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError
        self._size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(6)
    jar.deposit(6)
    jar.withdraw(10)
    print(jar)


if __name__ == "__main__":
    main()
