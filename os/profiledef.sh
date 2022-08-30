#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="ddos"
iso_label="ddos"
iso_publisher="ddosX"
iso_application="ddos Live/Rescue CD"
iso_version="V1.1 unstable"
install_dir="arch"
buildmodes=('iso')

# uefi and bios
# bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito'
#            'uefi-ia32.grub.esp' 'uefi-x64.grub.esp'
#            'uefi-ia32.grub.eltorito' 'uefi-x64.grub.eltorito')

# bios 
# bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito')

# uefi (systemd)
bootmodes=('uefi-x64.systemd-boot.esp' 'uefi-x64.systemd-boot.eltorito')

# uefi (grub) (not work, fixing)
# bootmodes=('uefi-ia32.grub.esp' 'uefi-x64.grub.esp'
#            'uefi-ia32.grub.eltorito' 'uefi-x64.grub.eltorito')
           
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/usr/local/bin/choose-mirror"]="0:0:755"
  ["/usr/local/bin/Installation_guide"]="0:0:755"
  ["/usr/local/bin/livecd-sound"]="0:0:755"
  ["/usr/bin/more_walls"]="0:0:777"
  ["/usr/bin/ddpkg"]="0:0:777"
)
