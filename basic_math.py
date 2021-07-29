#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """
    greatest_number = -999999
    for value_greatest in number_list:
        if value_greatest > greatest_number:
            greatest_number = value_greatest
    return greatest_number


def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """
    smallest_number = 999999
    for value_greatest in number_list:
        if value_greatest < smallest_number:
            smallest_number = value_greatest
    return smallest_number


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    mean = 0
    value_number = 0
    for i in number_list:
        value_number += i
        # print("value_numer = ", value_number)
    else:
        mean = value_number/len(number_list)
        # print(len(number_list))
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    median = 0
    compare_value = 0
    if len(number_list)%2 == 0:
        for i in range(0,len(number_list)):
            compare_value = number_list[i]
            for j in range(0,len(number_list)):
                if j+i > len(number_list)-1:
                    break
                elif number_list[i] > number_list[j+i]:
                    number_list[i] = number_list[j+i]
                    number_list[j+i] = compare_value
                    compare_value = number_list[i]
                    # print(f"number_list : {number_list} i = {i}, j = {j}")

        else:
            median = (number_list[int(len(number_list)/2)]+number_list[int(len(number_list)/2-1)])/2
    else:
        for i in range(0,len(number_list)):
            compare_value = number_list[i]
            for j in range(0,len(number_list)):
                if j+i > len(number_list)-1:
                    break
                elif number_list[i] > number_list[j+i]:
                    
                    number_list[i] = number_list[j+i]
                    number_list[j+i] = compare_value
                    compare_value = number_list[i]
                    # print(f"number_list : {number_list} i = {i}, j = {j}")
        else:
            median = number_list[int(len(number_list)/2)]
    return median
