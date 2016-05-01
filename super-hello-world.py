#-*- coding: utf8 -*-
import time

class Mail():
    """
    This class is very useful to display text messages !
    """
    def __init__(self, message, sender='Unknown', time=time.time()):
        self.message = message
        self.sender  = sender
        self.time    = time

    def __str__(self):
        str_args = (self.sender, 1000000*(time.time()-self.time), self.message)
        return 'Message from %s received %0.6f nano-seconds ago :%s'%str_args



if __name__ == '__main__':

    ### Message, sender and date informations.
    date    = time.time()
    text    = 'Hello, world !'
    name    = 'Leonard'
    message = Mail(text, sender=name, time=date)

    ### Display the message several times, just in case.
    times   = 10
    for _ in xrange(times):
        print message
