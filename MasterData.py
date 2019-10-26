import numpy as np

def PN(Y):        #mention the number upto which you want to find the prime number
    Input = np.arange (2, Y+1) #this will create a numpy array for the given range
    while len(Input)>0:
        print(Input[0])
        for i in range (0, len(Input)):
            if i % Input[0] == 0: 
                Input[i]= Input [0]
            else:
                Input[i]= Input[i]  
        Input = Input[Input != Input[0]] #this will drop all the non-prime number and loop will re-run with remaining numbers. 

PN (100000)
