import time
# import string
# import random
# import sqlite3
# import os
# import sys

# counter = 1_000_000
while True:
    # counter += 1
    # print(counter)
    time.sleep(0.5)
    with open('one.txt', 'r') as f:
        try:
            counter = int(f.read())
        except Exception as e:
            print(e)
            counter = None
    print(counter)
