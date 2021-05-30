#import joblib module
import joblib 

#load the pre trained model  
mind = joblib.load("SalaryEstimate.pk1")

repeat = True
while repeat :
    s=float(input("Enter your years of experience to estimate the salary : "))
    #predict salary
    print(mind.predict([[ s ]]))
    check=input("Want to continue [y/n]: ")
    if check == "n" :
        break
