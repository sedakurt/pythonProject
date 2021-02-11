#The continue statement skips the current part of the loop and moves on to the next part of the loop.


for number in range(1,10):
    if number == 5:
        print("We're skipping number 5.")
        continue
    print("This is the number {}.".format(number))