import os
import time
import shutil

try:
    os.system('node -v')
except:
    print('node is not installed. Exiting.')
    time.sleep(5)
    exit()

keys = 0

if os.getcwd() != os.path.dirname(__file__):
    os.chdir(os.path.dirname(__file__))
    print(os.getcwd())

try:
    os.system('curl.exe --version > output.txt')
    os.remove('output.txt')
except:
    print("curl is not installed exiting.")
    time.sleep(5)
    exit()

if os.path.isfile('extractor.js') == False:
    os.system('cmd /c curl https://github.com/Lord-Giganticus/access-key-extractor/releases/download/latest/extractor.js --output extractor.js')

if os.path.isfile('wiiurpxtool.exe') == False:
    try:
        os.system('wiiurpxtool -h')
    except:
        os.system('cmd /c curl https://github.com/Lord-Giganticus/access-key-extractor/releases/download/latest/wiiurpxtool.exe --output wiiurpxtool.exe')

if os.path.isfile('sha1.py') == False:
    os.system('cmd /c curl https://github.com/Lord-Giganticus/access-key-extractor/releases/download/latest/sha1.py --output sha1.py')

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        if file.endswith('.rpx') == True:
            file_name = os.path.splitext(os.path.basename(file))
            file_name = file_name[0]
            os.system('cmd /c wiiurpxtool -d '+file+' '+file_name+'.elf')
            try:
                os.chdir('temp_dir')
                os.chdir('../')
            except:
                os.mkdir('temp_dir')
            shutil.move(file, 'temp_dir')
time.sleep(2)
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file) == True:
        if file.endswith('.elf') == True:
            os.system('cmd /c node extractor '+os.path.basename(file)+' > output.txt')
            output = open('output.txt','r')
            key = output.readlines()
            key = key[3]
            file_name = os.path.splitext(os.path.basename(file))
            file_name = file_name[0]
            try:
                log = open('keys.txt','a')
                with open('keys.txt') as file:
                    contents = file.read()
                text = file_name+'.rpx'
                if text in contents:
                    print('Keys for',file_name+'.rpx already processed. Skipping.')
                    time.sleep(5)
                    file.close()
                else:
                    log.write('from '+file_name+'.rpx:\n'+key)
                    log.close()
                output.close()
                os.remove('output.txt')
                keys += 1
            except:
                log = open('keys.txt','w')
                log.write('From '+file_name+'.rpx:\n'+key)
                log.close()
                output.close()
                os.remove('output.txt')
                keys += 1
try:
    open('keys.txt')
    open('keys.txt').close()
    print(keys, 'files were proccesed. Getting sha1 dumps.')
except:
    print('No keys were produced. Exiting.')
    time.sleep(5)
    exit()
os.chdir('temp_dir')
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file) == True:
        if file.endswith('.rpx') == True:
            shutil.move(file, os.path.dirname(__file__))
os.chdir('../')
shutil.rmtree('temp_dir')
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file) == True:
        if file.endswith('.elf') == True:
            os.remove(file)
        if file.endswith('.rpx') == True:
            os.system('cmd /c python -m sha1 '+file+' > output.txt')
            with open('output.txt') as f:
                contents = f.read()
                try:
                    sha1 = open('sha1.txt','a')
                    with open('sha1.txt') as e:
                        text = e.read()
                        if contents in text:
                            print("sha1 for "+file+' already present. Skipping.')
                            time.sleep(5)
                            file.close()
                            e.close()
                        else:
                            sha1.write('From '+file+':\n'+contents)
                            sha1.close()
                            f.close()
                except:
                    f = open('sha1.txt','w')
                    f.write('From '+file+':\n'+contents)
                    f.close()
            os.remove('output.txt')
print("Complete. Exiting.")
time.sleep(5)
exit()