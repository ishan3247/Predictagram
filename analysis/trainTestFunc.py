def cuztomized_train_test(X, y):

    X_train = pd.DataFrame(columns = X.columns)
    X_test = pd.DataFrame(columns = X.columns)
    y_train = pd.DataFrame(columns = y.columns)
    y_test = pd.DataFrame(columns = y.columns)
  
    for artist in df.username.unique():

        df_artist = df[df.username==artist]

        Xa = df_artist[list(X.columns)]
        ya = df_artist['likesCount']

        X_a_train, X_a_test, y_a_train, y_a_test = train_test_split(Xa, ya, test_size=0.20) 

        X_train = X_train.append(X_a_train, ignore_index = True)
        X_test = X_test.append(X_a_test, ignore_index = True)
        y_train = y_train.append(y_a_train, ignore_index = True)
        y_test = y_test.append(y_a_test, ignore_index = True)
    
    return X_train, X_test, y_train, y_test