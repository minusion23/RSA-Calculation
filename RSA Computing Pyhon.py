
# coding: utf-8

# In[72]:


# A simple RSA computing algorithm based on the PBS Infinite Series video


# Import math - needed for easy calculation of the greatest common divisor
import math

# Provide a number being a multiple of two prime numbers to calculate the two underlying primes
N = 7

# A version with user providing the number:
# {
# try: 
#     N = int(input("Please provide a prime number being a product of two other prime numbers "))
# except :
#     print("This is not a valid number")
# }
    


# In[73]:


i = N
psol = 0
qsol = 0

# Checking if input is not 2 or is not a prime number altogether
if i == 2:
  
    print("The solutions are 1, 2")

elif i % 2 == 0:
    
    print ("The number provided is not a prime number")

else:
        
# Create a list of potential solutions
    potentialSolutions = []
    
# Picking a number smaller than N making sure it is relatively prime to N - that means that the greatest common denominator 
# is 1. If that's the case check if it is a potential answer to the equation 

    while i > 0:

# Going through potential odd numbers that could be solutions to the problem until we reach 0

        d = i - 2
        i -= 2
        
# Checking if the potential solution number is relatively prime to the target number
        
        z = math.gcd(d, N)

        if z == 1:


            counting = True 
            while(counting):
                
                ii = 1
                periodListOfCurrentR = []
                
# Computing the period of d MOD N
                
                while ii < 6:
                    ii += 1
                    zz = (d**ii)%10 

                    if zz not in periodListOfCurrentR:
                        periodListOfCurrentR.append(zz)
                    else:
                        break

                r = len(periodListOfCurrentR)
                
# If the period is not divisible by 2 break the loop and try another solution  

                if r % 2 != 0:
                    counting = False
                    break
                
# If the base for the solution

#                 if (d**(r/2) + 1) % N == 0:
#                     counting = False
#                     break
                    
                    
# Find the potential solutions:
                    
                else:
                    pSol = math.gcd(d**(r//2)-1, N)
                    qSol = math.gcd(d**(r//2)+1, N)
                    if pSol != 1 and pSol != N and pSol %2 != 0 :
                        potentialSolutions.append(pSol)
                    if qSol != 1 and qSol != N and pSol %2 != 0 :
                        potentialSolutions.append(qSol)
                    counting = False
                    break

#     print(r)
#     print(periodListOfCurrentR)

    if len(set(potentialSolutions)) < 3:
        
        print("The solutions are: [{0}]".format(', '.join(map(str, set(potentialSolutions)))))
        
    else:
        print("The original number was not prime") 

