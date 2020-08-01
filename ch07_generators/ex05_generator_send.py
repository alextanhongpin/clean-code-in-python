def sequence():
    num = 0
    step = 1
    while True:
        step = (yield num) or 1
        num += step
