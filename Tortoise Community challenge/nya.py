import itertools


class Cat:
    new_id = itertools.count()

    def __init__(self, name: str):
        self.name = name
        self.is_racing = False
        self._food = 500
        self._agility = 5
        self._speed = 0.0
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
    def id(self):
        return self._id

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
        self.accelerate()
        if self.food == 0:
            self.hit_the_brakes()
        else:
            self.food -= 1


class NyaRace:
    def __init__(self, race_length: int):
        self._race_length = race_length
        self._kitty_participants = set()
        self._race_started = False
        self._kitty_distances = []
        self._kitty_speeds = {}
        self._race_ended = False

    def add_kitty_participant(self, kitty: Cat):
        if not kitty.is_racing:
            self._kitty_participants.add(kitty)

    def step(self):
        if not self._race_ended:
            if not self._race_started:
                for kitty in self._kitty_participants:
                    kitty.is_racing = True
                self._race_started = True

            if len(self._kitty_distances) == 0:
                for kitty in self._kitty_participants:
                    self._kitty_distances.append([kitty, 0, kitty.id])
                    self._kitty_speeds[kitty.name + str(kitty.id)] = 0

            for kitty in self._kitty_participants:
                kitty.step()
                self._kitty_speeds[kitty.name + str(kitty.id)] = kitty.speed
                for kitty_distance in self._kitty_distances:
                    if kitty_distance[0] == kitty:
                        kitty_distance[1] += kitty.speed

            self._kitty_distances = sorted(self._kitty_distances, key=lambda distance: (distance[1], distance[2]))

            if (self._kitty_distances[len(self._kitty_participants) - 1][1] >= self._race_length or
                    sum(self._kitty_speeds.values()) == 0):
                self._race_ended = True

            yield[kitty[0] for kitty in self._kitty_distances]
        else:
            pass
