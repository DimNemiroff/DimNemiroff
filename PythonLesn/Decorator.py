import time
import 

def test_time(func):
    def full_control(*first, **second):
        at = time.time()
        res = func(*first, **second)
        et = time.time()
        print(f"Time {et - at} s")
        return res

    return full_control


@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


# get_nod = test_time(get_nod)
# fast_nod = test_time(fast_nod)

res = get_nod(13, 187000000)
res2 = fast_nod(13, 187000000)
print(res, res2)

# fast_nod
