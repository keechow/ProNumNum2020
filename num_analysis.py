"""
Project Num Num 2020
Name: num_analysis.py
Objective:  1. Generate numbers from 0000 to 9999
            2. Separate each number to different category - i24, i12, i6, i4
            3. Allow user to get a list of these numbers
Params: None
Return: None
Author: Project Echo Telion <echo.telion@gmail.com>

"""
#generate a string list containing element 0001 to 9999
def gen_num():
    num = 0
    str_num_list = []
    for each in range(10000):
        each_str = str(each)
        while len(each_str) < 4:
            each_str = "0" + each_str
        str_num_list.append(each_str)
    return str_num_list

#calculate how many times a a digit is repeated in a number
def calc_occurence(str_num):
    check_digit = ['0','1','2','3','4','5','6','7','8','9']
    occurence = 1
    for each in check_digit:
        count = str_num.count(each)
        if count > occurence:
            occurence = count
    return occurence

#check if given number is  double-double
def check_double_double(str_num):
    check_digit = ['0','1','2','3','4','5','6','7','8','9']
    for each in check_digit:
        count = str_num.count(each)
        if count == 2:
            for num in check_digit:
                count2 = str_num.count(num)
                if count2 == 2 and num != each:
                    return True
    return False

#return a list of i24 num in str
def get_i24():
    # return list of number with no repeating digit
    r_list = []
    for each in gen_num():
        if calc_occurence(each) == 1:
            r_list.append(each)
    return r_list

#return a list of i12 num in str
def get_i12():
    # return list of number with 2 repeating digits
    r_list = []
    for each in gen_num():
        if calc_occurence(each) == 2:
            r_list.append(each)
    return r_list

#return a list of i8 num in str
def get_i8():
    # return list of number with 3 repeating digits
    r_list = []
    for each in gen_num():
        if calc_occurence(each) == 3:
            r_list.append(each)
    return r_list

#return a list of double-double num in str
def get_double():
    # return list of number with 2 repeating digits
    r_list = []
    for each in gen_num():
        if calc_occurence(each) == 2 and check_double_double(each):
            r_list.append(each)
    return r_list

#return a list of i4 num in str
def get_i4():
    # return list of number with 4 repeating digits
    r_list = []
    for each in gen_num():
        if calc_occurence(each) == 4:
            r_list.append(each)
    return r_list

#return a list of i12 without double-double num in str
def get_i12_no_double():
    set_i12 = set(get_i12())
    set_double = set(get_double())
    i12_no_double = list(set_i12.difference(set_double))
    return i12_no_double

def check_num_cat(num_str):
    #return the num cat for given num
    #24 or 12 or 6 or 4
    occur = calc_occurence(num_str)

    if occur == 1:
        return 24
    elif occur == 2:
        if check_double_double(num_str):
            return 22
        else:
            return 12
    elif occur == 3:
        return 8
    else:
        return 4

def check_num_range(num_str):
    return int(num_str[0])

def check_num_sum(num_str):
    total_sum = 0
    for digit in num_str:
        digit_int = int(digit)
        total_sum += digit_int
    return total_sum


    
###################################
#Below are codes use during testing#
###################################
