def check_narcissistic_num(num):

    num_string_list = [x for x in str(num)]
    num_powers_list = [int(x) ** len(num_string_list) for x in str(num)]
    sum_value = 0
    for i in num_powers_list:
        sum_value += i
    print(num, sum_value, sum_value == num)
    return sum_value == num
