import threading
from play import next_match

e = threading.Event()
def set_interval(_func, _time):
    while not e.wait(_time):
        _func()
            
set_interval(next_match, 1)
