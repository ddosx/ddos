mkdir ~/tmp
chmod +x mkarchiso
sudo ./mkarchiso  -v -w ~/tmp -o ./release ./os
sudo rm -Rf ~/tmp
