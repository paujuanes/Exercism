def is_armstrong_number(number):
    strNum = str(number)
    digitSum = 0
    for i in range(len(strNum)):
        digit = int(strNum[i])**len(strNum)
        digitSum += digit
    return number == digitSum