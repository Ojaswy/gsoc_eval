import h5py
from scipy.signal import medfilt
import matplotlib.pyplot as plt
import numpy as np

file='1541962108935000000_167_838.h5'
	
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