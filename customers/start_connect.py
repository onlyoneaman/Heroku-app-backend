import time
import datetime

def start_connection_api(server, value):
    time_start = datetime.datetime.now()
    time.sleep(1)
    time_end = datetime.datetime.now()
    time_diff = time_end - time_start
    res = time_diff / datetime.timedelta(milliseconds=1)
    print(time_start,time_end,time_diff)
    return(res)