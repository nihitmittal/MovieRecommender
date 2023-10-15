import pandas as pd

import os
import csv
import datetime

app_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(app_dir)
project_dir = os.path.dirname(code_dir)
file_path = project_dir + "/data/comments.csv"

class Comments:
    def __init__(self):
        pass

    def getComments(self, movie):
        df = pd.read_csv(file_path)
        movie_entries = df[df['movieName'] == movie]
        return movie_entries
    
    def setComments(self, data):
        # Putting data into comments.csv
        all_rows = []
        for key,value in data.items():
            if len(value[1]) > 0: # Save only those fields that are populated
                all_rows.append(["user1","email_id<1>",key,value[1],datetime.datetime.now()])

        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            for row in all_rows:
                writer.writerow(row)