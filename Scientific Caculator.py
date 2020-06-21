#Scientific Calculator
#developer : Fahad Hassan

print("******************W E L C O M E  T O  S C I E N T I F I C  B Y  F A H A D  H A S S A N******************")
print("Remeber ! if you going to perform a unary or trignometry function then your function will be performed on your second number only. THANKS !")


import math

firstNumber = float(input("Please provide a number :"))
op = input("Please provide us the operator to perform operations such as \n 1. + for addition \n 2. - for subtraction \n 3. * for multiplication "
           "\n 4. / for division \n 5. ^ for power \n 6. r for root \n 7. % for modulus \n 8. ! for not \n 9. sin for sinTheta "
           "\n 10. cos for cosTheta \n 11. tan for tantheta \n 12. pie for PIE \n 13. e for exponential \n 14. ln for natural log").lower()

secondNumber = float(input("Please provide second number :"))

if op == "+":
    print (firstNumber, "+", secondNumber, "=", firstNumber + secondNumber )

elif op == "-":
    print (firstNumber, "-", secondNumber, "=", firstNumber - secondNumber )

elif op == "*":
    print (firstNumber, "*", secondNumber, "=", firstNumber * secondNumber )

elif op == "/":
    print (firstNumber, "/", secondNumber, "=", firstNumber / secondNumber )

elif op == "^":
    print (firstNumber, "^", secondNumber, "=", firstNumber ** secondNumber )

elif op == "r":
    print (firstNumber, "root", secondNumber, "=", secondNumber ** (1 / firstNumber) )

elif op == "%":
    print (firstNumber, "%", secondNumber, "=", firstNumber % secondNumber )

#factorial
elif op == "!":
    theNumber = firstNumber = secondNumber
    secondNumber = 1
    while firstNumber > 1:
        secondNumber *= firstNumber
        firstNumber = firstNumber - 1
    print ("n!(", theNumber, ")=", secondNumber )

elif op == "sin":
    print ("sin(", secondNumber, ")=", math.sin(secondNumber ))

elif op == "cos":
    print ("cos(", secondNumber, ")=", math.cos(secondNumber ))

elif op == "tan":
    print ("tan(", secondNumber, ")=", math.tan(secondNumber ))

elif op == "pie" or op == "pi":
    print ("Pie =", math.pi)

elif op == "e":
    print = ("E =", math.e)

elif op == "ln":
    print ("ln(", secondNumber , ")= ", math.log(secondNumber))

else:
    print ("incorrect operator")