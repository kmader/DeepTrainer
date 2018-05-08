from keras.datasets import cifar10, mnist
# download the data
cifar10.load_data();
mnist.load_data();
import keras.applications as apps
for c_app in dir(apps):
    try:
        # initialize the model
        apps.__getattribute__(c_app)(include_top = False)
    except Exception as e:
        print('{} complained that {}'.format(c_app, e))
