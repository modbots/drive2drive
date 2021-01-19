import os
import time
from util.config import first, second, third
firstD = first
secondD = second
thirdD = third
S = '-s '
D = ' -d '
C = ' --copy '
os.system('python3 autorclone.py '+ C + S + firstD + D + secondD)

time.sleep(15)
os.system('rclone --config rclone-generated.conf size src001:')
os.system('rclone --config rclone-generated.conf size dst001:')
os.system('rclone --config rclone-generated.conf dedupe dst001:')
time.sleep(120)

os.system('python3 loop.py')
