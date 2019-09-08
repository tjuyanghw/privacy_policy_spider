from primes import is_prime
from levenshtein import distance
import queue
import os
import re

class RollingHash:

    def __init__(self, a=101):
        self.h = 0
        if not is_prime(a):
            raise ValueError('a must be prime')
        self.a = a
        self.history = queue.deque()
        self.size = 0

    def __call__(self):
        return self.h

    def append(self, value):
        #assert(ord(value) < self.a)
        self.h *= self.a
        self.h += ord(value)
        self.history.append(value)
        self.size += 1

    def popleft(self):
        x = ord(self.history.popleft())
        self.h -= x*self.a**(self.size-1)
        self.size -= 1
    

def rabin_karp(s,pattern):
    """ find first index where pattern occur in s, or -1 if pattern is not a substr"""
    Ns = len(s)
    Np = len(pattern)
    if Np > Ns: return -1
    
    hs = RollingHash()
    hp = RollingHash()

    for i in range(Np):
        hp.append(pattern[i])
        hs.append(s[i])

    if hs() == hp() and pattern == s[:Np]:
        return 0

    for i in range(Np,Ns):
        hs.popleft()
        hs.append(s[i])

        #print('i',i,s[i+1-Np:i+1],hs(),hp())
        if hs() == hp() and pattern == s[i+1-Np:i+1]:
                return i+1-Np

    return -1











def main():
    path1 = 'set'
    path2 = '115'
    files = os.listdir(path1)
    for file in files:
        if not os.path.isdir(file):
            f_w = os.path.basename(file)
            paths = "set/" + f_w
            # 读取文件
        with open(paths, 'r', encoding='ISO-8859-1') as f:
            all_text1 = (''.join(f.readlines())).lower()
        sentences1 = [x.strip().lower() for x in all_text1.split('.')]#

        files2 = os.listdir(path2)
        for file in files2:
            if not os.path.isdir(file):
                f_f = os.path.basename(file)
                pathss = "115/" + f_f
            with open(pathss, 'r', encoding='ISO-8859-1') as f:
                all_text2 = (''.join(f.readlines())).lower()
            sentences2 = [x.strip().lower() for x in all_text2.split('.')]

        # search matching sentences
            count = 0
           # print('正在评估短语的精确匹配…')
            for i,s1 in enumerate(sentences1):
                 if len(s1)< 16:
                     continue
                 if rabin_karp(all_text2,s1) != -1:
                    count += 1
                    i += 1
                    print('match:',s1)


                # search similar sentences
            similar = 0
           # print('正在评估短语的类似措辞…')

            for i,si in enumerate(sentences1):
                wordsi = si.split()
                for j,sj in enumerate(sentences2):
                    wordsj = sj.split()
                    d = distance(wordsi,wordsj)
                    if d < min(len(wordsi),len(wordsj)) * .75 and min(len(si),len(sj)) >= 16:
                        similar += 1
                        print('similar:\nsi: {}\nsj: {}'.format(si,sj))


            percentage = 100*similar/len(sentences1)
            if percentage != 0:
                with open('result.txt', 'a') as file_object:

                    file_object.write(str(percentage) + '\t')
                    file_object.write(paths + '-----' + pathss + '\n')
                print('Similar phrases: {similar} ({percentage:.2f}%)'
                      .format(similar=similar, percentage=percentage))
                print(' "{file1}" found "{file2}"'.format(file1=paths, file2=pathss))
                print('\n---------------------------------------------')




    


if __name__ == '__main__':


    main()
