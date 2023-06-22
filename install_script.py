import os

# Путь установки приложения
while True:
    install_path = input("Ведите путь для установки приложения: ")
    if os.path.exists(install_path) \
            or install_path == "":
        break
    print("Эта директория не существует.")

# Создание ярлыка на рабочем столе
while True:
    answer = input("Создать ярлык на рабочем столе? (y/n) ")
    if answer == "y":
        create_desktop_icon = True
        break
    elif answer in ["n", ""]:
        create_desktop_icon = False
        break
    else:
        print("Невалидный ответ.")

os.system("sh install.sh " + install_path + " " + str(create_desktop_icon))
