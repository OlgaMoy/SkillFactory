# import redis  # импортируем библиотеку
#
# red = redis.Redis(
#     host=redis-11236.c1.asia-northeast1-1.gce.cloud.redislabs.com,
#     # ваш хост, если вы поставили Redis к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
#     port=11236,
#     # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегд разный, по этому его надо копировать оттуда же, что и host.
#     password=Q491ifaZjw7RVXQonLcu8yMmbGNcwjrn
#     # для локальной машины пароль не требуется (если вы устанавливали Redis к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password.
# )

import redis
import json

red = redis.Redis(
    host='redis-11236.c1.asia-northeast1-1.gce.cloud.redislabs.com',
    port=11236,
    password='Q491ifaZjw7RVXQonLcu8yMmbGNcwjrn')

red.delete('dict1') # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))