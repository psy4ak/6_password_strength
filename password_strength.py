import re


def get_password_strength(password):
    pass_strength = None
    if len(password) < 6:
        pass_strength = 'Слишком короткий пароль!'
    else:
        pass_strength = 0
        if re.search('(password)|(qwe)|(123)', password) and len(password) < 8:
            pass_strength -= 3
        if bool(re.search('\d', password)):
            pass_strength += 1
        if bool(re.search('[A-Z]', password)):
            pass_strength += 1
        if bool(re.search('[a-z]', password)):
            pass_strength += 1
        if bool(re.search('[\W_]', password)):
            pass_strength += 2
        if 6 < len(password) <= 8:
            pass_strength += 1
        if 9 <= len(password) <= 11:
            pass_strength += 2
        if 12 <= len(password) <= 20:
            pass_strength += 2
        if len(password) > 20:
            pass_strength = 10
        if pass_strength < 0:
            pass_strength = 0
    return pass_strength


if __name__ == '__main__':
    while True:
        get_password = input('Введите пароль(не менее 6 символов):')
        print('Сложность пароля (0-10):', get_password_strength(get_password))
