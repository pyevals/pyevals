def build(X_train, X_test, y_train, y_test=None, method=None,
          samples_size=None,
          number_of_independant_columns=None,
          figsize=None,
          ax=None):

    if y_test is not None:
        X_train = np.array(X_train)
        X_test = np.array(X_test)
        y_train = np.array(y_train)
        y_test = np.array(y_test)

        if method == "Regression":
            print("\n-----------------------\033[1mModels\033[0m-------------------------\n")
            a = linear_regression(X_train,
                                  X_test,
                                  y_train,
                                  y_test,
                                  samples_size=samples_size,
                                  number_of_independent_columns=number_of_independant_columns)
            print("\033[1mLinear Regression: \033[0m {}".format(a))
            return a
        elif method == "CLassification":
            print("\033[1mDecisionTreeClassifier: \033[0m {}".format(decisiontree(X_train,
                                                                                  X_test,
                                                                                  y_train,
                                                                                  y_test,
                                                                                  max_depth=6,
                                                                                  min_samples_leaf=6,
                                                                                  criterion="gini")))

