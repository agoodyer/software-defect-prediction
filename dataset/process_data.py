import pandas as pd
from scipy.io import arff
import os 

# Script for converting original .arff files to .csv

arff_dir = './dataset/dataset_arff'
csv_dir = './dataset/dataset_csv'

def arff_to_csv(arff_filepath):
    try:
        data, _ = arff.loadarff(arff_filepath)
        df = pd.DataFrame(data)

        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].str.decode('utf-8')

        base_name = os.path.splitext(os.path.basename(arff_filepath))[0]
        csv_filepath = os.path.join(csv_dir, base_name + '.csv')
        df.to_csv(csv_filepath,index=False)

    except Exception as e:
        print(f"An error occured while converting {arff_filepath}: {e}")

def convert_all_arff():
    
    print(f"Converting all .arff files in directory {arff_dir}")

    for filename in os.listdir(arff_dir):

        if filename.endswith('.arff'):
            arff_filepath = os.path.join(arff_dir, filename)
            arff_to_csv(arff_filepath)
            print(f"Succesfully converted file {filename} to .csv")
        
convert_all_arff()