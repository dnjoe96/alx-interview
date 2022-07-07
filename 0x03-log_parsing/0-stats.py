#!/usr/bin/env python3
""" Script to read logs"""
from signal import signal, SIGINT
import sys


class Log:
    """ Log class"""
    count = 0
    sum = 0
    status_code = {}
    code_choice = [200, 301, 400, 401, 403, 404, 405, 500]

    def process() -> None:
        """ Processes the log data"""
        # print(status_code)
        print(f"File size: {Log.sum}")
        for code in Log.code_choice:
            if code in Log.status_code.keys():
                print(f'{code}: {Log.status_code.get(code)}')
        Log.count = 0
        Log.sum = 0
        Log.status_code = {}
        return None


def handler(signal_received, frame) -> None:
    """ SIGINT handler function """
    # signal(SIGINT, handler)
    Log.process()
    return None


if __name__ == '__main__':
    signal(SIGINT, handler)

    for line in sys.stdin:

        str_code = line.split(" ")[-2]
        # print(str_code)
        if str_code.isdigit():
            code = int(line.split(" ")[-2])
        else:
            continue

        if code not in Log.status_code.keys():
            Log.status_code[code] = 1
        else:
            Log.status_code[code] += 1

        # print(Log.status_code)
        try:
            size = int(line.split(" ")[-1])
            Log.sum += size
        except Exception as e:
            print(f"Error - {e}")

        Log.count += 1
        if Log.count == 10:
            Log.process()
