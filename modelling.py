import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def create_model():
    # Test database connection
    test_connection()
    
    # Load and preprocess data
    train = load_data_from_postgres()
    train = preprocess(train)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        train.drop('survived', axis=1), 
        train['survived'], 
        test_size=0.30, 
        random_state=101
    )
    
    # Create and train the model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model trained and logged with accuracy: {accuracy}")

    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Save the model using pickle
    model_path = 'models/logistic_regression_model.pkl'
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    print(f"Model saved to {model_path}")
