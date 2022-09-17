from distutils.log import Log
import numpy as np

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression




class IrisClassifier:
    
    def __init__(self):
        self.X, self.y = load_iris(return_X_y=True)
        self.classifier = self.train_model()
        self.iris_type = {
            0: 'setosa', 1: 'versicolor', 2: 'virginica'
        }
        
    def train_model(self) -> LogisticRegression:
        return LogisticRegression(solver='lbfgs', max_iter = 1000, multi_class='multinomial').fit(self.X, self.y)
    
    def classify_iris(self, features: dict):
        x = [features['sepal_l'], features['sepal_w'], features['petal_l'], features['petal_w']]
        
        pred = self.classifier.predict_proba([x])
        
        return {
            'class': self.iris_type[np.argmax(pred)], 'probability': round(max(pred[0]), 2)
        }