from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def get_poly_pred(x_train, x_test, y_train, degree=1):

    # Generate polynomial features on the train data
    x_poly_train= PolynomialFeatures(degree=degree).fit_transform(x_train)

    # Generate polynomial features on the test data
    print(x_train.shape, x_test.shape, y_train.shape)
    x_poly_test= PolynomialFeatures(degree=degree).fit_transform(x_test)

    # Initialize a model to perform polynomial regression
    polymodel = LinearRegression()

    # Fit the model on the polynomial transformed train data
    polymodel.fit(x_poly_train, y_train)

    # Predict on the entire polynomial transformed test data
    y_poly_pred = polymodel.predict(x_poly_test)
    return y_poly_pred