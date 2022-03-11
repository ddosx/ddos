# ddos - современная ос
<!-- preimushestva list -->
## Преимущества
#### Скорость
Благодаря пакетному менеджеру pacman система работает быстро и стабильно (unstable означает, что версия *развивается*, а не вылетает каждые 5 секунд). 
А ещё ddOS запускается быстрее, чем Debian 9, Ubuntu, Fedora и openSUSE.
#### Простота
Система уже преднастроена и готова к использованию (установщика нет!)
А зачем установщик, если можно запускать систему из раздела внутреннего диска?
#### Чистота
На ddOS не установленны программы, которыми вы не пользуетесь.
Но вы сможете всегда их установить с помощью pacman.
## Как собрать
#### система собирается под ``archlinux``
#### зависимости — ``archiso``
1. С помощью ``neofetch`` гляньте *производителя* видеокарты. Модель неважна. Если производитель ``intel``, ``nvidia`` или ``amd``, то система будет работать.
2. Создайте папку ``release`` относительно файла build.sh или nvidia.sh
3. Если производитель видеокарты ``nvidia``, то запустите файл ``nvidia.sh``.
Если у вас видеокарта ``amd``/``intel``, запустите  ``build.sh``.
4. Когда .sh прогрузится в ``release/``, появится файл c названием ``ddos-V$V beta/aplha/pre-release/stable/unstable-$arch.iso``
где $V - версия, beta/aplha/pre-release/stable/unstable - состояние версии (см Релизы ), $arch - архитектура (обычно x86_64)
Пример:
``
ddos-V0.6 beta-x86_64.iso
``

*5. Вот и ваш .iso образ ddOS. Ставьте на флешку или в раздел внутреннего диска и готово!*
*(ахтунг: не ставьте полностью на весь диск, почитайте гайд по разделыванию диска под арч)*
## Как это выглядит:
### plasma,V0.8
![Screenshot_20220311_185218](https://user-images.githubusercontent.com/61107330/157901624-d5495e3e-9489-4088-8468-55cfb351febd.png)
![Screenshot_20220311_185317](https://user-images.githubusercontent.com/61107330/157901787-b35d4a76-34cc-4aa6-83e9-c591036e63ea.png)
![Screenshot_20220311_190123](https://user-images.githubusercontent.com/61107330/157903259-0d7c03e2-941f-4f9b-bbb4-a38ef99ee548.png)
![Screenshot_20220311_190331](https://user-images.githubusercontent.com/61107330/157903621-3253e2ab-beee-48d1-a03e-e71a6bb8201c.png)
![Screenshot_20220311_190443](https://user-images.githubusercontent.com/61107330/157903869-82c53238-a0c1-4035-9192-517a54a1783d.png)
![Screenshot_20220311_190900](https://user-images.githubusercontent.com/61107330/157904603-b23aca67-3189-4a5f-a38a-2c67695e3848.png)
![Screenshot_20220311_191306](https://user-images.githubusercontent.com/61107330/157905309-9be30b9e-a6d2-4839-aec4-a4cc7ad78ed5.png)
![Screenshot_20220311_193551](https://user-images.githubusercontent.com/61107330/157909058-8fd49c81-324a-4114-8f0d-add8efb54e93.png)
### gnome,V0.5
![login](https://user-images.githubusercontent.com/61107330/147656439-af642cd4-c505-4279-b5b5-6f101dea0d27.png)
![osafterlogin](https://user-images.githubusercontent.com/61107330/147656499-63ef6e9e-9fc1-408f-aecf-50d55a5405fb.png)
![desktop](https://user-images.githubusercontent.com/61107330/147656541-c123457f-3b72-4667-b753-a13ce6f023ac.png)
![appmenu](https://user-images.githubusercontent.com/61107330/147390074-6befb1e9-98e3-4667-969c-f9eb90534fe1.png)
![defaultsettings](https://user-images.githubusercontent.com/61107330/147656585-989ef5ea-6b6a-4f64-a22a-f892ea78cfa8.png)
![lockscreen_meta+l](https://user-images.githubusercontent.com/61107330/147390119-abe920ac-1c38-4368-9947-464ac0792771.png)
![multitasking](https://user-images.githubusercontent.com/61107330/147656815-61999bd4-4389-45e6-ac98-87d66cb21bde.png)
![multitasking2](https://user-images.githubusercontent.com/61107330/147390514-55986025-d1f3-45c7-a91d-dd7a659e59fc.png)
![multitasking3](https://user-images.githubusercontent.com/61107330/147390093-6ea7d82b-367b-4da5-b4ca-b1261cb966fd.png)
## Релизы
V0.1 aplha - чистый archiso

V0.2 alpha - archiso с gnome
добавлены gnome, gpudrivers(intel,amd)
добавлено и включено gdm,networkmanager

V0.3 aplha - первый полный релиз ddOS
добвлен пользователь, обои, консольная утилита ddos_conf

V0.4 aplha - поддержка видеокарт nvidia

V0.5 beta - очищена от мусора

V0.6 beta - uefi только, чтобы загрузится с bios пересобирайте; багфикс

V0.7 pre-release - plasma

V0.8 pre-release - добавлен installer, он не работает

V0.9 pre-release - installer, наверное. Может дефолтный ``archinstall``

V1.0 stable

V1.1 unstable

V1.2 stable

V1.3 unstable

V1.4 stable

V1.5 unstable

V1.6 stable

V1.7 unstable

V1.8 stable

V1.9 unstable

V2.0 stable
