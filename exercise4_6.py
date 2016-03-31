def computepay(hrs, rate):
    if (hrs > 40):
        pay = (40 * rate) + (hrs - 40) * 1.5 * rate
    else:
        pay = (hrs * rate)
    return pay

try:
    hrs = float(raw_input("Enter Hours: "))
    rate = float(raw_input("Enter Rate: "))    
except:
    print "Please enter a number"
    quit()    
p = computepay (hrs, rate)
print p