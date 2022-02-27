import os
import sys
import command_execute as cm
args = sys.argv

# base
if len(args) == 8:
    kernel = str(sys.argv[1]) #
    bootloader = str(sys.argv[2] )
    mountX = str(sys.argv[3]) #
    hostnameX = str(sys.argv[4]) #
    timedateX = str(sys.argv[5]) #
    userX = str(sys.argv[6] ) #
    archrepo = bool(sys.argv[7]) #
    lang = 'Russian' #
    print('Установка OS')
    cm.comex('pacstrap '+(mountX)+' base base-devel '+(kernel)+' linux-firmware btrfs-progs')
    cm.comex('genfstab -U '+(mountX)+' >> '+(mountX)+'/etc/fstab')
    cm.comexx('ln -sf /usr/share/zoneinfo/'+(timedateX)+' /etc/localtime',mountX)
    cm.comexx("hwclock --systohc",mountX)
    cm.comex('echo "en_US.UTF-8 UTF-8" >> '+(mountX)+'/etc/locale.gen')
    cm.comexx("locale-gen",mountX)
    if lang == 'Russian':
        cm.comex('echo "LANG=ru_RU.UTF-8" >> '+(mountX)+'/etc/locale.conf')
    else:
        cm.comex('echo "LANG=en_US.UTF-8" >> '+(mountX)+'/etc/locale.conf')
    cm.comexx("pacman -S NetworkManager && systemctl enable NetworkManager",mountX)
    cm.comex('echo "FONT=cyr-sun16" >> '+(mountX)+'/etc/vconsole.conf')
    cm.comex('echo "'+(hostnameX)+'" > '+(mountX)+'/etc/hostname')
    cm.comex('echo "127.0.0.1 localhost" > '+mountX+'/etc/hosts')
    if archrepo:
        cm.comex('echo "[archrepo]" >> '+(mountX)+'/etc/pacman.conf')
        cm.comex('echo "SigLevel = Optional TrustAll" >> '+(mountX)+'/etc/pacman.conf')
        cm.comex('echo "Server = https://barsnet.github.io/$repo/$arch" >> '+(mountX)+'/etc/pacman.conf')
        cm.comexx('pacman -Sy',mountX)
    cm.comex("rm -R {}/etc/skel".format(mountX))
    cm.comex("cp /etc/skel /{}/etc/skel".format(mountX))
    cm.comex("mkdir {}/home/{}/".format(mountX,userX))
    cm.comexx("useradd {} -d /home/{}".format(userX,userX),mountX)
    cm.comex("clear")
    cm.comexx("usermod -aG whell {}",mountX)
    cm.comexx("chown {}:{} -r".format(userX,userX),mountX)
    cm.comex("cp -r /etc/skel/* {}/home/{}/".format(userX,mountX,userX))
    cm.comexx("passwd {}".format(userX),mountX)
    if bootloader == 'refind':
        cm.comexx("pacman -S refind efibootmgr",mountX)
        cm.comexx("refind-install",mountX)
    elif bootloader == 'grub2':
        cm.comexx("pacman -S grub2 efibootmgr",mountX)
        cm.comexx("grub-install && grub-mkconfig -o /boot/grub/grub.cfg",mountX)
    else:
        print("Устанавливайте сами, {}".format(mountX))
        os.system("konsole")
else:
    print(len(args),args)

    print('Аргументы - :')
    print('1 - Ядро (linux-lqx,linux-zen,linux-clear,linux)')
    print('2 - Загрузчик (refind,grub2)')
    print('3 - Точка монтирования ')
    print('4 - Хостнаме')
    print('5 - Регион часов (Europe/Moscow)')
    print('6 - Имя пользователя (dydouser)')
    print('7 - Кастомный репозитоий (True/False)')