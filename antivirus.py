## Antivirus FarCry

import os
import os.path

path = '.'

for f in os.listdir(path):
    if f == 'FarCry.py':
        os.remove(os.path.join(path, f))
