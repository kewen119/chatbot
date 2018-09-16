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
    # X_train, X_test, y_train, y_test = train_test_split(data_x,data_y,test_size=0.2)
    return data_x, data_y

def train_model_svm(file,stop_words):
    data_x, data_y = get_train_data(file)
    counter = CountVectorizer(analyzer="word",stop_words=stop_words)
    train_data = counter.fit_transform(data_x).toarray
    X_train, X_test, y_train, y_test = train_test_split(train_data, data_y, test_size=0.2)
    svm = SVC()
    svm.fit(X_train,y_train)
    print(svm.score(X_test,y_test))


if __name__=="__main__":
    f = open("stopwords.txt",encoding="utf8")
    stop_words = f.readlines()
    train_model_svm("merge.txt", stop_words)




