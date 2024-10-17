

def read_file_yield(filename):
    with open(filename, "r") as f:
        while True:
            line = f.readline()     # not readlines not to load the whole file, just one line
            if not line:
                break
            yield line 
gen = read_file_yield("data.txt")  # the doc is in his gitub but it's too big (100MB)
next(gen)


def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        
    return lines