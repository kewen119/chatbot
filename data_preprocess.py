import re
import os
import jieba

#提取豆瓣问答中的问题，并且在每个问题后面加上0
def douban_question_prepare(path,file_name):
    d = []
    with open ("{}.txt".format(file_name) , "a", encoding= 'utf8') as file_name:
        with open(path,encoding='utf8') as f:
            for row in f:
                row = row.split("\t")
                tempo = row[1]+"\t"+ str(0)
                d.append(tempo)
            tempo_file = set(d)

            for i in tempo_file:
                file_name.write(i)
                file_name.write("\n")


# 提取百度问答中的问题，并且在每个问题后面加上1

def baidu_question_prepare(path):

    dir = os.listdir(path)
    dir = "".join(dir)
    file_name_list = re.findall(r"C\d*Question.dat", dir)
    for file_name in file_name_list:
        with open("baiduquestion.txt", "a", encoding="utf8") as baiduquestion:
            with open(path+file_name, encoding='utf8') as f:
                for row in f:
                    row = row.split("\t")
                    tempo = ''.join(row[2:])
                    tempo = tempo.replace("\\r\\n"," ")
                    tempo = tempo.replace("\n","")
                    tempo = tempo + "\t" + str(1) + "\n"
                    baiduquestion.write(tempo)
                    baiduquestion.write("\n")



douban_question_prepare("D:/wenke/Downloads/ChatBot/data/DoubanConversaionCorpus/train.txt", "doubanquestion")
print ("doubanquestion has been done!")
baidu_question_prepare("D:/wenke/Downloads/ChatBot/data/Baidu%20Data/baidu_knows/")
print ("baiduquestion has been done!")


# 将百度问题集做分词处理
f = open("baiduquestion.txt", "r", encoding="utf8")
f2 = open("baiduquestionfenci.txt","w",encoding="utf8")
line = f.readline()
while line:
    line= line.strip("\n")
    seg_list = jieba.cut(line)
    string = " ".join(seg_list)
    f2.write(string)
    f2.write("\n")
    line = f.readline()
print("BaiDu fenci Done!")


#合并两个文件
merge_text = open("merge.txt","a", encoding="utf8")
file_name_list = ["baiduquestionfenci.txt", "doubanquestion.txt"]

for file_name in file_name_list:
    file = open(file_name,encoding="utf8")
    for line in file.readlines():
        merge_text.write(line)
    merge_text.write("\n")

merge_text.close()
print("Merge has benn done!")







#
#

