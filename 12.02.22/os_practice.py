import os


def files(path):
    slashes = path.count('/')
    for f in os.walk(path):
        last_slash = f[0].rfind('/')
        depth = f[0].count('/') - slashes
        print(depth * '--', f[0][last_slash + 1])
        for d in f[1]:
            print(depth + 1 * '--', f[1])
        for file_ in f[2]:
            print(depth + 1 * '--', f[2])


files('home/gera/PycharmProjects/bash_lang/16.02.22')
