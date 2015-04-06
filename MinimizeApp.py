import subprocess
import os
import shutil
import sys


args = str(sys.argv)
# path = args[0]
# out = args[1]

####insert you input directory path and your desired destination
path = r'C:\inetpub\wwwroot\wab\reg'
out = r'C:\inetpub\wwwroot\wab\min'

if not out.endswith(r'\\'): out += r'\\'
for root, dirs, files in os.walk(path):
    for name in dirs:
        # print(os.path.join(root, name))

        fullname = os.path.join(root,name)
    #     copy file structure
        pastroot = fullname.split(path)[1]
        newpath = os.path.join(out+pastroot)
        if not os.path.exists(newpath):os.makedirs(newpath)
    for name in files:
        fullname = os.path.join(root, name)
        # print fullname
        pastroot = fullname.split(path)[1]
        newpath = os.path.join(out+pastroot)

        print newpath
        if name.endswith('.js'):
            subprocess.call('uglifyjs '+fullname + ' -o '+newpath, shell=True)
        elif name.endswith('.css'):
            subprocess.call("cleancss "+fullname+" -o "+newpath ,shell=True)
        elif name.endswith('.html'):
            subprocess.call("minimize -c true -d true -s true -q true --output " + newpath + " " + fullname,shell=True )
        else:
            shutil.copyfile(fullname,newpath)

