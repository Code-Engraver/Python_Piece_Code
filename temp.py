# focus \r
import time
# def show_Remaining_Time(time_delta):
#     print('Time Remaining: %d'%time_delta, end='\r', flush=False)

def show_Remaining_Time(time_delta):
    print('\r', end='')
    print('Time Remaining: %d'%time_delta, end='', flush=False)

count = 0
while True:
    show_Remaining_Time(count)
    count += 1
    time.sleep(1)
