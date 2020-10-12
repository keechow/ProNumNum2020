"""
File: 4D_num.py
Objective: Construct a class that contains all the numbers to be used in analysis
Methods: get_all_num() : returns 0000

"""

#0000 - 9999
#
class Numbers:
    all_num = []
    list_1 = []  # list containing numbers with no repeating digit
    list_2 = []  # list containing numbers with 2 repeating digits
    list_3 = []  # list containing numbers with 3 repeating digits
    list_4 = []  # list containing numbers with 4 repeating digits
    list_double = []  # list containing numbers with 2 pairs of digits
    clean_list_2 = []  # list_2 with overlapping elements from list_double removed

    def __init__(self):
        self.gen_all_num()
        self.separate_num()

    def gen_all_num(self):
        for each in range(10000):
            str_each = str(each)
            while len(str_each) < 4:
                str_each = "0" + str_each
            self.all_num.append(str_each)

# calculate how many times a a digit is repeated in a number
    def calc_occurence(self, str_num):
        check_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        occurence = 1
        for each in check_digit:
            count = str_num.count(each)
            if count > occurence:
                occurence = count
        return occurence

# check if given number is  double-double
    def check_double_double(self, str_num):
        check_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for each in check_digit:
            count = str_num.count(each)
            if count == 2:
                for num in check_digit:
                    count2 = str_num.count(num)
                    if count2 == 2 and num != each:
                        return True
        return False

# run gen_num() and separate num into respective num categorie
    def separate_num(self):
        num_list = self.all_num
        for each in num_list:
            occur = self.calc_occurence(each)
            if occur == 1:
               self.list_1.append(each)
            elif occur == 2:
                self.list_2.append(each)
            elif occur == 3:
                self.list_3.append(each)
            else:
                self.list_4.append(each)

        for each in self.list_2:
            if self.check_double_double(each):
                self.list_double.append(each)

        # there are same number in list_2 and list_double. we want to remove these numbers from list_2
        set_list2 = set(self.list_2)
        set_list_double = set(self.list_double)
        self.clean_list_2 = list(set_list2.difference(set_list_double))

    def get_all_num(self):
        return self.all_num

    def get_i24(self):
        return self.list_1

    def get_i12(self):
        return self.list_2

    def get_i8(self):
        return self.list_3

    def get_i12_double(self):
        return self.list_double

    def get_i12_clean(self):
        return self.clean_list_2




