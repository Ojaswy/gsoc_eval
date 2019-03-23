import h5py
import pandas as pd

file = '1541962108935000000_167_838.h5'
file_read = h5py.File(file, 'r')

data = {}

def get(path, element):
  if isinstance(element, h5py.Dataset):
    try:
      data_type = element.dtype
    except Exception as e:
      data_type = str(e)
    data[path] = ['Dataset', element.size, element.shape, data_type]
  else:
    data[path] = ['Group', '','','']

file_read.visititems(get)

df = pd.DataFrame.from_dict(data,orient='index',
    columns=['Element-type','Size','Shape','Data-type'])
df.to_csv('data.csv', sep=',')
print ('Data saved under data.csv')