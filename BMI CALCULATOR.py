#THIS IS A BMI CALCULATOR
H = input('Enter Your Height') #Here 'H' represents the height of the person
W = input('EnterYour Weight')  #Here "w" represents the weight of the person
h = float(H) #Height is in Metre
w = float(W) #Weight is in kg
BMI = (w/h**2)     
bmi = int(BMI)
print("Your BMI is" + str(bmi))
