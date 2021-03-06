def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    tp = 0      ## true positive
    tn = 0      ## true negative
    fp = 0      ## false positive
    fn = 0      ## false negative

    for i in range(len(prediction)):
        if prediction[i] == True and ground_truth[i] == True:
            tp += 1
        if prediction[i] == True and ground_truth[i] == False:
            fp += 1
        if prediction[i] == False and ground_truth[i] == True:
            fn += 1
        if prediction[i] == False and ground_truth[i] == False:
            tn += 1

    accuracy = (tp + tn)/(tp + tn + fp + fn)
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    f1 = 2 * (precision * recall)/(precision + recall)

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score

    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    right = 0
    total = 0

    for i in range(len(prediction)):
        if prediction[i] == ground_truth[i]:
            right += 1
        total += 1

    return right/total
