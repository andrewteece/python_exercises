largest = None
smallest = None
while True:
    u_inp = raw_input("Enter a number: ")
    if u_inp == "done":break
    try:
        num = int(u_inp)
    except: 
        print "Invalid input"
        continue
    else: 
        if smallest is None: 
            smallest = num
            largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

print "Maximum is", largest
print "Minimum is", smallest



