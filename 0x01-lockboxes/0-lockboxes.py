#!/usr/bin/python3
""" Module containing function to solve the lockboxes problem """


def canUnlockAll(boxes):
    """

    The lock checker function

    @arg: list - list of list representing list of boxes
    return: Bool -  True or False
    """

    all = []
    count = 0

    for box in boxes:
        if len(box) == 0 and box is not boxes[-1]:
            return False

        all = all + box
        count += 1

    if count - 1 not in all:
        return False
    return True
