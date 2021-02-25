import threading
from play import next_match

def set_interval(_func, _time):
    e = threading.Event()
    while not e.wait(_time):
        _func()
            
set_interval(next_match, 5)
