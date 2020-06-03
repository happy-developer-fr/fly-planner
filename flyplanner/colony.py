import random
from typing import List

from flyplanner import logger


class Fly:
    def __init__(self, initial_energy: float):
        self.initial_energy = initial_energy
        self.remaining_energy = initial_energy
        self.alive = True

    def energy_remaining(self) -> float:
        return self.remaining_energy

    def missing_energy(self) -> float:
        return self.initial_energy - self.remaining_energy

    def consume_energy(self, energy_consumed):
        self.remaining_energy -= energy_consumed
        if self.energy_remaining() <= 0:
            self.die()

    def feed(self, max_energy) -> float:
        energy_consumed = 0
        if max_energy > 0:
            energy_consumed = min(max_energy, self.missing_energy())
            self.remaining_energy += energy_consumed
        return energy_consumed

    def die(self):
        logger.log_fly_died()
        self.alive = False

    def creation_energy_price(self) -> float:
        return self.initial_energy

    @staticmethod
    def random_fly():
        return Fly(random.choice([1.0, 5.0, 10.0]))


class Colony:
    def __init__(self, flies: List[Fly], food_initial_energy: float):
        self.flies = flies
        self.energy_remaining = food_initial_energy
        self.days_alive = 0
        self.died = 0
        self.born = 0
        self.left = 0

    def create_fly(self):
        new_fly = Fly.random_fly()
        # TODO raise error
        if not self.energy_remaining < new_fly.creation_energy_price():
            self.flies.append(new_fly)
            self.energy_remaining = max(
                0.0, self.energy_remaining - new_fly.creation_energy_price()
            )
            self.born += 1
            logger.log_fly_is_born()

    def feed_flies(self) -> None:
        for fly in self.flies:
            if self.energy_remaining > 0:
                energy_consumed = fly.feed(self.energy_remaining)
                self.energy_remaining -= energy_consumed

    def leave(self) -> List[Fly]:
        flies_left = [
            self.flies.pop()
            for i in range(min(len(self.flies), random.randint(0, 5)))
        ]
        self.left += len(flies_left)
        logger.log_fly_left(len(flies_left))
        return flies_left

    def is_active(self) -> bool:
        return len(self.flies_alive()) > 0 or self.energy_remaining > 0

    def flies_alive(self) -> List[Fly]:
        return [f for f in self.flies if f.alive]

    def dead_flies(self) -> List[Fly]:
        return [f for f in self.flies if not f.alive]

    def new_day(self) -> None:
        self.days_alive += 1
        if self.is_active():
            self.leave()
            [fly.consume_energy(1) for fly in self.flies_alive()]
            self.feed_flies()
            if self.energy_remaining > 0:
                self.create_fly()
            self.died += len(self.dead_flies())
            self.flies = self.flies_alive()


class Colonnies:
    def __init__(self, colonies: List[Colony]):
        self.colonies = colonies

    def new_day(self):
        self.colonies = [colony.new_day() for colony in self.colonies]

    def pop_new_colony(self):
        self.colonies.append(
            Colony(flies=[], food_initial_energy=random.randint(100, 3000))
        )
