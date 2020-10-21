""""
Complete things marked with TODO (and only those, no need to touch other things).
Each todo is marked if it's for basic or intermediate.
You do not have to solve all TODOs to pass, but each solved adds you points.
"""


class Cat:
    def __init__(self, name: str):
        self.name = name
        self._food = 500
        self._agility = 5
        self._speed = 0.0
        self.is_racing = False
        # TODO for intermediate:
        # Each time a cat is created increase this id by 1
        # (first id can be whatever number you want as long as ids are in +1 ascending order)
        self._id = 0

    def __hash__(self):
        return hash(self._id)

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, food):
        """TODO for basic:
        Complete this setter. Food should not be less than 0 or more than 1000
        (if it's less/more than that then set it to min/max allowed value)"""
        pass

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        """TODO for basic:
        Complete this setter. Agility should not be less than 1 or more than 10
        (if it's less/more than that then set it to min/max allowed value)"""
        pass

    @property
    def speed(self):
        """Speed is a integer representing m/s"""
        return self._speed

    @speed.setter
    def speed(self, speed):
        """TODO for basic:
        Complete this setter. Speed should not be less than 0 or more than maximum_speed
        (if it's less/more than that then set it to min/max allowed value)"""
        pass

    @property
    def maximum_speed(self) -> float:
        return 1 + int(self.food / 70)

    @property
    def acceleration(self) -> float:
        return 1 + round(self.agility / 2, 1)

    def eat(self):
        """TODO for basic:
        Increases food by 450, decreases agility by 3"""
        pass

    def nap(self):
        """TODO for basic:
        Decreases food to 50, increases 1 point of agility for each 100 points of food decreased.
        Method should do nothing if food is already less than 50."""
        pass

    def train(self):
        """TODO for basic:
        Decrease food by 250, increase agility by 2, method should do nothing if food is already less than 250"""
        pass

    def accelerate(self):
        self.speed += self.acceleration

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

    def add_kitty_participant(self, kitty: Cat):
        """TODO for basic:
        Add kitten to _kitty_participants, but do not add it if kitten is already racing."""
        pass

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