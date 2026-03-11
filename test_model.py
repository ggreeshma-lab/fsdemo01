import numpy as np
from sklearn.linear_model import LinearRegression
x=np.array([[1],[2],[3],[4]])
y=np.array([2,4,6,8])

def test_coefficent():
    model=LinearRegression()
    model.fit(x,y)
    assert round(model.coef_[0],2) == 2.0

def test_intercept():
    model=LinearRegression()
    model.fit(x,y)
    assert round(model.intercept_,2) == 0.0

def test_prediction():
    model = LinearRegression()
    model.fit(x,y)
    pred =model.prediction([[5]])
    assert round(pred [0,2]==10.0)