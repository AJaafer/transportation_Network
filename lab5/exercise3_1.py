'''
xingeng wang
11144515
xiw031
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.utils import check_random_state
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50. * np.log(1 + np.arange(n))
x= np.array([x]).transpose()
y= np.array([y]).transpose()
regr = linear_model.LinearRegression()
regr.fit(x,y)
plt.scatter(x,y)
plt.plot(x,regr.predict(x))
plt.show()
