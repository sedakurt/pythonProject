#WHILE

temp_f= 30

while temp_f > 18:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 2 #If we don't use this decrement the loop will be infinite

    if temp_f == 24:
        break #The break statement indicates that when you see it, the loop should end and go on to the next statement in the program that is outside of the loop.