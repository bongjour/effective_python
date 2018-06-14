def safe_division(number, divisor, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    """

    :param number:
    :param divisor:
    :param ignore_overflow:
    :param ignore_zero_division:
    :return:
    """
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise

    except ZeroDivisionError:
        if ignore_zero_division:
            return 0
        else:
            raise


print(safe_division(1, 0, ignore_overflow=True, ignore_zero_division=True))


# for python 2.x
def safe_division_ver2(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_division = kwargs.pop('ignore_zero_division', False)

    # if kwargs:
    #     raise TypeError('Unexpected **kwargs: %r' % kwargs)

    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return 0
        raise


result = safe_division_ver2(1, 0, ignore_zero_division=True)
try:
    result = safe_division_ver2(1, 0)
except ZeroDivisionError:
    pass

print(result)

result = safe_division_ver2(1, 0, unexpected=True)
