import time
import LogHandler

big_queues = False
run_every = 60 * 5

def start():
    #TODO: Make sure this runs roughly every 5 minutes
    last_run = 0
    while True:
        # Run every 5 minutes
        LogHandler.log_warning("Checking Queues")
        
        finish_time = time.time()
        LogHandler.log_warning(str(finish_time - last_run))
        if finish_time - last_run > run_every:
            LogHandler.log_warning("Queues Getting too big to handle")
            big_queues = True
        else:
            big_queues = False
        sleep_length = time.time() % run_every
        LogHandler.log_warning(str(time.time()) + "/" + str(time.time()%run_every) +  " Sleeping For: " + str(sleep_length))
        time.sleep(sleep_length)
        last_run = time.time()

def health():
    pass

class QueueManager:
    
    pass

