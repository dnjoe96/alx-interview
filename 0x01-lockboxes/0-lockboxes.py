#!/usr/bin/python3

def canUnlockAll(boxes):
  all = []
  count = 0
  for one in boxes:
    if len(one) == 0:
      all = all + [0]
    all = all + one
    count += 1

  print(all)
  if count - 1 not in all:
    return False
  return True

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))