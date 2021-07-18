# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def binary_FRAC(fraction):
    binary = str()
    while (fraction):
        fraction*=2
        if fraction>=1:
            integer=1
            fraction-=1
        else:
            integer=0
        binary+=str(integer)
    #The binary string now contains our binary fraction representation
    return binary

def binary_IEEE(num):
    #Initialize the 3 variables that are to be passed
    sign_bit, bias_exp, significand, ind = 0,0,0,0
    #Assign the sign bit based on the absolute sum of the number
    try:
        if num<0:
            sign_bit=1
        #since the sign-bit already has the sign of the number
        #we take it's absolute value for further operations
        num=abs(num)
        #Convert integer part of the number to binary
        bin_int = bin(int(num))[2:]
        #Extract and convert the fraction part to binary
        frac_part = num - int(num)
        bin_frac = binary_FRAC(frac_part)
        #find the index of the first 1 in the mantissa
        try:
            ind=bin_int.index('1')
        except:
            ind=-(bin_frac.index('1')+1)
            pass
        #Calculating the biased exponent
        if ind<0:
            index_calc=ind
            bias_exp = bin(ind+127)[2:].zfill(8)
        else:
            index_calc=(len(bin_int) - ind - 1)
            bias_exp = bin((len(bin_int) - ind - 1) + 127)[2 : ].zfill(8)
        #Calculate the Significand
        if index_calc>128 or index_calc<-127:
            raise SystemExit('Input not in range')
        if ind<0:
            significand = bin_frac[(bin_frac.index('1')+1) : ]
        else:
            significand = bin_int[ind + 1 : ] + bin_frac
        #Adding 0's in the LSB to fill up 23 spaces for significand
        if len(significand)<=23:
            significand = significand + ('0' * (23 - len(significand)))
        else:
            significand = significand[:23]
        return sign_bit, bias_exp, significand
    except:
        return -1,-1,-1
  

if __name__ == '__main__':
    dec_num=input("Enter the decimal number :")
    dec_num=float(dec_num)
    
    sign_bit, bias_exp, significand = binary_IEEE(dec_num)
    if sign_bit==bias_exp==significand==-1:
        print('{0} cannot be represented in the IEEE 754 representation'.format(dec_num))
    else:
        print('The binary floating-point representation of {0} as per IEEE 754 is:'.format(dec_num))
        ieee_rep=str(sign_bit) + ' ' + bias_exp + ' ' + significand
        print(ieee_rep)
