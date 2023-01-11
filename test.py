rask = {'ё': 23, 'й': 0, 'q': 0, 'ц': 1, 'w': 1, 'у': 2, 'e': 2, 'к': 3, 'r': 3, 'е': 4, 't': 4, 'н': 5, 'y': 5,
        'г': 6, 'u': 6, 'ш': 7, 'i': 7, 'щ': 8, 'o': 8, 'з': 9, 'p': 9, 'х': 10, 'ъ': 11, 'ф': 12, 'a': 12, 'ы': 13,
        's': 13, 'в': 14, 'd': 14, 'а': 15, 'f': 15, 'п': 16, 'g': 16, 'р': 17, 'h': 17, 'о': 18, 'j': 18, 'л': 19,
        'k': 19, 'д': 20, 'l': 20, 'ж': 21, 'э': 22, 'я': 24, 'z': 24, 'ч': 25, 'x': 25, 'с': 26, 'c': 26, 'м': 27,
        'v': 27, 'и': 28, 'b': 28, 'т': 29, 'n': 29, 'ь': 30, 'm': 30, 'б': 31, 'ю': 32}


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


def check_lng_err(passw):
    if len(passw) <= 8:
        raise LengthError()


def check_dgt_err(passw):
    if not any([str(elem) in passw for elem in [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9]]):
        raise DigitError()


def check_ltt_err(passw):
    if passw.lower() == passw or passw.upper() == passw or passw.isdigit():
        raise LetterError()


def check_sqn_err(passw):
    for i in range(len(passw) - 2):
        if passw[i:i + 3].isalpha():
            lst = [rask[passw[i].lower()], rask[passw[i + 1].lower()], rask[passw[i + 2].lower()]]
            if lst[0] == lst[1] - 1 and lst[2] == lst[1] + 1 and ((12 not in lst or 11 not in lst) and
                                                                  (24 not in lst or 23 not in lst)):
                raise SequenceError()


def check_wrd_err(passw):
    flag = True
    passw = passw.lower()
    for word in words:
        if word in passw:
            flag = False
            break
    if not flag:
        raise WordError()


passwords = open("top 10000 passwd.txt", mode="r")
words = open("top-9999-words.txt", mode="r")
passwords = [elem.rstrip() for elem in passwords]
words = [elem.rstrip() for elem in words]
state = {"DigitError": 0, "LengthError": 0, "LetterError": 0, "SequenceError": 0, "WordError": 0}
for passw in passwords:
    for check in [check_wrd_err, check_dgt_err, check_lng_err, check_ltt_err, check_sqn_err]:
        try:
            check(passw)
        except Exception as ex:
            ans = ex.__class__.__name__
            state[ans] += 1
for elem in state.keys():
    print(elem, "-", state[elem])