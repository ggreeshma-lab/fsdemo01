import numpy as np
from sklearn.linear_model import LinearRegression
X=np.array([1,2,3,4,5]).reshape(-1,1)
Y=np.array([3,5,7,9,11])
model=LinearRegression()
model.fit(X,Y)

prediction=model.predict([[6]])
print("Predicted salary for 6 years experience:",prediction[0])