#!/usr/bin/python3
""" Module for UTF8_data class """


class Unicode:
    """ Unicode class """
    def validUTF8(data_set):
        """ A function to validate if a data set is a valid utf-8 format """
        for elem in data_set:
            if elem > 255 or elem < 0:
                return False
            return True
