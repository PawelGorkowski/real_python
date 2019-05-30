def funcs(operator, x, y):
    return{
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }.get(operator, None)()
    # }.get(operator, lambda: None)()


# if __name__ == '__main__':
#     print(funcs('add', 1, 2))

calcs = {'add': lambda x, y: x + y,
         'sub': lambda x, y: x - y,
         'mul': lambda x, y: x * y,
         'div': lambda x, y: x / y}


def funcs_2(operator, x, y):
    return calcs.get(operator, None)(x, y)


# if __name__ == '__main__':
#     print(funcs_2('divs', 10, 2))


def lm_click(x=1):
    print(f'Left mouse button clicked {x} time(s)')


def rm_click(x=1):
    print(f'Right mouse button clicked {x} time(s)')


def cm_click(x=1):
    print(f'Center mouse button clicked {x} time(s)')


clicks = {
    'lm': lm_click,
    'rm': rm_click,
    'cm': cm_click
}


def m_click(button, times):
    return clicks.get(button, None)(times)


if __name__ == '__main__':
    try:
        print(m_click('rm', 21))
    except (TypeError, ZeroDivisionError):
        print('No such button on the mouse.')
    else:
        print('No exceptions raised.')
    # finally:
    #     print('This always prints in m_click() method.')
