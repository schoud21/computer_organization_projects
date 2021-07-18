# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 21:33:27 2021

@author: schoud21
"""

import random

'''
Function to Determine the Banyan Network Switching For 16 inputs.
The Switching happens over 4 levels each determining the path for 
the corresponding bit
'''
def banyan_network_switching_16(input_port, value):
    switch1 = {
        'A1': ['B1', 'B5'],
        'A2': ['B2', 'B6'],
        'A3': ['B3', 'B7'],
        'A4': ['B4', 'B8'],
        'A5': ['B1', 'B5'],
        'A6': ['B2', 'B6'],
        'A7': ['B3', 'B7'],
        'A8': ['B4', 'B8']
        }
    
    switch2 = {
        'B1': ['C1', 'C3'],
        'B2': ['C2', 'C4'],
        'B3': ['C1', 'C3'],
        'B4': ['C2', 'C4'],
        'B5': ['C5', 'C7'],
        'B6': ['C6', 'C8'],
        'B7': ['C5', 'C7'],
        'B8': ['C6', 'C8']
        }
    
    switch3 = {
        'C1': ['D1', 'D2'],
        'C2': ['D1', 'D2'],
        'C3': ['D3', 'D4'],
        'C4': ['D3', 'D4'],
        'C5': ['D5', 'D6'],
        'C6': ['D5', 'D6'],
        'C7': ['D7', 'D8'],
        'C8': ['D7', 'D8']
        }

    switch4 = {
        'D1': ['0', '1'],
        'D2': ['2', '3'],
        'D3': ['4', '5'],
        'D4': ['6', '7'],
        'D5': ['8', '9'],
        'D6': ['10', '11'],
        'D7': ['12', '13'],
        'D8': ['14', '15']
        }
    
    if input_port not in switch1:
        return ValueError("Invalid Starting Port")
    
    path=input_port
    network=[switch1, switch2, switch3, switch4]
    print("Process Flow [", value , "]")
    for index, val in enumerate(value):
        print(' ', path, ' --> ', end="")
        path = network[index][path][int(val)]
    print(path)

'''
Function to Determine the Banyan Network Switching For 8 inputs.
The Switching happens over 3 levels each determining the path for 
the corresponding bit
'''        
def banyan_network_switching_8(input_port, value):
    switch1 = {
        'A1': ['B1', 'B3'],
        'A2': ['B2', 'B4'],
        'A3': ['B1', 'B3'],
        'A4': ['B2', 'B4']
        }
    
    switch2 = {
        'B1': ['C1', 'C2'],
        'B2': ['C1', 'C2'],
        'B3': ['C3', 'C4'],
        'B4': ['C3', 'C4']
        }
    
    switch3 = {
        'C1': ['0', '1'],
        'C2': ['2', '3'],
        'C3': ['4', '5'],
        'C4': ['6', '7']
        }

    if input_port not in switch1:
        return ValueError("Invalid Starting Port")
    
    path=input_port
    network=[switch1, switch2, switch3]
    print("Process Flow for [",value, "]")
    for index, val in enumerate(value):
        print(' ', path, ' --> ', end="")
        path = network[index][path][int(val)]
    print(path)

'''
main() co-ordinates the flow of the entire program. It does the following:
    1. Takes the input for number of inputs from the user and also if the user
       would like to transmit the same over a 16X16 Network.
    2. If no value is given for Network, code directs the flow to 8X8 or 16X16 network based
       on the max number of bits that is used to represent the inputs
    3. Determines, starting_path={} which keeps record of the starting path for each input
    4. Based on the number of inputs, banyan_network_switching_16() or 
       banyan_network_switching_8() is called.
    5. If in case user wishes to explicitly use the 16X16 network, it is called. 
       Otherwise we use the understanding in Point 4 to determine the Banyan Network 
       Switching method to be used.
'''
def main():
    #Number of inputs for the Network
    inputs = []
    n = int(input('enter the number of inputs: \n'))
    network = bool(input('Would you like to use a 16X16 network? (Do not answer if you wish to use default network) \n'))
    #generate Random numbers
    while len(inputs)!=n:
        if network:
            randN = random.randint(0, 15)
        else:
            if n<=8:
                randN = random.randint(0, 7)
            elif n>8 and n<=16:
                randN = random.randint(0, 15)
            else:
                raise ValueError("Code is built for a *X8 or 16X16 network. Cannot support a higher value!")
        if randN not in inputs:
            inputs.append(randN)
    print("Randomly generated numbers are:\n", inputs)
    
    #Sorting the Inputs in ascending order
    inputs.sort()
    print("Sorted input after Batcher:\n", inputs)
    input_dict = {}
    for i in range(n):
        input_dict[i] = inputs[i]
    print("\nInputs attached to corresponding input ports:\n", input_dict)
    
    
    print('\n')
    #Using Batcher Sort to determine the Banyan Network port the Random input is mappped too
    starting_path={}
    for i in range(n):
        if n<=8 and network==False:
            if i < 4:
                starting_path[str(i)] = 'A'+str(i+1)
            else:
                starting_path[str(i)] = 'A'+str(int(i-3))
        else:
            if i < 8:
                starting_path[str(i)] = 'A'+str(i+1)
            else:
                starting_path[str(i)] = 'A'+str(int(i-7))
    #Staring points for each Input port
    print("Defining the starting points for each input:")
    print(starting_path)
    
    print('\n\n')
    #Finding the path for each input
    for i in range(n):
        x=bin(input_dict[i])[2:].zfill(len(bin(n-1)[2:]))
        if network:
            if len(x)<4:
                banyan_network_switching_16(starting_path[str(i)], x.zfill(4))
            else:
                banyan_network_switching_16(starting_path[str(i)], x)
        else: 
            if len(x) == 4:
                banyan_network_switching_16(starting_path[str(i)], x)
            else:
                if len(x) == 3:
                    banyan_network_switching_8(starting_path[str(i)], x)
                else:
                    banyan_network_switching_8(starting_path[str(i)], x.zfill(3))

if __name__ == '__main__':
    main()