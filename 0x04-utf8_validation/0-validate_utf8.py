#!/usr/bin/python3
""" Module for UTF8_data class """


def validUTF8(data_set):
    """ A function to validate if a data set is a valid utf-8 format """
    if data_set[0] > 127:
        return False
    for elem in data_set:
        # print(elem)
        if elem > 255 or elem < 0:
            return False
    return True
