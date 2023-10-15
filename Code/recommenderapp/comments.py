import pandas as pd

import os

app_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(app_dir)
project_dir = os.path.dirname(code_dir)

class Comments:
    df = pd.read_csv(project_dir + "/data/comments.csv")

    def __init__(self):
        pass

    def getComments(self, movie):
        movie_entries = self.df[self.df['movie_name'] == movie]
        return movie_entries