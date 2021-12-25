echo 'nvidia' >> os/packages.x86_64
echo 'nvidia-utils' >> os/packages.x86_64
mkdir ~/tmp
sudo mkarchiso  -v -w ~/tmp -o ./release ./os
sudo rm -R ~/tmp