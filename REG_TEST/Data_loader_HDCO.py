# This Code loads any type of data into Data Arrays (NP or PD)


#These are TF specific functions for saving and printing
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd
import tensorflow as tf

#import xlrd

# Paths and Data Description here
DATA_FILE_TRAIN = "F:\PiyushWS\data\HD_CO_train.csv"
DATA_FILE_TEST = "F:\PiyushWS\data\HD_CO_test.csv"

CSV_COLUMN_NAMES = ['URBAN','RURAL','AGE_under5','AGE_5_9',
                    'AGE_10_14','AGE_15_19','AGE_20_24','AGE_25_29',
                    'AGE_30_34','AGE_35_39','AGE_40_44','AGE_45_49',
                    'AGE_50_54','AGE_55_59','AGE_60_64','AGE_65OVER',
                    'MALE','FEMALE','WHITE','AFR_AMER','AMIALASKA','ASIAN',
                    'HAWAIIANPI','OTHERRACE','HISPANIC_LATINO','NONHISPANIC_WHITE',
                    'MINORITY','E_EDU_LESS_9GRADE','E_EDU_9_12GRADE','E_EDU_HIGHSCHOOL',
                    'E_EDU_SOMECOLLEGE','E_EDU_ASSOCIATES','E_EDU_BACHELORS','E_EDU_GRADPROF',
                    'E_MEDHOUSEHOLD_INCOME','E_PERCAPITA_INCOME','Smoker','Obese','HealthDistress',
                    'PhyInactivity','OWNOCC_HOUSING_UNITS','RENTOCC_HOUSING_UNITS', 'Y']

#OUTPUT_LABELS = ['A']S

# this code reads data into an NDArray from the .xls file
"""
DATA_FILE = "F:\PiyushWS\TF_TEST\LR1\data\data.xlsx"
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1
print(data)
"""

# this code reads data into PD DF
def load_data(y_name) :

    train_path = DATA_FILE_TRAIN
    test_path = DATA_FILE_TEST

    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)

# This code converts features and lables into a Dataset
def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset

# This code converts features and lables into a Dataset
def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset


if __name__ == "__main__":
    # run the code here
    print(load_data('Y'))

