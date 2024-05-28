# class create 
class Survival_cal:

# class method
  def duration_of_survival(self):
    # take input from user 
    age = int(input("What's your age? "))  
    unit = input("Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds. \nNote: You can write the first letter or the full name of the time unit. ").strip().lower()
    
    months = age * 12
    weeks = months * 4
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    if unit == 'months' or unit == 'm':
        print(f'You lived for {months:,} Months')

    elif unit == 'weeks' or unit == 'w':
        print(f'You lived for {weeks:,} Weeks')

    elif unit == 'days' or unit == 'd':
        print(f'You lived for {days:,} Days')

    elif unit == 'hours' or unit == 'h':
        print(f'You lived for {hours:,} Hours')

    elif unit == 'minutes' or unit == 'mi':
        print(f'You lived for {minutes:,} Minutes')

    elif unit == 'seconds' or unit == 's':
        print(f'You lived for {seconds:,} Seconds')

    else:
        print('Your choice is not available')

    return
  
# object create 
s = Survival_cal()
# call to the method of class 
s.duration_of_survival()

print(
    f'''
\n Expected output example:
\n What's your age? 25
\n Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds. 
\n Note: You can write the first letter or the full name of the time unit. d
\n You lived for 9,125 Days
 '''
)
