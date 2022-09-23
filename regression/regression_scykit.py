import numpy as np 
import matplotlib.pyplot as plt 
  
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score 
import statsmodels.api as sm

x = np.array([1,2,3,4,5])  #Abhängige Variable -> von y abhängig! (Bsp. Energie )
y = np.array([7,14,15,18,19]) #Unabhängige Variable -> von x nixht abhängig! (Bsp. Produktion)

x,y


x = x.reshape(-1,1) 
regression_model = LinearRegression() 
  
regression_model.fit(x, y) 
  
y_predicted = regression_model.predict(x) 
  
mse=mean_squared_error(y,y_predicted) 
  
rmse = np.sqrt(mean_squared_error(y, y_predicted)) 
r2 = r2_score(y, y_predicted) 



print('Slope:' ,regression_model.coef_) 
print('Intercept:', regression_model.intercept_) 
print('MSE:',mse) 
print('Root mean squared error: ', rmse) 
print('R2 score: ', r2)


  
def plot_regression_line(x, y, b0,b1): 
    
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    
    y_pred = b0 + b1*x 
  
    
    plt.plot(x, y_pred, color = "g") 
  
    
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    
    plt.show() 