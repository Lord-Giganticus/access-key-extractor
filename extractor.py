import os
import time

keys = 0

if os.getcwd() != os.path.dirname(__file__) == True:
    os.chdir(__file__)

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        if file.endswith('.rpx') == True:
            os.system('cmd /c wiiurpxtool -d '+file)
            os.remove(file)
time.sleep(2)
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file) == True:
        if file.endswith('.elf') == True:
            os.system('cmd /c node extractor '+os.path.basename(file)+' > output.txt')
            output = open('output.txt','r')
            key = output.read()
            log = open('log.txt','w')
            log.write(key+'\n')
            log.close()
            output.close()
            os.remove('output.txt')
            keys += 1
try:
    open('log.txt')
    open('log.txt').close()
    print(keys, 'files were proccesed. Exiting.')
    time.sleep(5)
    exit()
except:
    print('No keys were produced. Exiting.')
    time.sleep(5)
    exit()