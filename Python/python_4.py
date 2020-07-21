import numpy as np
import random
X = np.random.normal(0,1,(20,20))

y = np.array([random.choice(list(range(-50,50))) for i in range(20)], dtype = np.int32).reshape(-1,1)

theta = np.dot(np.dot(np.linalg.inv(np.dot(X,X.T)),X.T),y)
