from database import load_data_from_postgres, test_connection
from data_preprocessing import preprocess
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def create_model():
    test_connection()
    train = load_data_from_postgres()
    train = preprocess(train)
    X_train, X_test, y_train, y_test = train_test_split(train.drop('survived', axis=1), train['survived'], test_size=0.30, random_state=101)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model trained and logged with accuracy: {accuracy}")