import os
import sys
import command_execute as cm
args = sys.argv


if len(sys.argv) == 9:
    # apps
    firefox = bool(sys.argv[1])
    konsole = bool(sys.argv[2])
    pamac = bool(sys.argv[3])
    yay = bool(sys.argv[4])
    libreoffice = bool(sys.argv[5])
    mountX = str(sys.argv[6])
    archrepo = bool(sys.argv[7])
    de = str(sys.argv[8])
    if yay:
        if archrepo:
            cm.comexx('pacman -Sy yay',mountX)
        else:
            print('yay --> error')
    if pamac:
        print('pamac --> error')
    if firefox:
        cm.comexx('pacman -Sy firefox',mountX)
    if konsole:
        if de == 'plasma':
            cm.comexx('pacman -Sy konsole',mountX)
    else:
        cm.comexx('pacman -Sy gnome-terminal',mountX)
    if libreoffice:
        cm.comexx('pacman -Sy libreoffice-fresh libreoffice-fresh-ru',mountX)
else:
    print(len(args),args)

    print('Ошибка в аргументах')
    print('1 - firefox')
    print('2 - konsole')
    print('3 - pamac')
    print('4 - yay')
    print('5 - libreoffice')
    print('6 - точка монтирования')
    print('7 - установлен archrepo?')
