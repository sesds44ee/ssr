from owns import send_shell
import time

l = ['ku.py', 'su.py']

while True:
    for i in l:
        send_shell('python3', i)

    time.sleep(3)