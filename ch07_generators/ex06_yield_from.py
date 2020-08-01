def naive_chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

def chain(*iterables):
    for it in iterables:
        yield from it
