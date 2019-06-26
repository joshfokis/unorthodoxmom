import os
from time import sleep

os.chdir('../staticfiles')
os.popen('rm js/mom*')
os.popen('rm css/mom*')
sleep(1)
count = 0
for js in os.listdir('js'):
    file_count = ''
    if count == 0:
        file_count = ''
    else:
        file_count = count+1
    print(f'renaming {js} as mom{file_count}.js')
    os.popen(f'mv js/{js} js/mom{file_count}.js')
    count += 1
    

os.popen('mv css/* css/mom.css')

print(os.getcwd())