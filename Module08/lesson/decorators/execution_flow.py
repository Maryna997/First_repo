from time import sleep


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)

    return inner

@star
@percent
def make_db_backup():
    print("I'm working")
    sleep(5)

make_db_backup()
