import sub

from time import sleep

dt = .1

app = sub.Window()
app.thread()
while True:
    print('main')
    sleep(dt)