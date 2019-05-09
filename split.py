from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
import io

from rasa_nlu import training_data, utils, config


data = "data33.json"

# load the training data
data = training_data.load_data(data)
# split into test & train
data_train, data_test = data.train_test_split()

with io.open('test.md', 'w', encoding="utf-8") as f:
    f.write(data_test.as_markdown())

with io.open('train.md', 'w', encoding="utf-8") as f:
    f.write(data_train.as_markdown())
