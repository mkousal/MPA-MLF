import numpy as np
import pandas as pd
import glob, os, re

# Add path to lines below!!

train_files_path = "xxxxx/Dataset/Train/CSV/*.csv"
test_files_path = "xxxxx/Dataset/Test/CSV/*.csv"

train_files = glob.glob(train_files_path)
test_files = glob.glob(test_files_path)

train_files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])
test_files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

# Add path here!!
y_train_file = glob.glob("xxxxx/Dataset/y_train.csv")

x_train_files = []
x_test_files = []
for file_ in train_files:
  df = pd.read_csv(file_, index_col=None, header=0)
  x_train_files.append(df.to_numpy())
  print("Done " + str(file_))

for file_ in test_files:
  df = pd.read_csv(file_, index_col=None, header=0)
  x_test_files.append(df.to_numpy())
  print("Done " + str(file_))

x_train = np.stack(x_train_files)
x_test = np.stack(x_test_files)

np.save("/x_train", x_train)
np.save("/x_test", x_test)