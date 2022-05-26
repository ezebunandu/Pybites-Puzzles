from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple("State", "color command timeout")


def traffic_light():
    """Returns an itertools.cycle iterator that
    when iterated over returns State namedtuples
    as shown in the Bite's description"""
    stop = State("red", "Stop", 2)
    start = State("green", "Go", 2)
    caution = State("amber", "Caution", 0.5)
    states = [stop, start, caution]
    return cycle(states)


if __name__ == "__main__":
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f"{state.command}! The light is {state.color}")
        sleep(state.timeout)
