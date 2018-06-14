#Calculate how many digits is in the number of seconds in the year
#A common year is taken as a base

def seconds_in_year():
    seconds = 365 * 24 * 60 * 60
    return len(str(seconds))
