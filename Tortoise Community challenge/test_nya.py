"""
Note for running tests:
Be sure that you have named the qualifier script that you got in our
paste as 'nya.py', without the quotes (as this is what we import if you look below at imports).

You can name this test script as 'test_nya.py', without the quotes.

Put both the qualifier script and this test script in the same folder, let's call the folder as 'qualifier'
without the quotes.

You can run these tests either in terminal with this command (after you CD to /qualifier):
python -m unittest discover

or you can just run this script directly.
"""
import nya
import unittest
import pdb

class BasicTestCases(unittest.TestCase):
    # represents what acceleration kitty should have for each state of agility
    agility_acceleration_pairs = (
        (1, 1.5), (2, 2.0), (3, 2.5), (4, 3.0), (5, 3.5), (6, 4.0), (7, 4.5), (8, 5.0), (9, 5.5), (10, 6.0)
    )

    def test_cat_default_values(self):
        # cat default values should not be altered from their original state.
        kitty = nya.Cat("desperado")
        self.assertEqual(500, kitty.food)
        self.assertEqual(5, kitty.agility)
        self.assertEqual(0, kitty.speed)

    def test_food_getter(self):
        # food getter should not be altered from it's original state.
        kitty = nya.Cat("desperado")

        kitty._food = 500
        self.assertEqual(500, kitty.food)
        kitty._food = -300
        self.assertEqual(-300, kitty.food)

    def test_food_range(self):
        kitty = nya.Cat("desperado")

        kitty.food = -1
        self.assertEqual(0, kitty.food)

        kitty.food = 1001
        self.assertEqual(1000, kitty.food)

    def test_agility_getter(self):
        # agility getter should not be altered from it's original state.
        kitty = nya.Cat("desperado")

        kitty._agility = 500
        self.assertEqual(500, kitty.agility)
        kitty._agility = -300
        self.assertEqual(-300, kitty.agility)

    def test_agility_range(self):
        kitty = nya.Cat("desperado")

        kitty.agility = -1
        self.assertEqual(1, kitty.agility)

        kitty.agility = 11
        self.assertEqual(10, kitty.agility)

    def test_speed_getter(self):
        # speed getter should not be altered from it's original state.
        kitty = nya.Cat("desperado")

        kitty._speed = 500
        self.assertEqual(500, kitty.speed)
        kitty._speed = -300
        self.assertEqual(-300, kitty.speed)

    def test_speed_range(self):
        kitty = nya.Cat("desperado")

        for food in range(0, 100, 5):
            kitty.food = food
            kitty.speed = 1000
            self.assertEqual(kitty.maximum_speed, kitty.speed)

        kitty.speed = -1
        self.assertEqual(0, kitty.speed)

    def test_maximum_speed(self):
        # maximum speed method should not be altered from it's original state.
        food_max_speed_pairs = (
            (0, 1), (50, 1), (100, 2), (150, 3), (200, 3), (250, 4), (300, 5), (350, 6), (400, 6), (450, 7), (500, 8),
            (550, 8), (600, 9), (650, 10), (700, 11), (750, 11), (800, 12), (850, 13), (900, 13), (950, 14), (1000, 15)
        )

        kitty = nya.Cat("desperado")

        for food, expected_max_speed in food_max_speed_pairs:
            kitty.food = food
            self.assertEqual(expected_max_speed, kitty.maximum_speed)

    def test_acceleration(self):
        # acceleration method should not be altered from it's original state.
        kitty = nya.Cat("desperado")

        for agility, expected_acceleration in self.agility_acceleration_pairs:
            kitty.agility = agility
            self.assertEqual(expected_acceleration, kitty.acceleration)

    def test_eat(self):
        kitty = nya.Cat("desperado")
        kitty.food = 0
        kitty.agility = 10
        expected_food_agility_pairs = ((450, 7), (900, 4), (1000, 1), (1000, 1))

        for expected_food, expected_agility in expected_food_agility_pairs:
            kitty.eat()
            self.assertEqual(expected_food, kitty.food)
            self.assertEqual(expected_agility, kitty.agility)

    def test_nap(self):
        kitty = nya.Cat("desperado")
        food_expected_agility_pairs = (
            (90, 1), (100, 1), (120, 1), (150, 2), (200, 2), (250, 3), (270, 3), (300, 3),
            (330, 3), (350, 4), (400, 4), (450, 5), (500, 5), (550, 6), (600, 6), (1000, 10)
        )
        for food, expected_agility in food_expected_agility_pairs:
            kitty.agility = 1
            kitty.food = food
            kitty.nap()
            self.assertEqual(expected_agility, kitty.agility)
            self.assertEqual(50, kitty.food)

        # Nap should be ignored (aka it will not nap) if food is less than 50
        lower_food_expected_agility_pairs = ((0, 1), (10, 1), (20, 1), (30, 1), (40, 1))
        for food, expected_agility in lower_food_expected_agility_pairs:
            kitty.agility = 1
            kitty.food = food
            kitty.nap()
            self.assertEqual(expected_agility, kitty.agility)
            self.assertEqual(food, kitty.food)

    def test_train(self):
        kitty = nya.Cat("desperado")
        food_expected_agility_pairs = (
            (0, 1), (100, 1), (200, 1), (250, 3), (300, 3), (1000, 3)
        )
        for food, expected_agility in food_expected_agility_pairs:
            kitty.agility = 1
            kitty.food = food
            kitty.train()
            self.assertEqual(expected_agility, kitty.agility)

    def test_accelerate(self):
        # acceleration method should not be altered from it's original state.
        kitty = nya.Cat("desperado")
        for agility, expected_acceleration in self.agility_acceleration_pairs:
            kitty.speed = 0
            kitty.agility = agility
            kitty.accelerate()
            self.assertEqual(expected_acceleration, kitty.speed)

        kitty.speed = 0
        for agility, acceleration in self.agility_acceleration_pairs:
            kitty.agility = agility
            speed_before = kitty.speed
            kitty.accelerate()
            self.assertLessEqual(kitty.speed, kitty.maximum_speed)
            if kitty.speed < kitty.maximum_speed:
                self.assertEqual(speed_before + acceleration, kitty.speed)

    def test_hit_the_brakes(self):
        # hit_the_brakes method should not be altered from it's original state.
        kitty = nya.Cat("desperado")
        kitty.food = 100
        kitty.speed = kitty.maximum_speed
        kitty.hit_the_brakes()
        self.assertEqual(0, kitty.speed)

    def test_cat_step(self):
        # cat step  method should not be altered from it's original state.
        kitty_recreate = nya.Cat("recreate")
        kitty_original = nya.Cat("original")

        for _ in range(5):
            # lazy copy paste
            kitty_recreate.accelerate()
            if kitty_recreate.food == 0:
                kitty_recreate.hit_the_brakes()
            else:
                kitty_recreate.food -= 1

            kitty_original.step()
            self.assertEqual(kitty_recreate.speed, kitty_original.speed)
            self.assertEqual(kitty_recreate.food, kitty_original.food)

    def test_adding_kitty_participants_to_race(self):
        kitty_one = nya.Cat("desperado")
        kitty_two = nya.Cat("el niño")
        kitty_three = nya.Cat("catnip")
        kitty_four = nya.Cat("desperado")

        race = nya.NyaRace(500)
        race.add_kitty_participant(kitty_one)
        race.add_kitty_participant(kitty_two)
        race.add_kitty_participant(kitty_three)
        race.add_kitty_participant(kitty_four)
        self.assertEqual(4, len(race._kitty_participants))

        # Can't add kitties that are already racing
        kitty_racing = nya.Cat("already racing")
        kitty_racing.is_racing = True
        race.add_kitty_participant(kitty_racing)
        self.assertEqual(4, len(race._kitty_participants))


