import time
import sys

'''
    The consumer file, this will read from the queue.txt file in a loop
    
    This solution relies on looking at differences in the file each time it checks.
    Would this scale over time?

'''

POLL_INTERVAL = 2
POLL_COUNTER_PRINT_INTERVAL = 10
QUEUE_FN = 'queue.txt'
LOG_ERR = True
LOG_WARN = True
LOG_NOISY = False

# startup, if we can't read the file, exit
try:
    with open(QUEUE_FN, 'r') as f:
        lines = f.readlines()
    num_events = len(lines)
    print('Found', num_events, 'existing events in queue.txt')
except Exception as e:
    print('Error in startup(), exiting:', e)
    sys.exit(1)


# main loop
counter = 0
while True:
    
    counter += 1
    
    time.sleep(POLL_INTERVAL)
    
    try:
        
        with open(QUEUE_FN, 'r') as f:
            lines = f.readlines()
            _num_events = len(lines)
        
        if _num_events > num_events:
            
            num_new_events = _num_events - num_events
            new_events = lines[-num_new_events:]
            
            # two.py has received new messages from one.py
            # here we're just going to print it out
            # but you could do something else, like:
            # send a registration confirmation email
            # tell a driver to go pick up a passenger
            print('====FOUND', num_new_events, 'new events')
            for event in new_events:
                print(event)

            num_events = _num_events
        
        elif _num_events < num_events:
            if LOG_WARN: print('WARNING: queue.txt has fewer events than before')

        else:
            if LOG_NOISY: print('No new events')

    except Exception as e:
        if LOG_ERR: print('Error reading queue.txt:', e)

    if counter % POLL_COUNTER_PRINT_INTERVAL == 0:
        print('\nPolling interval', counter)
