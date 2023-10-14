import unittest
import warnings
import sys

sys.path.append("../")
from Code.prediction_scripts.item_based import recommendForNewUser

warnings.filterwarnings("ignore")


class Tests(unittest.TestCase):
    def testToyStory(self):
        ts = [
            {"title": "Toy Story (1995)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(
            "Adventures of Rocky and Bullwinkle, The (2000)" in recommendations
        )

    def testHorrorWithCartoon(self):
        ts = [
            {"title": "Strangers, The (2008)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Bats (1999)" in recommendations) == False)

    def testIronMan(self):
        ts = [
            {"title": "Iron Man (2008)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Thor: Ragnarok (2017)" in recommendations))

    def testRoboCop(self):
        ts = [
            {"title": "RoboCop (1987)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(
            ("Boondock Saints II: All Saints Day, The (2009)" in recommendations)
        )

    def testNolan(self):
        ts = [
            {"title": "Inception (2010)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Watchmen (2009)" in recommendations))

    def testDC(self):
        ts = [
            {"title": "Man of Steel (2013)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(
            ("Man of Steel (2013)" in recommendations)
        )

    def testArmageddon(self):
        ts = [
            {"title": "Armageddon (1998)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Saint, The (1997)" in recommendations))

    def testLethalWeapon(self):
        ts = [
            {"title": "Lethal Weapon (1987)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Lethal Weapon 2 (1989)" in recommendations))

    def testDarkAction(self):
        ts = [
            {"title": "Batman: The Killing Joke (2016)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(
            ("Branded to Kill (Koroshi no rakuin) (1967)" in recommendations)
        )

    def testDark(self):
        ts = [
            {"title": "Puppet Master (1989)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Apollo 18 (2011)" in recommendations))

    def testHorrorComedy(self):
        ts = [
            {"title": "Scary Movie (2000)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Attack of the Killer Tomatoes! (1978)" in recommendations))

    def testSuperHeroes(self):
        ts = [
            {"title": "Spider-Man (2002)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Terminator Genisys (2015)" in recommendations))

    def testCartoon(self):
        ts = [
            {"title": "Moana (2016)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Monsters, Inc. (2001)" in recommendations))

    def testMultipleMovies(self):
        ts = [
            {"title": "Iron Man (2008)", "rating": 5.0},
            {"title": "Avengers: Age of Ultron (2015)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(ts)
        self.assertTrue(("Justice League (2017)" in recommendations))


if __name__ == "__main__":
    unittest.main()
