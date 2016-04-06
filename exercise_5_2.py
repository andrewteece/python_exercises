largest = None
smallest = None
while True:
    u_inp = raw_input('Enter a number: ')
    if u_inp == 'done':
        break
    try:
        num = int(u_inp)
    except:
        print 'Invalid input'
        continue

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print 'Maximum is', largest
print 'Minimum is', smallest



