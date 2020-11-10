# import datetime # downside we have to write datetime.datetime all the time then
from datetime import datetime
start = datetime.now()
mylist = [f"{x} - something" for x in range(1_000_000)]  
# so takes about 2 seconds to create a list with 1M elements
end = datetime.now()
print(start ,end)
print(end-start)
day_list = ["Pirm","Otr", "Trešdiena", "Cet", "P", "S", "Sv"]
print(start.day, start.weekday(), day_list[start.weekday()], start.hour, start.minute, start.second)


