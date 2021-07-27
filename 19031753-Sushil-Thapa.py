def GreetingAtEnd():
    print("\n")
    print("***Thank you for using the conversion system. :):)***")

continueLoop=True
while continueLoop==True:

        def userInput():
                g=False
                while g==False:
                        try:   #try block lets you test a block of code for errors
                            f_number=int(input("Enter your First Decimal Number: ")) #taking input from user
                            if f_number>0 and f_number<=255: #checking input if this satisfy this statement will continue
                                g=True
                            else: #if the upper user input doesnt satisfy this statement will run
                                print("Doesnt match please enter number between 0-255")
             
                        except: #The except block lets you handle the error.
                            print("INVALID INPUT!!!")
                            print("Please type again......")

                            
                f=False
                while f==False:
                        try: #try block lets you test a block of code for errors
                            l_number=int(input("Enter your last Decimal Number: ")) #taking input from user
                            if f_number>0 and f_number<=255:  #checking input if this satisfy this statement will continue
                                f=True
                            else: #if the upper user input doesnt satisfy this statement will run
                                print("Doesnt match please enter number between 0-255")
             
                        except: #The except block lets you handle the error.
                            print("INVALID INPUT!!!")
                            print("Please type again......")

                if(f_number + l_number)>=255: #checking input if this satisfy this statement will continue and the program will auto shut down
                    print("The value should  be between 0 to 255. “9bit numbers are not Allowed to be displayed” So, the program will close now.")
                    exit()
                upper_bit = [int(x) for x in list('{:08b}'.format(f_number))]# using list comprehension to perform conversion
                lower_bit = [int(x) for x in list('{:08b}'.format(l_number))]# using list comprehension to perform conversion
                return (upper_bit, lower_bit)

        def andGate(valOne, valTwo): #bitwise #defining function andgate
                return valOne & valTwo #Return “and value” of valone and valtwo 

        def orGate(valOne, valTwo): #bitwiseor #defining function orgate
                return valOne | valTwo

        def compliment(bitValue): #notoperation #defining function compliment
                return ~bitValue 

        def xorGate(bitOne, bitTwo): #by passing through or and and gates #defining function
                return orGate(andGate(bitOne, compliment(bitTwo)), andGate(compliment(bitOne), bitTwo)) #Return value of andGate and compliment by calling orGate

        def calculateCarry(q, r, s, t): #by perforing and gate, xor gate, or gate #defining function calculatecarry
                return orGate(andGate(q,r), andGate(s,t)) #Evaluatecary Return the value of andGate when the parameters (q,r,s,t) are passed by calling orGate


        def calculateResult(upper_bit, lower_bit): ##defining function calculateresult
                result = []
                carry = 0
                for index in range(len(upper_bit)): #implement for loop
                        after_xor_cal = xorGate(upper_bit[index], lower_bit[index])
                        result.append(xorGate(after_xor_cal, carry))
                        carry = calculateCarry(upper_bit[index], lower_bit[index], after_xor_cal, carry)

                result.append(carry)
                return list(reversed(result))

        def main(): #defining function main
                while True: 
                        upper_bit, lower_bit = userInput()
                        result = calculateResult(list(reversed(upper_bit)), list(reversed(lower_bit)))
                        print("The conversion of decimal to binary is:", ''.join(str(e) for e in result)) #Display conversion of binary number
                        return result
        variable=main()


        def binToDec():
            "This function is responsible to convert the 8 bit binary digit obtained from the final_result into decimal value."
            list1 = variable
            init = 1
            dec_v = 0
            for i in range(len(list1)-1, - 1, - 1): #Evaluatecarry function and store them in variable carry Return the value of result stored in list in a reversed manner
                dec_v += init*list1[i]
                init = init*2
            print("\nThe addition of two decimal number taken from user is:", dec_v) #Display addition of two decimal number taken from user
        binToDec()

        print("\n")

        continuous=input("Do you want to continue??? Type 'No' to exit").lower() #store value 
        if continuous=="no":
                break
print("\n")
print("\n")
GreetingAtEnd()
