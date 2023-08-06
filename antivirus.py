## Antivirus FarCry

import os
import os.path

path = '.'

for f in os.listdir(path):
    if f.beginswith('FarCry'):
        os.remove(os.path.join(path, f))
