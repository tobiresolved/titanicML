import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class Data_Handling():
    def __init__(self):
        self.train_data = self.read_csv_into_dataframe("src\\data\\train.csv")
        self.test_data = self.read_csv_into_dataframe("src\\data\\test.csv")
        self.train_data = self.clean_data(self.train_data)
        self.test_data = self.clean_data(self.test_data)
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

    def clean_data(self, dataframe):
        # Cleans the data and handles missing data
            
        try:
            dataframe.drop(columns=['Name'], inplace=True) # The Name is irrelevant
            dataframe.drop(columns=['Cabin'], inplace=True) # Too many missing values(687/891)
            mean_age = dataframe['Age'].mean()              # Fill missing age by mean age
            dataframe['Age'].fillna(mean_age, inplace=True)         
            dataframe['Embarked'].fillna("S", inplace=True) # Fill the two missing embarked values with "S"
            label_encoder = LabelEncoder()
            dataframe['Sex'] = label_encoder.fit_transform(dataframe['Sex'])
            dataframe['Ticket'] = label_encoder.fit_transform(dataframe['Ticket'])
            dataframe['Embarked'] = label_encoder.fit_transform(dataframe['Embarked'])
            dataframe['Fare'] = label_encoder.fit_transform(dataframe['Fare'])
            return dataframe
        except Exception as e:
            print(f"An error occurred during data cleaning: {e}")

    def split_into_X_y(self):
        # Splits the dataset into the feature set "X" and the target vector "y"
        try:
            self.y = self.train_data["Survived"]
            self.X = self.train_data.drop(columns=['Survived'])
            print(self.X)
            print(self.y)
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

        print("Training data size:", len(self.X_train))
        print("Validation data size:", len(self.X_val))
   

    


        
            

        

        

