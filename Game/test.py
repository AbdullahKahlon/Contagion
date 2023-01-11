import datetime
  
# For using listdir()
import os

amount = 12


for i in range(amount+1):
    date = datetime.date.today() + datetime.timedelta(days=i)
    print(date)