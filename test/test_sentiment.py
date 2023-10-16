import unittest
import warnings
import sys

sys.path.append("../")
from Code.prediction_scripts.item_based import getSentimentScores

warnings.filterwarnings("ignore")


class Tests(unittest.TestCase):
    def test_positive(self):
        ts = "Good Movie"
        sentiment = getSentimentScores(ts)
        self.assertTrue(sentiment == "Supportive")

    def test_negative(self):
        ts = "Bad Movie"
        sentiment = getSentimentScores(ts)
        self.assertTrue(sentiment == "Critical")


if __name__ == "__main__":
    unittest.main()
