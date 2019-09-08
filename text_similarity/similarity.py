import os
import nltk
def Jaccrad(word1,word2):

    pass

if __name__ == "__main__":
    path1='set'
    path2='115'
    files = os.listdir(path1)
    for file in files:
        if not os.path.isdir(file):
            f_w = os.path.basename(file)
            paths = "set/" + f_w
            # 读取文件
        with open(paths, 'r', encoding='ISO-8859-1') as f:
            all_text1 = (''.join(f.readlines())).lower()
            word1 = [x.strip() for x in nltk.word_tokenize(all_text1)]
            #print(word1)

            # print('文件名：{file1}-------单词{word}'.format(file1=paths,word=len(word1)))
            #print(word1)
            print(set(word1))

    files2 = os.listdir(path2)
    for file in files2:
        if not os.path.isdir(file):
            f_f = os.path.basename(file)
            pathss = "115/" + f_f
        with open(pathss, 'r') as f:
            all_text2 = (''.join(f.readlines())).lower()
            word2 = [x.strip() for x in nltk.word_tokenize(all_text2)]
            # print('文件名：{file2}-------单词{word}'.format(file2=pathss, word=len(word2)))


    Jaccrad(word1,word2)

