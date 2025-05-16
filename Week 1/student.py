"""
A University of Helsinki student number is a sequence of nine digits. The first digit is 0 and the last digit is a check value that allows checking for typos in the student number.
The check value is obtained by summing up the other digits multiplied by the values 3,7,1,3,7,1,3,7 in the left-to-right order. If the sum is a multiple of 10, the check digit is 0. Otherwise, the check digit is the distance of the sum to the next multiple of 10.
For example, if the student number is 012749139, the sum is 3 \cdot 0 + 7 \cdot 1 + 1 \cdot 2 + 3 \cdot 7 + 7 \cdot 4 + 1 \cdot 9 + 3 \cdot 1 + 7 \cdot 3 = 91. The next multiple of 10 is 100 and the distance to that is 9. Thus the last digit of the student number is 9.
In a file student.py, implement the function check_number that reports if the parameter is a valid student number. The function should return True or False.
Your function will be tested using many different sequences of digits.
"""


def check_number(number):
    result = [int(x) for x in list(number)]
    list_of_digits = [3, 7, 1, 3, 7, 1, 3, 7]

    if len(result) == 9 and result[0]==0:
        for i in range(len(result)-1):
            result[i] *= list_of_digits[i]
        if sum(result) % 10 == 0:
            return True
        else:
            return False
    else:
        return False







if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
    print(check_number("8910231367")) # False
    print(check_number("100000007")) # False