"""
File: 4D_num.py
Objective: Construct a class that contains all the numbers to be used in analysis
Methods: get_all_num() : returns 0000

"""

#0000 - 9999
#
class Numbers:
    all_num = []
    def __init__(self):
        for each in range(10000):
            str_each = str(each)
            while len(str_each) < 4:
                str_each = "0" + str_each
            self.all_num.append(str_each)
    def get_all_num(self):
        return self.all_num


my_num = Numbers()

print(my_num.get_num())