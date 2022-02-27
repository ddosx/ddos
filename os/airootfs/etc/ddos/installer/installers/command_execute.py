import os
devmode = True
if devmode:
    def comex(command):
        os.system("echo '{}' >> command.list".format(command))
        # os.system(str(command))
    def comexx(command,path):
        os.system("echo '{}'::::'{}' >> command.list".format(command,path))
        # os.system('arch-chroot '+str(path)+' "'+str(command)+'"')
else:
    def comex(command):
        # os.system("echo '{}' >> command.list".format(command))
        os.system(str(command))
    def comexx(command,path):
        # os.system("echo '{}'::::'{}' >> command.list".format(command,path))
        os.system('arch-chroot '+str(path)+' "'+str(command)+'"')
