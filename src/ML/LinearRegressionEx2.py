import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

#dummy dataset for house predication

data={
    "size":[1000,1500,2000,2500,3000],
    "price":[50,75,100,125,150]
}
dataframe=pd.DataFrame(data)
print(dataframe)
X=dataframe[['size']]
y=dataframe[['price']]
#splitting into train and test
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("predictions=",predictions)
print("actual=",y_test.values)

#Evalute Performeance
mse=mean_squared_error(y_test,predictions)
print("mse=",mse)
r2=r2_score(y_test,predictions)
print(r2)

print(model.coef_[0])
print(model.intercept_)