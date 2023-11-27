import unittest
import warnings
import sys

sys.path.append("../")
from Code.recommenderapp.app import rcmd

warnings.filterwarnings("ignore")


class Tests(unittest.TestCase):
    def testToyStory(self):
        ts = "Toy story"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(
                movie == "cars"
                for movie in recommendations
            )
        )

    def testCamelCase(self):
        ts = "Toy Story"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(
                movie == "cars"
                for movie in recommendations
            )
        )

    def testLoweCase(self):
        ts = "toy story"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(
                movie == "cars"
                for movie in recommendations
            )
        )

    def testUpperCase(self):
        ts = "TOY STORY"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(
                movie == "cars"
                for movie in recommendations
            )
        )

    def testRoboCop(self):
        ts = "RoboCop"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(
                movie == "elite squad"
                for movie in recommendations
            )
        )

    def testBatmanPos(self):
        ts = "Batman"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(
                movie == "batman returns"
                for movie in recommendations
            )
        )   

    def testBatmanNeg(self):
        ts = "Batman"
        recommendations = rcmd(ts)
        self.assertFalse(
            any(
                movie == "avengers"
                for movie in recommendations
            )
        )  
    
    def testPrisonersPos(self):
        ts = "Prisoners"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(
                movie == "zodiac"
                for movie in recommendations
            )
        )

    def testPrisonersNeg(self):
        ts = "Prisoners"
        recommendations = rcmd(ts)
        self.assertFalse(
            any(
                movie == "barbie"
                for movie in recommendations
            )
        )

    def testNolan(self):
        ts = "Inception"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(movie == "the revenant" for movie in recommendations)
        )

    def testDC(self):
        ts = "Man of Steel"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(movie == "justice league" for movie in recommendations)
        )

    def testArmageddon(self):
        ts = "Armageddon"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(movie == "transformers" for movie in recommendations)
        )

    def testHorror(self):
        ts = "The nun"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(movie == "the conjuring" for movie in recommendations)
        )

    def testAnime(self):
        ts = "Finding Nemo"
        recommendations = rcmd(ts)
        self.assertTrue(
            any(movie == "ice age" for movie in recommendations)
        )

    #Testing if the input string is empty, the code should handle this scenario as well
    def testEmptyInput(self):
        ts = ""
        recommendations = rcmd(ts)
        self.assertEqual(recommendations, "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies")

    def testInvalidMovie(self):
        ts = "Invalid Movie"
        recommendations = rcmd(ts)
        self.assertEqual(recommendations, "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies")

    def testNoRecommendationsForGenre(self):
        ts = "Romantic movie"
        recommendations = rcmd(ts)
        self.assertEqual(recommendations, "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies")

    def testCaseSensitivity(self):
        ts_upper = "TOY STORY"
        ts_lower = "toy story"
    
        recommendations_upper = rcmd(ts_upper)
        recommendations_lower = rcmd(ts_lower)
    
        self.assertEqual(recommendations_upper, recommendations_lower)

    def testNonExistentMovie(self):
        ts = "Nonexistent Movie"
        recommendations = rcmd(ts)
        self.assertEqual(recommendations, "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies")

    def testMultipleRecommendations(self):
        ts = "Inception"
        recommendations = rcmd(ts)
        self.assertTrue(len(recommendations) > 1)

    def testLongMovieTitles(self):
        ts = "A Movie with a Very Long and Descriptive Title"
        recommendations = rcmd(ts)
        self.assertTrue(len(recommendations) > 0)

    def testUnicodeCharacters(self):
        ts = "Coco (2017) :) – Remember Me (Lullaby)"
        recommendations = rcmd(ts)
        self.assertTrue(len(recommendations) > 0)

    def testUnexpectedInput(self):
        ts = "12345"
        recommendations = rcmd(ts)
        self.assertEqual(recommendations, "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies")

    def testGibberishInput(self):
        ts = "alkfjasdlfjasldf"
        recommendations = rcmd(ts)
        self.assertEqual(recommendations, "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies")

if __name__ == "__main__":
    unittest.main()
