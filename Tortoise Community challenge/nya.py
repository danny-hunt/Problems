""""
Complete things marked with TODO (and only those, no need to touch other things).
Each todo is marked if it's for basic or intermediate.
You do not have to solve all TODOs to pass, but each solved adds you points.
"""
import itertools

class Cat:
    new_id = itertools.count()
    def __init__(self, name: str):
        self.name = name
        self._food = 500
        self._agility = 5
        self._speed = 0.0
        self.is_racing = False
        # TODO for intermediate:
        # Each time a cat is created increase this id by 1
        # (first id can be whatever number you want as long as ids are in +1 ascending order)
        self._id = next(self.new_id)

    def __hash__(self):
        return hash(self._id)

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, food):
        if food < 0:
            food = 0
        elif food > 1000:
            food = 1000
        self._food = food

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        if agility < 1:
            agility = 1
        elif agility > 10:
            agility = 10
        self._agility = agility

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < 0:
            self._speed = 0
        elif speed > self.maximum_speed:
            self._speed = self.maximum_speed
        else:
            self._speed = speed

    @property
    def maximum_speed(self) -> float:
        return 1 + int(self.food / 70)

    @property
    def acceleration(self) -> float:
        return 1 + round(self.agility / 2, 1)

    def eat(self):
        self.food = self.food + 450
        self.agility = self.agility - 3

    def nap(self):
        if self.food >= 50:
            self.agility = self.agility + (self.food - 50) // 100
            self.food = 50

    def train(self):
        if self.food >= 250:
            self.food = self.food - 250
            self.agility = self.agility + 2

    def accelerate(self):
        self.speed = self.acceleration + self.speed

    def hit_the_brakes(self):
        self.speed = 0

    def step(self):
        """Think of this as one second of time in race track."""
        self.accelerate()
        if self.food == 0:
            self.hit_the_brakes()
        else:
            self.food -= 1


class NyaRace:
    def __init__(self, race_length: int):
        """
        Class that deals with kitty racing.
        :param race_length: integer, length of race track in meters.
        """
        self._race_length = race_length
        self._kitty_participants = set()
        self._race_started = False
        self._kitty_id = 0

    def add_kitty_participant(self, kitty: Cat):
        if not kitty.is_racing:
            self._kitty_participants.add(kitty)
            kitty.is_racing = True

    def step(self):

        """
        TODO for intermediate:
        Implement step feature. Think of step as one second of time.
        - First step also marks the race as started and sets all kitties racing status to True.
        - Keep track of each kitty passed distance so you can know which kitty is in which place
          (you need to implement this yourself, do it however you see fit as long as this method yields the
          correct results).
        - Each race step should call each kitty step method (which deals with acceleration and food consumption).
        - Each time this is called each kitty should pass some distance depending on its current speed (be sure to call
          kitty step first as stated in above note)
        - This should be a generator that each time yields a list of kittens ordered from last to first place, first
          list index representing the last place and last list index representing the first place in race.
          (if 2 or more kittens are in the same place then they should be ordered by cat id)
        - Last yield is as soon as any kitten passes the finish line (or if all have stopped).
        """
        pass