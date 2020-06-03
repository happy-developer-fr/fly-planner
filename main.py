import random
import time

from flyplanner.colony import Colony
from fluent import sender

sender.setup(
    "flyplanner", host="localhost", port=24224, nanosecond_precision=False
)


def main():
    initial_energy = 30_000
    colony = Colony([], initial_energy)
    while colony.is_active():
        time.sleep(random.uniform(0.001, 0.01))
        colony.new_day()
    print(
        f"A colony live {colony.days_alive} days with {initial_energy} energy"
    )
    print(
        f"{colony.left} leaved, {colony.born} born and {colony.died} flies died during colony life"
    )
    sender.close()


if __name__ == "__main__":
    main()
