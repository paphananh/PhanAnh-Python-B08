
import datetime
import pyglet
#
# x = datetime.datetime.now()
# print (x.hour, x.minute, x.second)
while True:
    x = datetime.datetime.now()
    print (x.hour, x.minute, x.second)
    if(x.hour == 20 and  x.minute == 32 and x.second == 00):
        music = pyglet.resource.media("cello.wav")
        music.play()
        pyglet.app.run()
