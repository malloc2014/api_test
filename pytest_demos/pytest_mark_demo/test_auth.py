import time
def test_timer1():
    t1 = time.time()
    print(t1)
    assert t1 >= 0
