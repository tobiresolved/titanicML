import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class Data_Handling():
    def __init__(self):
        self.train_data = self.read_csv_into_dataframe("src\\data\\train.csv")
        self.test_data = self.read_csv_into_dataframe("src\\data\\test.csv")
        self.explore_data(self.train_data)
        
        self.train_data = self.clean_data(self.train_data)
        self.test_data = self.clean_data(self.test_data)
        self.explore_data(self.train_data)
        self.split_into_X_y()
        self.split_into_test_validation_sets()

    def read_csv_into_dataframe(self, link):
        # Reads a csv into pandas dataframa
        try:
            data = pd.read_csv(link)
            return data
        except FileNotFoundError:
            print("The CSV file does not exist.")
        except pd.errors.EmptyDataError:
            print("The CSV file is empty.")
        except pd.errors.ParserError as e:
            print(f"An error occurred while parsing the CSV file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def explore_data(self, dataframe):
        print("____________________________________________________")
        print(dataframe.head())
        print(dataframe.describe())
        print(dataframe.isnull().sum())
        print(dataframe.isnull())
        print(dataframe.isna())
        columns_with_null = dataframe.columns[dataframe.isna().any()]
        print(columns_with_null)
        print("____________________________________________________")



    def clean_data(self, dataframe):
        # Cleans the data and handles missing data
        try:
            dataframe = dataframe.drop(columns=['Cabin']) # Drop the Cabin attribute due to too many missing values

            
            return dataframe
        except Exception as e:
            print(f"An error occurred during data cleaning: {e}")

    def split_into_X_y(self):
        # Splits the dataset into the feature set "X" and the target vector "y"
        try:
            self.y = self.train_data["Survived"]
            self.X = self.train_data.drop(columns=['Survived'])
        except KeyError as e:
            print(f"An error occurred: {e}")
            print("The specified column does not exist in the DataFrame.")
    def split_into_test_validation_sets(self):
        # Splits the feature set "X" into a train and a validation set
        try:
            self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(self.X, self.y, test_size=0.25, random_state=11)
        except ValueError as e:
            print(f"An error occurred: {e}")
            print("Check if data is correctly formatted for splitting.")

   

    


        
            

        

        

