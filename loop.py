import os
import time
from util.config import first, second, third, fourth
firstD = first
secondD = second
thirdD = third
fourthD = fourth
S = '-s '
D = ' -d '
C = ' --copy '
os.system('python3 autorclone.py '+ C + S + tirdD + D + fourthD)

time.sleep(15)
os.system('rclone --config rclone-generated.conf size src001:')
os.system('rclone --config rclone-generated.conf size dst001:')
os.system('rclone --config rclone-generated.conf dedupe dst001:')
time.sleep(120)



#os.system('python3 autorclone.py --sync -s 0ACT5UpIf3zQMUk9PVA -d 0AJKePN7XU84hUk9PVA')
#time.sleep(120)
#os.system('python3 autorclone.py --sync -s 0AJKePN7XU84hUk9PVA -d 0ADCeN_vURI8gUk9PVA')
#time.sleep(120)
#os.system('python3 autorclone.py --sync -s 0ADCeN_vURI8gUk9PVA -d 0AOiOrOe5PEGyUk9PVA')
#time.sleep(120)
os.system('python3 back.py')
