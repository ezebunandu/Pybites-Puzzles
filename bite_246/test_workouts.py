import pytest

from workouts import print_workout_days


def test_empty_input():
    with pytest.raises(TypeError):
        print_workout_days()

@pytest.mark.parametrize("input, expected", [
    ('nonsense', 'No matching workout'),
    ('30 min cardio -', 'No matching workout'),
    ("body", "Mon, Tue, Thu, Fri"), 
    ("cardio", 'Wed')
    ])

def test_print_workout_days(capfd, input, expected):
    print_workout_days(input)
    captured = capfd.readouterr()[0].strip()
    assert captured == expected