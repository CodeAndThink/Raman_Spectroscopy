import DataLoader
from sklearn.ensemble import BaggingClassifier
from sklearn import metrics
import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold

#   Hàm main là hàm thực hiện thuật toán học máy
def main():

    dataset_folder_name = 'dataset'
    source_link = 'C:/Users/Admin/Desktop/FastAccess/Fast Access/CÔNG VIỆC/TIẾN SĨ/Mau du lieu/Method 3/'

    #   Lấy dữ liệu đưa vào tập X, tập y
    X, y = DataLoader.loaddata(source_link, dataset_folder_name)

    #   Chuyển dữ liệu sang dạng numpy để thực hiện thẩm định chéo K-fold
    numX = np.array(X)
    numy = np.array(y)
    print(numy)

    #   Thiết lập các tham số cũng như thiết lập mô hình học máy SVM
    model = BaggingClassifier()
    sum_rf_accuracy_score = 0.0
    max_rf_accuracy_score = 0.0
    min_rf_accuracy_score = 1.0

    #   Phân chia bộ dữ liệu huấn luyện và kiểm thử, đồng thời thiết lập số chu kỳ thí nghiệm là 100 x 3 = 300
    rskf = RepeatedStratifiedKFold(n_splits= 3, n_repeats= 50)
    i = 0
    for train_index, test_index in rskf.split(X,y):
        i += 1
        print("Turn:", i)
        print("TRAIN dataset have ",len(train_index)," sample include: ", train_index)
        print("TEST dataset have ", len(test_index), " sample include: ", test_index)
        X_train, X_test = numX[train_index], numX[test_index]
        y_train, y_test = numy[train_index], numy[test_index]

        # Huấn luyện
        model.fit(X_train, y_train)

        # Kiểm thử
        rf_prediction = model.predict(X_test)
        # print("y_predicted", rf_prediction)
        # print("y_test", y_test)
        accuracy_score = metrics.accuracy_score(rf_prediction, y_test)

        # In và lấy giá trị để lấy kết quả cuối cùng
        print(f'Bagging accuracy = {accuracy_score}')
        sum_rf_accuracy_score += accuracy_score
        print("--------------------------------------")

        if (accuracy_score < min_rf_accuracy_score):
            min_rf_accuracy_score = accuracy_score

        if (accuracy_score > max_rf_accuracy_score):
            max_rf_accuracy_score = accuracy_score

    # In kết quả
    average_rf_accuracy_score = sum_rf_accuracy_score / i
    print("Average Bagging accuracy: ", average_rf_accuracy_score, "in number of turn: ", i)
    print("Min Bagging accuracy: ", min_rf_accuracy_score)
    print("Max Bagging accuracy: ", max_rf_accuracy_score)

#   Chạy hàm main
main()