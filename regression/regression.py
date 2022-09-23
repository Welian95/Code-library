#https://de.acervolima.com/losen-der-linearen-regression-in-python/

import numpy as np 
import matplotlib.pyplot as plt 

def reg (x,y):
    ''' This is a function to make a regression analysis.
    param x : np.array with dtype = np.float64 ; dependent variable
    param y : np.array with dtype = np.float64 ; independent variable
    output b1 : gradient 
    output b0 : intercept
    output se : squared error
    output mse : mean squared error 
    output rmse : root mean square error
    output R2 : R square'''

    n = np.size(x) # size of array (Größe des Arrays ermitteln)

    x_mean = np.mean(x) # mean of x values (Mittelwerte des arrays X berechnen) 
    y_mean = np.mean(y) # mean of y value (Mittelwerte des arrays Y berechnen)

    Sxy = np.sum(x*y)- n*x_mean*y_mean 
    Sxx = np.sum(x*x)-n*x_mean*x_mean 
  
    b1 = Sxy/Sxx  #gradient (Steigung)
    b0 = y_mean-b1*x_mean #intercept (Achsenabschnitt)

    y_pred = b1 * x + b0 #linear function (Aufstellen der Geradengleichung)

    error = y - y_pred 
    se = np.sum(error**2) 
  
    mse = se/n  
   
    rmse = np.sqrt(mse) 
  
    SSt = np.sum((y - y_mean)**2) 
    R2 = 1- (se/SSt) 

    return b1, b0, se, mse, rmse, R2 


if __name__ == '__main__':


    #Create a testdata
    x = np.array([1,2,3,4,5], dtype = np.float64)  #Abhängige Variable -> von y abhängig! (Bsp. Energie )
    y = np.array([7,14,15,18,19],dtype = np.float64) #Unabhängige Variable -> von x nixht abhängig! (Bsp. Produktion)

    b1, b0, se, mse, rmse, R2  = reg (x,y)

    print(f'gradient is {b1}.') #Ausgabe Steigung
    print(f'intercept is {b0}.') #Ausgabe Achsenabschnitt
    print(f'linear function is: {b1} * x + {b0}')
    print('squared error is:', se) 
    print('mean squared error is:', mse) 
    print('root mean square error is:', rmse) 
    print('R square is:', R2)

    #Make a plot 
    y_pred = b1 * x + b0
    plt.scatter(x, y, color = 'red')  #Farben der Punkt definiern 
    plt.plot(x, y_pred, color = 'green') #Farben der Regressionslinie (TREND) angeben
    plt.xlabel('X') 
    plt.ylabel('y') 

    plt.show()