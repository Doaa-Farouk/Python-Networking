import subprocess
import os
# j = subprocess.run(['journalctl','-r'])
# log_file = 'log_file.txt'
# with open(log_file, 'w') as f:
#     f.write(j)

print(os.getcwd())
print(os.path.join(os.getcwd(),'f.txt'))
print(os.path.exists('/home/nightmare/pt'))
print(os.name)