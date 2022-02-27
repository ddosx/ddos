#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="ddos"
iso_label="ddos"
iso_publisher="ddosX"
iso_application="ddos Live/Rescue CD"
iso_version="V0.7X beta"
install_dir="arch"
buildmodes=('iso')

# uefi and bios
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito' 'uefi-x64.systemd-boot.esp' 'uefi-x64.systemd-boot.eltorito')

# bios 
# bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito')

# uefi
# bootmodes=('uefi-x64.systemd-boot.esp' 'uefi-x64.systemd-boot.eltorito')

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
  ["/etc/shadow"]="0:0:0400"
  ["/etc/gshadow"]="0:0:0400"
  ["/etc/ddos_conf/autostart.sh"]="0:0:777"
  ["/etc/ddos_conf/gtk-theme.sh"]="0:0:777"
  ["/etc/ddos_conf/icon_pack.sh"]="0:0:777"
  ["/etc/ddos_conf/wallpaper.sh"]="0:0:777"
  ["/etc/ddos_conf/window_keys.sh"]="0:0:777"
)
