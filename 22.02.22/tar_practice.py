import tarfile
#
# tar = tarfile.open('source.tar', 'w')
# # "w: gz - на сжатие"
# tar.add("source.txt")
# tar.close()

tar = tarfile.open('source.tar.gz', 'w:gz')
# "w: gz - на сжатие"
tar.add("source.txt")
tar.close()