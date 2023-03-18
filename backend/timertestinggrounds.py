import time
timer = time.time() +3

while(True):

    if(time.time()>=timer):
        print(timer)
        timer = time.time() +3
