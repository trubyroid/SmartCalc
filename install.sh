!/usr/bin/env bash

desktop_icon_path="$HOME/Desktop/SmartCalc.app"

install_path = $1
create_desktop_icon = $2

desktop_path = "$HOME/Desktop/"

 # Установка приложения
 cp -R "$PWD/dist/SmartCalc.app" "$install_path"

 # Создание ярлыка на рабочем столе (если необходимо)
 if [ "$create_desktop_icon" = true ]; then
     ln -s "$install_path" "$desktop_path"
 fi