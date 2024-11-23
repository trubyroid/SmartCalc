import os

# Какой путь установки приложения?
while True:
    install_path = input("Insert path to install application: ")
    if os.path.exists(install_path):
        break
    elif install_path == "":
        install_path = "/Applications"
        break
    else:
        print("This directory is not exist.")

# Создать ярлык на рабочем столе?
while True:
    answer = input("Create a desktop shortcut ? (y/n) ")
    if answer == "y":
        create_desktop_icon = True
        break
    elif answer in ["n", ""]:
        create_desktop_icon = False
        break
    else:
        print("Invalid answer.")

# Создание приложения
os.system("python3 setup.py py2app")

# Установка приложения
os.system("cp -R \"$PWD/dist/SmartCalc.app\" " + install_path)
os.system("rm -rf \"$PWD/dist\" \"$PWD/build\"")

print("SmartCalc_v.3 has been installed in " + install_path + "\n")

# Создание ярлыка
if create_desktop_icon:
    os.system("ln -s " + install_path + "/SmartCalc.app \"$HOME/Desktop/\"")