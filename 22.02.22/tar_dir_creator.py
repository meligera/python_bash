import os
import tarfile
tar = tarfile.open('practice.tar.gz', 'w:gz')
for root, dirs, files in os.walk('.'):
    for file in files:
        tar.add(os.path.join(root, file))
tar.close()