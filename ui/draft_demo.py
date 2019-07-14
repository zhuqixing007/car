import time
for i in range(10):
    with open('position.txt', 'a') as f:
        f.writelines(str(i)+'\n')
    time.sleep(1)