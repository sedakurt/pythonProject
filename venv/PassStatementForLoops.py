#The pass statement skips any part of the loop where pass appears. This is best used for testing code, but make sure you don't forget to remove the pass statement when you're ready for your code to go into production.


for number in range(1,5):
    if number == 3:
        pass
    else:
       print("This is the number {}.".format(number))

       '''
       This is the number 1.
       This is the number 2.
       This is the number 4.       
       '''


