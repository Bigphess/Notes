# import os
# import time

# # 1. 需要备份的文件与目录将被
# # 指定在一个列表中。
# # 例如在 Windows 下：
# # source = ['"C:\\My Documents"', 'C:\\Code']
# # 又例如在 Mac OS X 与 Linux 下：
# source = ['/Users/bigphess/backup']
# # 在这里要注意到我们必须在字符串中使用双引号
# # 用以括起其中包含空格的名称。

# #2. 备份文件必须存储在一个
# #主备份目录中
# #例如在 Windows 下：
# # target_dir = 'E:\\Backup'
# # 又例如在 Mac OS X 和 Linux 下：
# target_dir = '/Users/bigphess/backup2'
# # 要记得将这里的目录地址修改至你将使用的路径

# # 3. 备份文件将打包压缩成 zip 文件。
# # 4. zip 压缩文件的文件名由当前日期与时间构成。
# target = target_dir + os.sep + \
#          time.strftime('%Y%m%d%H%M%S') + '.zip'

# # 如果目标目录还不存在，则进行创建
# if not os.path.exists(target_dir):
#     os.mkdir(target_dir)  # 创建目录

# # 5. 我们使用 zip 命令将文件打包成 zip 格式
# zip_command = 'zip -r {0} {1}'.format(target,
#                                       ' '.join(source))

# # 运行备份
# print('Zip command is:')
# print(zip_command)
# print('Running:')
# if os.system(zip_command) == 0:
#     print('Successful backup to', target)
# else:
#     print('Backup FAILED')


import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
ar_dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

while True:
	ret, frame = cap.read()
	corners_o, ids_o, _ = cv2.aruco.detectMarkers(frame,ar_dictionary)
	if corners_o != []:
		print(corners_o)
	# else: continue
	cv2.imshow("try",frame)
	cv2.waitKey(1)
	# print(ret)

# a = np.array([1,2,3,4])
# b = np.array([[1,2],[2,3],[3,4]])
# c = np.array([[[1,3],[2,4]],[[1,3],[2,4]],[[1,3],[2,4]]])

# print(a, np.square(b))
# print(b, b.shape)
# print(c, c.shape)