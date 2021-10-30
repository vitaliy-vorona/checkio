# return boolean if parameter value is equal to sum of powers of each int

def check_narcissistic_num(num):
    nums_powered_list = [int(x) ** len(str(num)) for x in str(num)]
    return sum(nums_powered_list) == num
