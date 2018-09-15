from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer


def get_train_data(file):
    f = open(file,encoding="utf8")
    data_x =[]
    data_y =[]
    for line in f:
        row = line.strip("\n").split("\t")
        if len(row) < 2:
            continue
        feature = " ".join(row[0].split(","))
        data_x.append(feature)
        data_y.append(row[1])
    f.close()
    X_train, X_test, y_train, y_test = train_test_split(data_x,data_y,test_size=0.2)
    return X_train, X_test, y_train, y_test

def train_model_svm(file,stop_words):
    X_train, X_test, y_train, y_test = get_train_data(file)
    counter = CountVectorizer(analyzer="word",stop_words=stop_words)
    train_data = counter.fit_transform(X_train)
    test_data = counter.fit_transform(X_test)
    svm = SVC()
    svm.fit(train_data,y_train)
    print(svm.score(test_data,y_test))


if __name__=="__main__":
    f = open("stopwords.txt",encoding="utf8")
    stop_words = f.readlines()
    train_model_svm("merge.txt", stop_words)




