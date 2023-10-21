from data_handler import Data_Handling
from logistic_regression import CustomLogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
def main():

    dh = Data_Handling()
    clf = CustomLogisticRegression(data_handler= dh)
  
    if False:
        clf.train(df.X, df.y)
        # Make predictions
        y_pred = clf.predict(df.X_val)

        # Evaluate the model's accuracy
        accuracy = accuracy_score(df.y_val, y_pred)
        print(f"Accuracy: {accuracy * 100:.2f}%")

        print(df.test_data)
        missing_values = df.test_data.isna()  # or df.isnull()

# You can also count the missing values in each column
        missing_counts = df.test_data.isna().sum()  # or df.isnull().sum()
        print(df.test_data)

    

        print("\nMissing Value Counts per Column:")
        print(missing_counts)

        y_prediction = clf.predict(df.test_data)
        print(y_prediction)

        submission = pd.read_csv("src\\data\\gender_submission.csv")
        submission['Survived'] = y_prediction
        submission.to_csv("src\\data\\gender_submission.csv", index=False)




    

if __name__ == "__main__":
    main()
