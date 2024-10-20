from time import  time, sleep

def measure(func):
    def wrapper(*args, **kwargs):
        t = time()   # additional code
        res = func(*args, **kwargs)    # here will be function make_db_backup
        print(func.__name__, "took", time() - t)  # additional code
        return res # so the decorator will also show the result of the function (in this case make_db_backup)

    return wrapper

@measure
def make_db_backup():
    sleep(5)

make_db_backup()