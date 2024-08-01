def my_range_gen(*args):
    if len(args) == 1:
        stop = args[0]
        start = 0
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    else:
        start = args[0]
        stop = args[1]
        step = args[2]
    while (start < stop and step > 0) or (stop < start and step < 0):
        yield start
        start += step

value = my_range_gen(5)
value1 = my_range_gen(5,10)
value2 = my_range_gen(5,10,2)