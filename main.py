import re
import calculateTime as ct

print('Welcome to Time Calculator!')
print('\nKindly Enter your starting time in this format: hh:mm am or pm \nAnd your time duration in: h:mm  \nYou may add as many hours in your Time Duration as you want there is not limit')
print('You may also enter the day you started from. But it is optional')

startingtime=input ('Enter Your Starting Time (hh:mm am/pm): ')
refinedstarttime= startingtime.split(':')
sth = refinedstarttime[0]
stm = refinedstarttime[1].split()[0]
m = refinedstarttime[1].split()[1]




time_duration = input('Enter the Time Duration (you may enter thosands of hours) in the correct format (h:mm): ')
tdh = time_duration.split(':')[0]
tdm = time_duration.split(':')[1]

Day = input('If you want to specify the starting day you may specify it otherwise just press Enter: ')

if len(Day) > 1: 
    day = Day
else :
    day = False


    
Final = ct.calculateTime(sth, stm, m, tdh, tdm, day)




