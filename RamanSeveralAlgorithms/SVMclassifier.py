from matplotlib import pyplot as plt
from sklearn.metrics import RocCurveDisplay, roc_auc_score

import DataLoader
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.svm import SVC
from sklearn import metrics
import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold

#   Hàm main là hàm thực hiện thuật toán học máy
import MachineLearningCalculator
from MachineLearningCalculator import RvO_sensitivity


def main():

    dataset_folder_name = 'dataset'
    source_link = 'C:/Users/trg14/PycharmProjects/RamanSeveralAlgorithms/'

    #   Lấy dữ liệu đưa vào tập X, tập y
    X, y = DataLoader.loaddata(source_link, dataset_folder_name)
    # X, y = DataLoader.loaddata_withseriesanomolydetection(source_link, dataset_folder_name)

    #   Chuyển dữ liệu sang dạng numpy để thực hiện thẩm định chéo K-fold
    numX = np.array(X)
    numy = np.array(y)
    # print(numy)

    #   Thiết lập các tham số cũng như thiết lập mô hình học máy SVM
    model = make_pipeline(StandardScaler(), SVC(kernel='rbf'))
    # model = make_pipeline(StandardScaler(), SVC())

    max_svm_accuracy_score = 0.0
    min_svm_accuracy_score = 1.0

    sum_svm_accuracy_score = 0.0
    sum_svm_one_vs_rest_auc_ovr = 0.0
    sum_svm_one_vs_rest_sensitivity = 0.0
    sum_svm_one_vs_rest_specificity = 0.0

    #   Phân chia bộ dữ liệu huấn luyện và kiểm thử, đồng thời thiết lập số chu kỳ thí nghiệm là 5 x 30 = 150
    rskf = RepeatedStratifiedKFold(n_splits=5, n_repeats=30)
    i = 0
    for train_index, test_index in rskf.split(X, y):
        i += 1
        print("Turn:", i)
        print("TRAIN dataset have ", len(train_index), " sample include: ", train_index)
        print("TEST dataset have ", len(test_index), " sample include: ", test_index)
        X_train, X_test = numX[train_index], numX[test_index]
        y_train, y_test = numy[train_index], numy[test_index]

        # Huấn luyện
        model.fit(X_train, y_train)
        # y_score = model.predict_proba(X_test)

        # Kiểm thử
        svm_prediction = model.predict(X_test)

        accuracy_score = metrics.accuracy_score(svm_prediction, y_test)
        print(f'SVM accuracy = {accuracy_score}')

        # macro_roc_auc_ovr = roc_auc_score(
        #     y_test,
        #     y_score,
        #     multi_class="ovr",
        #     average="macro",
        # )
        # print(f'Micro-averaged One-vs-Rest ROC AUC score: = {macro_roc_auc_ovr}')

        # In và lấy giá trị để lấy kết quả cuối cùng
        # print("y_predicted", rf_prediction)
        # print("y_test", y_test)

        one_vs_rest_sensitivity = MachineLearningCalculator.RvO_sensitivity(svm_prediction, y_test)
        print(f'Sensitivity = {one_vs_rest_sensitivity}')

        one_vs_rest_specificity = MachineLearningCalculator.RvO_specificity(svm_prediction, y_test)
        print(f'Specificity = {one_vs_rest_specificity}')

        sum_svm_one_vs_rest_sensitivity += one_vs_rest_sensitivity
        sum_svm_one_vs_rest_specificity += one_vs_rest_specificity
        sum_svm_accuracy_score += accuracy_score
        # sum_svm_one_vs_rest_auc_ovr += macro_roc_auc_ovr

        print("--------------------------------------")

        if (accuracy_score < min_svm_accuracy_score):
            min_svm_accuracy_score = accuracy_score

        if (accuracy_score > max_svm_accuracy_score):
            max_svm_accuracy_score = accuracy_score

    # In kết quả
    average_svm_accuracy_score = sum_svm_accuracy_score / i
    # average_svm_micro_roc_auc_ovr = sum_svm_one_vs_rest_auc_ovr / i
    sum_svm_one_vs_rest_sensitivity = sum_svm_one_vs_rest_sensitivity / i
    sum_svm_one_vs_rest_specificity = sum_svm_one_vs_rest_specificity / i

    print("Average SVM accuracy: ", average_svm_accuracy_score, "in number of turn: ", i)
    # print("Average SVM Micro-averaged One-vs-Rest ROC AUC score: ", average_svm_micro_roc_auc_ovr, "in number of turn: ", i)
    print("Average SVM One-vs-Rest ROC Sensitivity: ", sum_svm_one_vs_rest_sensitivity, "in number of turn: ", i)
    print("Average SVM One-vs-Rest ROC Specificity: ", sum_svm_one_vs_rest_specificity, "in number of turn: ", i)
    # print("Min Random Forest accuracy: ", min_svm_accuracy_score)
    # print("Max Random Forest accuracy: ", max_svm_accuracy_score)


#   Chạy hàm main
main()