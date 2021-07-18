# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:50:32 2021

@author: schoud21
"""

#Perform Binary addition for the two 8-bit binary numbers given as input by:
# 1. Add the respective bits from each number
# 2. If the addition is >1, we set our carry bit=1
# 3. The resultant bit of the summation that is added to output string = Sum%2
# 4. The Addition string is reversed, as we perform this calculation from Right to Left
#Note: If the summation of the numbers is a 9-bit number, the carry bit(9th) is 
#ignored thus maintaining a 8-bit system
def binary_add(x, y):
    carry=0
    bin_sum=''
    for i in range(len(x)-1, -1, -1):
        temp=int(x[i])+int(y[i])+carry
        if temp>1:
            bin_sum+=str(temp%2)
            carry=1
        else:
            bin_sum+=str(temp)
            carry=0
    return bin_sum[::-1]


#Finding the 2s complement of the Binary number by the following steps:
# 1. Find the 1s complement of the number by performing the following action
#    on each bit: Bit = (Bit+1)%2
# 2. Add 00000001(Binary 8 bits systems) or 1 to this 1s complement
def compliment(x): 
    comp = ''   
    # Iterating through the number 
    for i in range (0, len(x)):   
        # Computing the compliment 
        comp += str((int(x[i]) + 1) % 2)   
    # Adding 1 to the computed value 
    comp
    comp = binary_add(comp, '00000001') 
    return comp


#Restoring 2s complement divison in a step-wise process:
# 1. Left shift registers A,Q
# 2. A_new = A+Mc (Mc = 2s complement of M)
# 3. Check if A_new is negative. If yes then Q0=0, else A=A_new and Q0=1
def restoring_division(A, Q, M):
    M_c=compliment(M)
    #Left Shift the values in A and Q registers
    A=A[1:]+Q[0]
    Q=Q[1:]
    A_new = binary_add(A, M_c)
    if A_new[0]=='1':
        Q=Q+'0'
    else:
        A=A_new
        Q=Q+'1'
    return A, Q, M


#The main() to compute the necessary output
#It iteratively calls the restoring_division() which performs our division step by step
def main(dividend, divisor):
    
    #initialize the sign bits of the numbers and the registers 
    #that will be used in the division
    sign_dividend, sign_divisor = '+','+'
    M, Q, A, count = '','',bin(int(0))[2:].zfill(8),0
    
    #Check the signs of both numerator and denominator and store them 
    if dividend<0:
        if divisor<0:
            sign_divisor='-'
            sign_dividend='-'
        else:
            sign_dividend='-'
    elif divisor<0:
        sign_divisor='-'
    
    #Take the Absolute value of both Dividend and Divisor, we change back the sign once
    #the division is complete
    dividend=abs(dividend)
    divisor=abs(divisor)
    print(dividend)
    print(divisor)
    #Initialize the values of Q and M register with the binary values 
    #For Dividend and Divisor respectively
    Q = bin(int(dividend))[2:].zfill(8)
    M = bin(int(divisor))[2:].zfill(8)
    count = len(Q)
    
    #Iteratively compute the result of the division by calling the restoring_division()
    #for the number of bits in the dividend
    print('The initial values in the registers A, Q and M are:')
    print('       A ||        Q ||        M')
    print('{0} || {1} || {2}'.format(A, Q, M))
    print('--------------------------------------------------------------------------------------')
    for i in range(count):
        A, Q, M = restoring_division(A, Q, M)
        print('       A ||        Q ||        M')
        print('{0} || {1} || {2}    ----> Step {3}'.format(A, Q, M, (i+1)))
     
    #The computed binary quotient and remainder after performing
    #restoring 2s complement division
    print('\nBinary unsigned output after the final cycle:')
    print('       A ||        Q')
    print('{0} || {1}'.format(A, Q))
    
    #Based on the signs of the Dividend and Divisor we compute the signs of 
    #The Quotient and Remainder using the understanding
    #sign(R)=sign(D) and sign(Q)=sign(D)*sign(V) 
    #where D,V,Q,R are Dividend, Divisor, Quotient and Remainder respectively
    #Also compute the decimal values for the Quotient and remainder
    if sign_dividend=='-':
        if sign_divisor=='-':
            print('Both the Dividend and Divisor are negative, so only Remainder is negative')
            A = int(A, 2)*-1
            Q = int(Q, 2)
        else:
            print('Only the dividend is negative so both the remainder and quotient are negative')
            A = int(A, 2)*-1
            Q = int(Q, 2)*-1
    elif sign_divisor=='-':
        print('Only Divisor is negative so only quotient is negative')
        A = int(A, 2)
        Q = int(Q, 2)*-1
    else:
        print('Both the Dividend and Divisor are positive, no need to change signs')
        A = int(A, 2)
        Q = int(Q, 2)
    
    return Q, A


if __name__ == '__main__':
    
    #Taking user input for Divisor and Dividend
    
    dividend=input("Enter the dividend :")
    divisor=input("Enter the divisor :")
    dividend=float(dividend)
    divisor=float(divisor)
    quotient, remainder = 0,0
    
    # Perform the following checks:
    # 1. Zero Check = If either Divisor or Dividend is zero, our process will not run
    # 2. Overflow Check = Since this Restoring Division is for a 8-bit system,
    #    the abs(Dividend) cannot be > 255 and abs(divisor) cannot be >128
    #    since 2s complement of the same is out of range in a 8-bit system
    # 3. Decimal Check = Both the Dividend and Divisor are integers +ve or -ve
    # 4. Integer check =  Check both divisor and dividend are integers
    
    if divisor.is_integer() and dividend.is_integer():
        divisor=int(divisor)
        dividend=int(dividend)
        if divisor != 0 and dividend !=0:
                if abs(dividend)<256 and abs(divisor)<128:
                    quotient, remainder = main(dividend, divisor)
                    print('The result of the division of {0}/{1} is:'.format(dividend,divisor))
                    print('{0}R{1}'.format(quotient, remainder))
                else:
                    if abs(dividend)>=256 and abs(divisor)>=128:
                        print('''Since this is a 8-bit system, 
                              dividend cannot be more than 255 
                              and since we need to use 2s complement 
                              of the divisor in restoring 2s division, our divisor cannot be >=128
                              as its complement cannot be contained in our system''')
                    elif abs(dividend)>=256:
                        print('Since this is a 8-bit system, dividend cannot be more than 255')
                    else:
                        print('Since in restoring 2s division, we take the complement of the divisor, it needs to be withing -127 and 128')
        elif divisor == 0:
            print("The divisor entered is zero. So division of the numbers is not possible")
        elif dividend == 0:
            print("The output of the above 2 numbers is: {0}R{1}".format(quotient, remainder))
    else:
        print('The divisor and dividend need to be integer in this process')
    