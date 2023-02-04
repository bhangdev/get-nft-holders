import time
import glob
import pandas as pd

csv_files = glob.glob('data/*.{}'.format('csv'))
print("CSV files: %s" % csv_files)

files = []

for file in csv_files:
    temp = pd.read_csv(file)
    files.append(temp)

result = pd.concat(files)

filename = "data/merged/holders_MERGED_%s.csv" % str(time.time())

result.drop_duplicates(subset="address", keep="first", inplace=True)
result.to_csv(filename, index=False)

print("Files merged: ", result.head())
