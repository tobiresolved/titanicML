import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class Data_Handling():
    def __init__(self):
        self.train_data = self.read_csv_into_dataframe("src\\data\\train.csv")
        self.test_data = self.read_csv_into_dataframe("src\\data\\test.csv")
        self.concat_df()
        self.explore_data()
        self.clean_data()
        self.explore_data()
        self.divide_df()
        self.split_into_X_y()

    def concat_df(self):
        # Returns a concatenated df of training and test set
        self.all_data =  pd.concat([self.train_data, self.test_data], sort=True).reset_index(drop=True)
    
    def divide_df(self):
        # Returns divided dfs of training and test set
        self.train_data = self.all_data.loc[:890]
        self.test_data = self.all_data.loc[891:].drop(['Survived'], axis=1)
       

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
    
    def explore_data(self):
        try:
            self.all_data.info()
            columns_with_null = self.all_data.columns[self.all_data.isna().any()]
            print(f"COLLUMNS WITH MISSING VALUES: {columns_with_null}")
        except Exception as e:
            print(f"An unexpected error occurred during exploring: {e}")
        
    def fill_age(self):
        try:
            median_age_by_pclass_sex = self.all_data.groupby(['Sex', 'Pclass'])['Age'].transform('median')
            self.all_data['Age'].fillna(median_age_by_pclass_sex, inplace=True)
        except Exception as e:
            print(f"An error occurred: {e}. Please review your data for potential issues.")

    def fill_fare(self):
        try:
            med_fare = self.all_data.groupby(['Pclass', 'Parch', 'SibSp']).Fare.median()[3][0][0]
            self.all_data['Fare'] = self.all_data['Fare'].fillna(med_fare)
        except Exception as e:
            print(f"An error occurred: {e}. Please review your data for potential issues.")
       
    


    def clean_data(self):
        # Cleans the data and handles missing data
        try:
            # Fill the Age attribute by the median of passenger class and sex
            self.fill_age()
            # Fill the two missing ports
            self.all_data['Embarked'] = self.all_data['Embarked'].fillna('S') 
            # Fill the missing fare by the median of third class with no family aboard
            self.fill_fare()
            # Drop the Cabin attribute due to too many missing values
            self.all_data = self.all_data.drop(columns=['Cabin'])

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

   

    


        
            

        

        

