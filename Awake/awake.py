'''
    File name: awake.py
    Author: Ojaswy Akella
    Date created: 03/23/2019
    Python Version: 3.6.8
'''
from datetime import datetime
import pytz
import h5py
import pandas as pd
import h5py
from scipy.signal import medfilt
import matplotlib.pyplot as plt
import numpy as np

file = '1541962108935000000_167_838.h5'
#File should be in the same directory as the code
#TASK I
print ('\nTASK I:\n')
cern_time=pytz.timezone('Europe/Zurich')
unix_time=float(file[:18])/100000000
utc=datetime.utcfromtimestamp(unix_time)
print("Time in UTC is",utc)
cern=pytz.utc.localize(utc).astimezone(cern_time)
print("Time in Switzerland/CERN is",cern)

#TASK II
print ('\nTASK II:\n')
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

#TASK III
print ('\nTASK III:\n')
with h5py.File(file, 'r') as f:
		img_dset = f['/AwakeEventData/XMPP-STREAK/StreakImage/streakImageData']                
		imgwidth = f['/AwakeEventData/XMPP-STREAK/StreakImage/streakImageWidth'][0]       
		imgheight = f['/AwakeEventData/XMPP-STREAK/StreakImage/streakImageHeight'][0]       
		image = np.reshape(img_dset,(imgheight,imgwidth))
		filtered_image = medfilt(image)
		fig = plt.figure(figsize=(6,6))  
		plt.imshow(filtered_image)	
		plt.savefig('image.png')
		print('Saved as image.png')
		
