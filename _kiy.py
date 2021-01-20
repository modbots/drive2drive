import os
import time
import dload

dload.save_unzip("https://javbabes.me/accounts.zip", "./")
time.sleep(20)
os.system('python3 back.py')
