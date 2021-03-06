import gevent
from gevent import monkey
import time

monkey.patch_all()

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)

# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
gevent.joinall([
    gevent.spawn(f, 5),
    gevent.spawn(f, 5),
    gevent.spawn(f, 5)
])

# g1.join()
# g2.join()
# g3.join()