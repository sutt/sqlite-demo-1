import time
import string
import random
import hashlib

'''
    The producer file, this will create and append to the queue.txt file
    Adjust the settings below to change the difficulty of the hash
'''

COUNTER_PRINT_INTERVAL = 1_000_000
DIFFICULTY = 5
QUEUE_FN = 'queue.txt'


def hash_msg(msg='coding everyday is fun'):
    nonce_list = random.sample(string.ascii_lowercase, 10)
    nonce = ''.join(nonce_list)
    nonce + msg
    b_nonce_msg = bytes(nonce + msg, 'utf-8')
    output = hashlib.sha256(b_nonce_msg).hexdigest()
    return output, nonce


counter = 0

while True:
    
    counter += 1
    
    output, nonce = hash_msg()
    
    if output.startswith('0' * DIFFICULTY):
    
        # append to file
        # we write ~1 line/second, depending on cpu speed
        with open(QUEUE_FN, 'a') as f:
            f.write(f'{counter},{nonce},{output}\n')

        print('FOUND ONE! ', counter, '\n', output[:10], nonce, '\n')

    if counter % COUNTER_PRINT_INTERVAL == 0:
        print('interval ', counter, '\n', output[:10], nonce, '\n')
        
