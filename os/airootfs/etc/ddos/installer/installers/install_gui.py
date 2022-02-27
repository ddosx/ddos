import os
import sys
import command_execute as cm
args = sys.argv

# gui
de = str(sys.argv[1])
lde = str(sys.argv[2])
gpud = str(sys.argv[3])
mountX = str(sys.argv[4])
archrepo = bool(sys.argv[5])
plasmapkgs = [
    'bluedevil',
    'breeze-gtk',
    'drkonqi',
    'kde-gtk-config',
    'kdeplasma-addons',
    'kgamma5',
    'khotkeys',
    'kinfocenter',
    'kscreen',
    'ksshaskpass',
    'kwallet-pam',
    'kwayland-integration',
    'kwrited',
    'oxygen',
    'plasma-browser-integration',
    'plasma-desktop',
    'plasma-disks',
    'plasma-firewall',
    'plasma-nm',
    'plasma-pa',
    'plasma-systemmonitor',
    'plasma-thunderbolt',
    'plasma-vault',
    'plasma-workspace-wallpapers',
    'powerdevil',
    'sddm-kcm',
    'xdg-desktop-portal-kde',
    'kate'
]
gnomepkgs= [
    'gnome',
    'gnome-extra',
    'gnome-control-center',
    'gedit'
]
cinnamon = ['cinnamon','mousepad']
xfce4 = [
    'xfce4',
    'xfce4-goodies',
    'xfce4-xkb-plugin',
    'mousepad']
archpkgs = [
    'layan-kde-git',
    'kvantum',
    'kvantum-theme-layan-git'
]



if gpud == 'atiamd':
    gpudriver = 'xf86-video-amdgpu xf86-video-ati'
if gpud == 'intel':
    gpudriver = 'xf86-video-intel'
if gpud == 'mesa':
    gpudriver = 'mesa'
if gpud == 'nvd':
    gpudriver = 'nvidia nvidia-utils'
if gpud == 'open':
    gpudriver = 'xf86-video-amdgpu xf86-video-ati xf86-video-intel mesa'
    

cm.comexx("pacman -S {}".format(gpudriver),mountX)

if lde == 'sddm':
    cm.comexx("pacman -S sddm && systemctl enable sddm",mountX)
if lde == 'lightdm':
    cm.comexx("pacman -S lightdm && systemctl enable lightdm",mountX)
if lde == 'gdm':
    cm.comexx("pacman -S gdm && systemctl enable gdm",mountX)

pkgsa = ' '.join(archpkgs)
if de == 'plasma':
    pkgs = ' '.join(plasmapkgs)
    cm.comexx("pacman -S "+pkgs,mountX)
if de == 'cinnamon':
    pkgs = ' '.join(cinnamon)
    cm.comexx("pacman -S "+pkgs,mountX)
if de == 'xfce4':
    pkgs = ' '.join(xfce4)
    cm.comexx("pacman -S "+pkgs,mountX)
if de == 'gnome':
    pkgs = ' '.join(gnomepkgs)
    cm.comexx("pacman -S "+pkgs,mountX)
if archrepo:
    cm.comexx("pacman -S "+pkgsa,mountX)