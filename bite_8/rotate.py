from collections import deque

def rotate(string, n) -> str:
   """Rotate characters in a string.
   Expects string and n (int) for number of characters to move.
   """
   string_queue = deque(string)
   string_queue.rotate(-n)
   return ''.join(string_queue)
