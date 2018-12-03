from IMF import IMF
import SETTINGS


# Авторизация
run = IMF(
    SETTINGS.USERNAME,
    SETTINGS.PASSWORD
)

# Назначение файла логов
run.logsfile = SETTINGS.LOGSFILE

# Установка донеров (получение их id)
run.setDonors(
    SETTINGS.DONERS
)

# Запуск цикла подписка отписка
run.start_loop(
    mode=SETTINGS.MODE,
    count=SETTINGS.COUNT,
    delay=SETTINGS.DELAY
)

# Подписка на заданное количество пользователей
# run.start_follow(
#     count=SETTINGS.COUNT,
#     delay=SETTINGS.DELAY
# )

# Отписка от заданного количества пользователей
# run.start_unfollow(
#     count=SETTINGS.COUNT,
#     delay=SETTINGS.DELAY
# )