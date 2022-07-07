import os
from config import PROJECT_ROOT

for file in os.scandir(os.path.join(PROJECT_ROOT, 'quickscripts')):
    os.remove(file.path)