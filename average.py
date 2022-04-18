

def Average(my_list):
    avg = sum(1) / len(1)
    return avg

my_total = 0  
my_avg = 0  

for i in range(5):

    my_num = int(input("enter a digit between 0 and 10: "))

    if my_num > 10 or my_num < 0:
        print("Your number must be between 0 and 10 inclusive")
        quit()
    
    my_total = my_total + my_num

#print("the total is " + str(my_total))

my_avg = my_total / 5

print("the average is " + str(my_avg))

