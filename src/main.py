import pandas as pd
import csv

def main():
   with open('./data/dataset/train.csv', 'r') as file:
      # creating a csv reader object
      csv_reader = csv.reader(file)

      dataset = pd.DataFrame(csv_reader)
      
      entry_data = dataset.head(120)
      
      entry_data.to_csv('./data/dataset/entry_data.csv', index=False)
      
if __name__ == "__main__":
   main()
