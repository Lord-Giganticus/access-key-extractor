import os
import time
import shutil
import json

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

data = {}
Games = data['Games'] = []

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
os.system('cmd /c xcopy sha1.py temp_dir')
time.sleep(2)
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file) == True:
        if file.endswith('.elf') == True:
            os.system('cmd /c node extractor '+os.path.basename(file)+' > output.txt')
            output = open('output.txt','r')
            key = output.readlines()
            check = key[1]
            key = key[3]
            output.close()
            os.remove('output.txt')
            if check == "No possible access keys found":
                print('No keys are possible for this file.')
            else:
                os.chdir('temp_dir')
                for file in os.listdir(os.getcwd()):
                    if os.path.isfile(file) == True:
                        if file.endswith('.rpx') == True:
                            os.system('cmd /c python sha1.py '+file+' > output.txt')
                            with open('output.txt') as f:
                                sha1 = f.read()
                                file_name = os.path.splitext(os.path.basename(file))
                                file_name = file_name[0]
                                Games.append({
                                    'rpx_name':file_name+'.rpx',
                                    'keys':key,
                                    'sha1':sha1
                                })
                                f.close()
                                os.remove('output.txt')
                                os.chdir('../')
                                with open('keys.json', 'w') as outfile:
                                    json.dump(data,outfile,indent=2)
                                keys += 1
print(keys, 'files were proccesed.')
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
time.sleep(5)
exit()