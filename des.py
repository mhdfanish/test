


def func(raise_error):
    if raise_error:
        raise Exception

    for i in range(10):
        yield i

func(True)