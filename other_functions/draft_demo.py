import time
for i in range(10):
    with open('test.txt', 'a') as f:
        f.writelines('ergdfgsdg\n')
    time.sleep(1)