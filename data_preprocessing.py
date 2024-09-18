import pandas as pd
from database import load_data_from_postgres


def impute_age(cols):
    age = cols[0]
    pclass = cols[1]
    
    if pd.isnull(age):
        if pclass == 1:
            return 37
        elif pclass == 2:
            return 29
        else:
            return 24
    else:
        return age

def preprocess(train):
    if train.empty:
        print("No data to process. Exiting.")
        return
    
    train['age'] = train[['age', 'pclass']].apply(impute_age, axis=1)
    train.drop('cabin', axis=1, inplace=True)
    train.dropna(inplace=True)
    sex = pd.get_dummies(train['sex'], drop_first=True)
    embark = pd.get_dummies(train['embarked'], drop_first=True)
    train.drop(['sex', 'embarked', 'name', 'ticket'], axis=1, inplace=True)
    train = pd.concat([train, sex, embark], axis=1)
    return train