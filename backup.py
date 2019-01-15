# 把设置好路径的文件打包成压缩文件，打包名称是时间和自己的评论


import os
import time


# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Windows 下：
# source = ['"C:\\My Documents"', 'C:\\Code']
# 又例如在 Mac OS X 与 Linux 下：
source = ['/Users/bigphess/backup']
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称。

#2. 备份文件必须存储在一个
#主备份目录中
#例如在 Windows 下：
# target_dir = 'E:\\Backup'
# 又例如在 Mac OS X 和 Linux 下：
target_dir = '/Users/bigphess/backup2'
# 要记得将这里的目录地址修改至你将使用的路径

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录


# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter a comment ---->')


# 给日期的最后加上相应的评论，把comment里面的空格换成下划线
if len(comment) == 0:
	target =  today + os.sep + now + '.zip'
else:
	target =  today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'



# 如果目标目录还不存在，则进行创建
if not os.path.exists(today):
    os.mkdir(today)  # 创建目录
    print('Successful create directory',today)

# 5. 我们使用 zip 命令将文件打包成 zip 格式。通过zip触发了压缩，-r表示递归的进行压缩
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
# 这里真的执行程序
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')