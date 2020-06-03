from fluent import event


def log_fly_is_born() -> None:
    text = "a_fly_is_born"
    event.Event(label=text, data={})


def log_fly_died() -> None:
    text = "fly_died"
    event.Event(label=text, data={})


def log_fly_left(flies: int) -> None:
    text = "fly_left"
    [event.Event(label=text, data={}) for fly in range(flies)]
