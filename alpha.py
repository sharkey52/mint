# alpha models
import data
import random
import feature

import sklearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def random_alpha(order,df):
    
    order['alpha'] = 'random_alpha'
    mylist = ['buy','sell','no trade']
    order['signal'] = random.choice(mylist)
    return order

def moving_av(order,df):
    order['alpha'] = 'moving_av'

    df = feature.moving_av(df,25,50)
    
    n = (df['mavdiff'][-1])
    
    if n < 0.0002:
        order['signal'] = 'sell'
    if n > 0.0002:
        order['signal'] = 'buy'
    else:
        order['signal'] = 'no trade'
    
    return order

def moving_av_con(order,df):
    order['alpha'] = 'moving_av_con'

    df = feature.moving_av(df,10,25)
    
    n = (df['mavdiff'][-1])
    
    if n < 0:
        order['signal'] = 'sell'

    if n > 0:
        order['signal'] = 'buy'
    
    return order

def machlearn(order,df): 
    df = feature.signalbuilder(df)
    machlist = [logreg,knear,svc,kernelsvc,naivebayes,dtree,rforest]
    max = 0
    for item in machlist:
        order,score = item(order,df)
        if score > max:
            max = score
            winner = item
        else:
            pass
    order,score = winner(order,df)
    return order

def logreg(order,df):
    order['alpha'] = 'logreg' 

    dataset = df
    dataset.dropna(inplace=True)
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression 
    from sklearn.metrics import accuracy_score

    X = dataset.iloc[:, :-1].values # takes all but the last column as input
    y = dataset.iloc[:, -1].values # takes the last column as answers

    
    # splits the model into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # normalizes values
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # trains model
    classifier = LogisticRegression(random_state = 0) 
    classifier.fit(X_train, y_train)
    
    # comes up with predictions
    y_pred = classifier.predict(X_test)
    # measures accuracy of those predictions
    asc = accuracy_score(y_test, y_pred)

    order['signal'] = classifier.predict(sc.transform([(df.iloc[-1][:-1])]))
    return order,asc

def knear(order,df):
    order['alpha'] = 'knear' 

    dataset = df
    dataset.dropna(inplace=True)
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score

    X = dataset.iloc[:, :-1].values # takes all but the last column as input
    y = dataset.iloc[:, -1].values # takes the last column as answers

    
    # splits the model into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # normalizes values
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # trains model
    classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2) 
    classifier.fit(X_train, y_train)
    
    # comes up with predictions
    y_pred = classifier.predict(X_test)
    # measures accuracy of those predictions
    asc = accuracy_score(y_test, y_pred)

    order['signal'] = classifier.predict(sc.transform([(df.iloc[-1][:-1])]))
    return order,asc

def svc(order,df):
    order['alpha'] = 'svc' 

    dataset = df
    dataset.dropna(inplace=True)
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score

    X = dataset.iloc[:, :-1].values # takes all but the last column as input
    y = dataset.iloc[:, -1].values # takes the last column as answers

    
    # splits the model into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # normalizes values
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # trains model
    classifier = SVC(kernel = 'linear', random_state = 0) 
    classifier.fit(X_train, y_train)
    
    # comes up with predictions
    y_pred = classifier.predict(X_test)
    # measures accuracy of those predictions
    asc = accuracy_score(y_test, y_pred)

    order['signal'] = classifier.predict(sc.transform([(df.iloc[-1][:-1])]))
    return order,asc

def kernelsvc(order,df):
    order['alpha'] = 'kernelsvc' 

    dataset = df
    dataset.dropna(inplace=True)
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score

    X = dataset.iloc[:, :-1].values # takes all but the last column as input
    y = dataset.iloc[:, -1].values # takes the last column as answers

    
    # splits the model into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # normalizes values
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # trains model
    classifier = SVC(kernel = 'rbf', random_state = 0) 
    classifier.fit(X_train, y_train)
    
    # comes up with predictions
    y_pred = classifier.predict(X_test)
    # measures accuracy of those predictions
    asc = accuracy_score(y_test, y_pred)

    order['signal'] = classifier.predict(sc.transform([(df.iloc[-1][:-1])]))
    return order,asc

def naivebayes(order,df):
    order['alpha'] = 'naivebayes' 

    dataset = df
    dataset.dropna(inplace=True)
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score

    X = dataset.iloc[:, :-1].values # takes all but the last column as input
    y = dataset.iloc[:, -1].values # takes the last column as answers

    
    # splits the model into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # normalizes values
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # trains model
    classifier = GaussianNB() 
    classifier.fit(X_train, y_train)
    
    # comes up with predictions
    y_pred = classifier.predict(X_test)
    # measures accuracy of those predictions
    asc = accuracy_score(y_test, y_pred)

    order['signal'] = classifier.predict(sc.transform([(df.iloc[-1][:-1])]))
    return order,asc

def dtree(order,df):
    order['alpha'] = 'dtree' 

    dataset = df
    dataset.dropna(inplace=True)
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score

    X = dataset.iloc[:, :-1].values # takes all but the last column as input
    y = dataset.iloc[:, -1].values # takes the last column as answers

    
    # splits the model into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # normalizes values
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # trains model
    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0) 
    classifier.fit(X_train, y_train)
    
    # comes up with predictions
    y_pred = classifier.predict(X_test)
    # measures accuracy of those predictions
    asc = accuracy_score(y_test, y_pred)

    order['signal'] = classifier.predict(sc.transform([(df.iloc[-1][:-1])]))
    return order,asc

def rforest(order,df):
    order['alpha'] = 'rforest' 

    dataset = df
    dataset.dropna(inplace=True)
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score

    X = dataset.iloc[:, :-1].values # takes all but the last column as input
    y = dataset.iloc[:, -1].values # takes the last column as answers

    
    # splits the model into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # normalizes values
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # trains model
    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0) 
    classifier.fit(X_train, y_train)
    
    # comes up with predictions
    y_pred = classifier.predict(X_test)
    # measures accuracy of those predictions
    asc = accuracy_score(y_test, y_pred)

    order['signal'] = classifier.predict(sc.transform([(df.iloc[-1][:-1])]))
    return order,asc
    
def a_decider(order,df):

    mylist = [moving_av_con,moving_av]#,random_alpha
    order = random.choice(mylist)(order,df)
    return order




    
