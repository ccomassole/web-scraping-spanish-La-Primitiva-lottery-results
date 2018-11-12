# Press CTRL + B to launch the Script from SublimeText
# Practice 1. Web Scraping from the website loteriasyapuestasdelestado.es

# Main module.
import os  # path management
import numpy as np  # Advanced calculations (required by pandas library)
import pandas as pd  # Multidimensional data manipulation
import time  # time control
from scraper import Scraper  # library created for this particular project, having the definition of the Scraper Class

# We have previously analysed the characteristics of the pages to scrap (see document: previous.pdf).

# Declaring the draws of interest
draws = [
    'Classic',
    'ElGordo'
]
output_file = "dataset.csv"  # output file declaration
initial_path = os.getcwd()
os.chdir("..")
path = os.getcwd()
try:
    os.chdir("../csv")
except:
    os.mkdir("csv")
path = os.path.join(path, "csv", output_file)
os.chdir(initial_path)
df = pd.DataFrame()  # empty dataframe to store the results from all draws
# Start timer
print('Starting the process of getting data.\n')
print('This will take roughly 3 minutes.\n')
start_time = time.time()
for i in np.arange(0, len(draws)):
    print("Trying " + draws[i] + '...\n')
    game = Scraper(draws[i])  # Scrape Class instantiation for each game
    df = pd.concat([df, game.scrape()], sort=True)  # Joining data
print(path)
df.to_csv(path, sep=",", index=False)  # Saving data in a single file
print("\nData properly stored in " + output_file)
# Show elapsed time
end_time = time.time()
print("\nelapsed time: " + str(round(((end_time - start_time) / 60), 2)) + " minutes")
