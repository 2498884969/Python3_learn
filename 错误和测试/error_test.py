# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError', e)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError', e)
# except ZeroDivisionError as e:
#     print('except:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

# def foo(s):
#     return 10 / int(s)
#
# try:
#     foo()
# except ValueError as e:
#     print('Valueerror')
# except UnicodeError as e:
#     print('UnicodeError')


# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error', e)
#     finally:
#         print('finally...')
#
#
# main()

# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     bar('0')
#
#
# main()

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')
