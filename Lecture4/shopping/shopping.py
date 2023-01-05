import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            processed_row = []
            processed_row.append(int(row['Administrative']))
            processed_row.append(float(row['Administrative_Duration']))
            processed_row.append(int(row['Informational']))
            processed_row.append(float(row['Informational_Duration']))
            processed_row.append(int(row['ProductRelated']))
            processed_row.append(float(row['ProductRelated_Duration']))
            processed_row.append(float(row['BounceRates']))
            processed_row.append(float(row['ExitRates']))
            processed_row.append(float(row['PageValues']))
            processed_row.append(float(row['SpecialDay']))
            if row['Month'] == 'Jan':
                processed_row.append(0)
            elif row['Month'] == 'Feb':
                processed_row.append(1)
            elif row['Month'] == 'Mar':
                processed_row.append(2)
            elif row['Month'] == 'Apr':
                processed_row.append(3)
            elif row['Month'] == 'May':
                processed_row.append(4)
            elif row['Month'] == 'June':
                processed_row.append(5)
            elif row['Month'] == 'Jul':
                processed_row.append(6)
            elif row['Month'] == 'Aug':
                processed_row.append(7)
            elif row['Month'] == 'Sep':
                processed_row.append(8)
            elif row['Month'] == 'Oct':
                processed_row.append(9)
            elif row['Month'] == 'Nov':
                processed_row.append(10)
            elif row['Month'] == 'Dec':
                processed_row.append(11)
            processed_row.append(int(row['OperatingSystems']))
            processed_row.append(int(row['Browser']))
            processed_row.append(int(row['Region']))
            processed_row.append(int(row['TrafficType']))
            processed_row.append(1) if row['VisitorType'] == 'Returning_Visitor' else processed_row.append(0)
            processed_row.append(1) if row['Weekend'] == 'TRUE' else processed_row.append(0)
            evidence.append(processed_row)
            labels.append(1) if row['Revenue'] == 'TRUE' else labels.append(0)
    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neigh = KNeighborsClassifier(n_neighbors=1)
    neigh.fit(evidence, labels)
    return neigh


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    correct_positive = 0.0
    total_positive = 0.0
    correct_negative = 0.0
    total_negative = 0.0
    for label, prediction in zip(labels, predictions):
        if label == 1 and prediction == 1:
            correct_positive += 1
        if label == 1:
            total_positive += 1
        if label == 0 and prediction == 0:
            correct_negative += 1
        if label == 0:
            total_negative += 1
    sensitivity = correct_positive / total_positive
    specificity = correct_negative / total_negative
    return sensitivity, specificity


if __name__ == "__main__":
    main()