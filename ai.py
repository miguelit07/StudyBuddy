import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    # Connect to the SQLite database
    conn = sqlite3.connect("database.db")

    # Load data from the database into a Pandas DataFrame
    query = "SELECT * FROM StudentPerformance;"
    data = pd.read_sql_query(query, conn)
    print(data.columns)

    # Close the database connection
    conn.close()

    # Split data into features and target variable
    target_name = "TimeItTook"
    X = data.drop(columns=["TimeItTook"])
    y = data["TimeItTook"]

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Convert data to DMatrix format for XGBoost
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    # Define XGBoost parameters
    params = {
        "objective": "binary:logistic",
        "max_depth": 3,
        "learning_rate": 0.1,
        "eval_metric": "logloss",
    }

    # Train the XGBoost model
    num_rounds = 100
    model = xgb.train(params, dtrain, num_rounds)

    # Make predictions on the test set
    y_pred = model.predict(dtest)
    predictions = [round(value) for value in y_pred]

    # Evaluate model accuracy
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
