def is_number(value):
    try:
        # print("Es válido")
        int(value)
        return True

    except Exception as e:
        # print(e)
        # print("No es válido")
        return False


def int_in_range(number, start, end):
    if number >= start and number <= end:
        return True
    else:
        return False
