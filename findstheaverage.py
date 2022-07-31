
my_total = 0  
my_avg = 0  
my_count = 0

while True:

    my_num = int(input("enter a digit between 0 and 10: "))

    if my_num == -1:
        print("Goodbye :D")
        break

    if my_num > 10 or my_num < 0:
        print("Your number must be between 0 and 10 inclusive")
        break
    
    my_total = my_total + my_num
    my_count += 1

print("the total is " + str(my_total))

if my_count != 0: 
    my_avg = my_total / my_count

print("the average is " + str(my_avg))

