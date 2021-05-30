import pandas

#import dataset
db=pandas.read_csv("SalaryData.csv")

#print dataset
print(db)
print(db.columns)


y=db['Salary']
x=db['YearsExperience']

#reshape x frpm pandas into ndarray
print(type(x))
x=x.values
print(type(x))

#reshape x from 1D array into 2D array 
print(x.shape)
x=x.reshape(-1,1)
print(x.shape)

#import module
from sklearn.linear_model import LinearRegression

#create empty model
model=LinearRegression()

#train model
model.fit(x,y)

#import joblib module
import joblib

#create the trained model
joblib.dump(model,'SalaryEstimate.pk1')


