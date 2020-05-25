from flyplanner.colony import Colony


def main():
    initial_energy = 30_000
    colony = Colony([], initial_energy)
    while colony.is_active():
        colony.new_day()
    print(f"A colony live {colony.days_alive} days with {initial_energy} energy")
    print(
        f"{colony.left} leaved, {colony.born} born and {colony.died} flies died during colony life"
    )


if __name__ == "__main__":
    main()
