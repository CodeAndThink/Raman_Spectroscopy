from sklearn.metrics import roc_auc_score
import DataLoader
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold

#   Hàm main là hàm thực hiện thuật toán học máy
import MachineLearningCalculator

def main():

    dataset_folder_name = 'dataset'
    source_link = 'D:/CÔNG VIỆC/TIẾN SĨ/CÔNG VIỆC/2023 - 03 Áp dụng hotpot series extraction vào đoán đường huyết bằng Raman/Mau du lieu/Method 3/'

    #   Lấy dữ liệu đưa vào tập X, tập y
    # X, y = DataLoader.loaddata(source_link, dataset_folder_name)
    X, y = DataLoader.loaddata_withseriesanomolydetection(source_link, dataset_folder_name)

    #   Chuyển dữ liệu sang dạng numpy để thực hiện thẩm định chéo K-fold
    numX = np.array(X)
    numy = np.array(y)
    print(numy)

    #   Thiết lập các tham số cũng như thiết lập mô hình học máy SVM
    model = RandomForestClassifier()

    max_rf_accuracy_score = 0.0
    min_rf_accuracy_score = 1.0

    sum_rf_accuracy_score = 0.0
    sum_rf_one_vs_rest_auc_ovr = 0.0
    sum_rf_one_vs_rest_sensitivity = 0.0
    sum_rf_one_vs_rest_specificity = 0.0

    #   Phân chia bộ dữ liệu huấn luyện và kiểm thử, đồng thời thiết lập số chu kỳ thí nghiệm là 5 x 30 = 150
    rskf = RepeatedStratifiedKFold(n_splits= 5, n_repeats= 30)
    i = 0
    for train_index, test_index in rskf.split(X,y):
        i += 1
        print("Turn:", i)
        print("TRAIN dataset have ", len(train_index), " sample include: ", train_index)
        print("TEST dataset have ", len(test_index), " sample include: ", test_index)
        X_train, X_test = numX[train_index], numX[test_index]
        y_train, y_test = numy[train_index], numy[test_index]

        # Huấn luyện
        model.fit(X_train, y_train)
        y_score = model.predict_proba(X_test)

        # Kiểm thử
        rf_prediction = model.predict(X_test)

        accuracy_score = metrics.accuracy_score(rf_prediction, y_test)
        print(f'Random Forest accuracy = {accuracy_score}')

        macro_roc_auc_ovr = roc_auc_score(
            y_test,
            y_score,
            multi_class="ovr",
            average="macro",
        )
        print(f'Micro-averaged One-vs-Rest ROC AUC score: = {macro_roc_auc_ovr}')

        # In và lấy giá trị để lấy kết quả cuối cùng
        # print("y_predicted", rf_prediction)
        # print("y_test", y_test)

        one_vs_rest_sensitivity = MachineLearningCalculator.RvO_sensitivity(rf_prediction, y_test)
        print(f'Sensitivity = {one_vs_rest_sensitivity}')

        one_vs_rest_specificity = MachineLearningCalculator.RvO_specificity(rf_prediction, y_test)
        print(f'Specificity = {one_vs_rest_specificity}')

        sum_rf_one_vs_rest_sensitivity += one_vs_rest_sensitivity
        sum_rf_one_vs_rest_specificity += one_vs_rest_specificity
        sum_rf_accuracy_score += accuracy_score
        sum_rf_one_vs_rest_auc_ovr += macro_roc_auc_ovr

        print("--------------------------------------")

        if (accuracy_score < min_rf_accuracy_score):
            min_rf_accuracy_score = accuracy_score

        if (accuracy_score > max_rf_accuracy_score):
            max_rf_accuracy_score = accuracy_score

    # In kết quả
    average_rf_accuracy_score = sum_rf_accuracy_score / i
    average_rf_micro_roc_auc_ovr = sum_rf_one_vs_rest_auc_ovr / i
    average_rf_one_vs_rest_sensitivity = sum_rf_one_vs_rest_sensitivity / i
    average_rf_one_vs_rest_specificity = sum_rf_one_vs_rest_specificity / i

    print("Average Random Forest accuracy: ", average_rf_accuracy_score, "in number of turn: ", i)
    print("Average Random Forest Micro-averaged One-vs-Rest ROC AUC score: ", average_rf_micro_roc_auc_ovr, "in number of turn: ", i)
    print("Average Random Forest One-vs-Rest ROC Sensitivity: ", average_rf_one_vs_rest_sensitivity, "in number of turn: ", i)
    print("Average Random Forest One-vs-Rest ROC Specificity: ", average_rf_one_vs_rest_specificity, "in number of turn: ", i)

    # print("Min Random Forest accuracy: ", min_rf_accuracy_score)
    # print("Max Random Forest accuracy: ", max_rf_accuracy_score)

#   Chạy hàm main
main()