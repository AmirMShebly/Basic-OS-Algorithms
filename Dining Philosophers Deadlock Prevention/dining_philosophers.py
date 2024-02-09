import threading
import time

num_philosophers = 5
# max_eat_count = 3


class Philosopher:
    def __init__(self, name, left_fork, right_fork):
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.eat_count = 0

    def think(self):
        print(f"{self.name} is thinking.\n")
        time.sleep(2)

    def eat(self):
        print(f"{self.name} is eating.\n")
        time.sleep(2)
        self.eat_count += 1

    def dine(self):
        while True:  #self.eat_count < max_eat_count:
            self.think()
            self.pick_forks()
            self.eat()
            self.put_forks()

    def pick_forks(self):
        print(f"{self.name} is trying to pick up forks.\n")

        if self.left_fork.acquire(blocking=False):
            print(f"{self.name} picked up the left fork.\n")
            if self.right_fork.acquire(blocking=False):
                print(f"{self.name} picked up the right fork.\n")
            else:
                print(f"{self.name} couldn't pick the right fork")
                self.left_fork.release()
                print(f"{self.name} is releasing the right fork")

        else:
            print(f"{self.name} couldn't pick the left fork")
            self.left_fork.release()
            print(f"{self.name} is releasing the left fork")

    def put_forks(self):
        print(f"{self.name} is putting down forks.\n")
        self.left_fork.release()
        self.right_fork.release()


def main():
    forks = [threading.Semaphore(1) for _ in range(num_philosophers)]
    philosophers = []

    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]
        philosopher = Philosopher(f"Philosopher {i + 1}", left_fork, right_fork)
        philosophers.append(philosopher)

    philosopher_threads = [threading.Thread(target=philosopher.dine) for philosopher in philosophers]

    for thread in philosopher_threads:
        thread.start()

    for thread in philosopher_threads:
        thread.join()


if __name__ == "__main__":
    main()

