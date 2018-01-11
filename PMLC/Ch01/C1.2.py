import numpy as np
from sklearn import preprocessing


data = np.array([[3, -1.5, 2, -5.4],
                 [0, 4, -0.3, 2.1],
                 [1, 3.3, -1.9, -4.3]])

data_standardized = preprocessing.scale(data)
print(data_standardized.mean(axis=0))
print(data_standardized.std(axis=0))

data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(data)
print(data_scaled)

data_normalized = preprocessing.normalize(data, norm='l1')
print(data_normalized)

data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)
print(data_binarized)

encoder = preprocessing.OneHotEncoder()
encoder.fit([[0, 2, 1, 12],
             [1, 3, 5, 3],
             [2, 3, 2, 12],
             [1, 2, 4, 3]])
encoder_vector = encoder.transform([[2, 3, 5, 3]]).toarray()
print(encoder_vector)

