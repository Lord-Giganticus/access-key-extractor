import os
import time
import shutil

keys = 0

if os.getcwd() != os.path.dirname(__file__):
    os.chdir(os.path.dirname(__file__))
    print(os.getcwd())

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
                log = open('log.txt','a')
                with open('log.txt') as file:
                    contents = file.read()
                text = file_name+'.rpx'
                if text in contents:
                    print('Keys for',file_name+'.rpx already processed. Skipping.')
                    time.sleep(5)
                    log.close()
                else:
                    log.write('from '+file_name+'.rpx:\n'+key)
                    log.close()
                output.close()
                os.remove('output.txt')
                keys += 1
            except:
                log = open('log.txt','w')
                log.write('from '+file_name+'.rpx:\n'+key)
                log.close()
                output.close()
                os.remove('output.txt')
                keys += 1
try:
    open('log.txt')
    open('log.txt').close()
    print(keys, 'files were proccesed. Exiting.')
except:
    print('No keys were produced. Exiting.')
os.chdir('temp_dir')
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file) == True:
        if file.endswith('.rpx') == True:
            shutil.move(file, os.path.dirname(__file__))
os.chdir('../')
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file) == True:
        if file.endswith('.elf') == True:
            os.remove(file)
shutil.rmtree('temp_dir')
time.sleep(5)
exit()