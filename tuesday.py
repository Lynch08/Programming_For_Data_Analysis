# if statements reviewed

import datetime

today = datetime.datetime.today()
dayoftheweek = today.weekday()

print ("Lets check if its Tuesday")

if dayoftheweek == 1:
    print ("its Tuesday")
elif dayoftheweek == 3:
    print ("Its not Tuesday")
    print (" Missed it two days ago!!!!!!!")
else:
    print ("Not Tuesday")

print ("Thanks for checking day of week")