from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class CustomLogisticRegression:
    def __init__(self, data_handler):
        self.model = LogisticRegression(penalty='l2', C=1.0, solver='lbfgs', max_iter=1000)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)




    