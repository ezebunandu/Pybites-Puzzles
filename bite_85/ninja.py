scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        belt = max(key for key in BELTS.keys() if new_score >= key)
        return BELTS.get(belt)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError("Score takes an int")

        if new_score < self._score:
            raise ValueError("Cannot lower score")

        self._score = new_score

        the_belt = self._get_belt(new_score)

        if self._last_earned_belt != the_belt:
            self._last_earned_belt = the_belt
            print(f"Congrats, you earned {self._score} points obtaining the PyBites Ninja {self._last_earned_belt.capitalize()} Belt")
        else:
            print(f"Set new score to {self._score}")

if __name__ == "__main__":
    ninja = NinjaBelt(score=0)
    print(ninja.score)
    ninja.score = 50


