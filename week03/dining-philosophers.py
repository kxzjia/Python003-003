import threading


class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        first = philosopher
        second = philosopher + 1 if philosopher < 4 else 0

        if philosopher & 1:
            first, second = second, first

        with self.forks[first], self.forks[second]:
            pickLeftFork()
            pickRightFork()
            eat()
            putRightFork()
            putLeftFork()