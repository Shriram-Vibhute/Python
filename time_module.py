import time

# This loop will run exactly like setInterval in javascript -> Synchronous

"""
let count = 1;
setInterval(()=> {
    console.log(count);
    count++;
}, 1000)
"""

for i in range (4):
    time.sleep(1) # delay function -> parameter in sec
    print(i)


# ctime -> converts the from sec to exact time
tm = time.ctime(1627908313.717886)
print(tm)

# time -> returns the total time in seconds from 1 jan 1970 to current
print(time.time())



from time import gmtime, strftime
s = strftime("%a, %d %b %Y %H:%M:%S") # This gives current time
'''
%a -> Day
%d -> Date
%b -> Month
%Y -> Year
%H -> Hour
%M -> Min
%S -> sec
'''
s = strftime("%a, %d %b %Y %H:%M:%S", gmtime(1627987508.6496193)) # Givan time to Human Readable time -> ctime(time)

print(s)


string = "Tue, 03 Aug 2021 10:45:08" # The pattern of string and the function is must be same
obj = time.strptime(string, "%a %d %b %Y %H:%M:%S")
print(obj)