import random
import time

random.seed(time.time())

a = []

for i in range(10):
    a.append(random.randint(1,10))


start_time = time.time()

print("---- {} seconds ----".format(time.time() - start_time))






