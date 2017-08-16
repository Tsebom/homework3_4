import requests

VERSION = '5.67'
TOKEN = str('ЗДЕСЬ ДОЛЖЕН БЫТЬ ВАШ ТОКЕН')


def method_api(method, params_):
    """
    Реализация метода API вконтакте
    :param method: реализуемый метод
    :param params_: словарь с параматрами
    :return: словарь с результатом
    """
    response = requests.get(
        '/'.join(['https://api.vk.com/method', method]),
        params_
    )
    return response.json()


def list_id(list_):
    """
    Список id друзей
    :param list_: список словарей с данными друзей
    :return: список id
    """
    id_ = list()
    for user in list_:
        id_.append(user['id'])
    return id_


def name_frends(list_):
    """
    Список имен друзей
    :param list_: список словарей с данными друзей
    :return: список имен
    """
    frends = list()
    for name in list_:
        frends.append(' '.join([name['first_name'], name['last_name']]))
    return frends


def main():
    # Словать с параматрами для запроса списка друзей
    my_frends = {
        'fields': 'first_nam, last_name, id',
        'access_token': TOKEN,
        'v': VERSION
    }

    # список словарей с данными друзей
    list_my_frends = method_api('friends.get', my_frends)['response']['items']

    common_frends = set()  # общие друзья

    # друзья друзей
    for friend in list_id(list_my_frends):
        # Словать с параматрами для запроса списка друзей друзей
        params = {
            'user_id': friend,
            'fields': 'first_nam, last_name, id',
            'access_token': TOKEN,
            'v': VERSION
        }

        # Почему ошибка понять не смог. Поэтому этих друзей пропускаем
        # Бонусное умение - "ловец исключений"
        try:
            # список словарей с данными друзей моих друзей
            friend_list = method_api(
                'friends.get', params)['response']['items']
            # список имен друзей моих друзей в множество
            friend_list = set(name_frends(friend_list))
            # пересечение имен моих друзей, и имен друзей моих друзей
            friend_list.intersection_update(set(name_frends(list_my_frends)))
            # добавление в множество общих друзей
            common_frends.update(friend_list)
        except KeyError:
            continue

    print('Общих друзей: {}'.format(len(common_frends)))
    print('\n'.join(list(common_frends)))


main()