class IntermediateTestCases(unittest.TestCase):
    def test_cat_hash(self):
        # cat hash dunder should not be altered from it's original state.
        cat_ids = (0, 1, 2, 33, 77, 2000)
        cat_test = nya.Cat("test")
        for cat_id in cat_ids:
            cat_test._id = cat_id
            self.assertEqual(hash(cat_test), hash(cat_id))

    def test_race_participant_type(self):
        # race _kitty_participants should not be altered from it's original type.
        race_test = nya.NyaRace(500)
        self.assertEqual(type(race_test._kitty_participants), set)

    def test_cat_ids(self):
        kitties = [nya.Cat("desperado"), nya.Cat("el niño"), nya.Cat("catnip"), nya.Cat("desperado")]

        # IDs should be unique
        ids = [kitty._id for kitty in kitties]
        self.assertEqual(len(ids), len(set(ids)))

        # IDs should be in +1 ascending order
        for previous, current in zip(ids, ids[1:]):
            self.assertEqual(current - previous, 1)

    def test_cat_race(self):
        kitty_one = nya.Cat("desperado")
        kitty_one.food = 750
        kitty_one.agility = 5

        kitty_two = nya.Cat("el niño")
        kitty_two.food = 500
        kitty_two.agility = 10

        kitty_three = nya.Cat("catnip")
        kitty_three.food = 800
        kitty_three.agility = 4

        kitty_four = nya.Cat("hotail")
        kitty_four.food = 1000
        kitty_four.agility = 3

        race = nya.NyaRace(100)
        race.add_kitty_participant(kitty_one)
        race.add_kitty_participant(kitty_two)
        race.add_kitty_participant(kitty_three)
        race.add_kitty_participant(kitty_four)

        expected_results = (
            [kitty_four, kitty_three, kitty_one, kitty_two, ],
            [kitty_four, kitty_three, kitty_one, kitty_two, ],
            [kitty_four, kitty_three, kitty_one, kitty_two, ],
            [kitty_four, kitty_two, kitty_three, kitty_one, ],
            [kitty_four, kitty_two, kitty_three, kitty_one, ],
            [kitty_two, kitty_four, kitty_one, kitty_three, ],
            [kitty_two, kitty_one, kitty_three, kitty_four, ],
            [kitty_two, kitty_one, kitty_three, kitty_four, ],
            [kitty_two, kitty_one, kitty_three, kitty_four, ],
            [kitty_two, kitty_one, kitty_three, kitty_four, ],
        )

        for expected_state, race_state in zip(expected_results, race.step()):
            self.assertEqual(expected_state, race_state)

test = BasicTestCases()
test.test_accelerate()