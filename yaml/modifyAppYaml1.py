import yaml
import os

######修改yaml文件内容

def changeYamlConfig(path, key, value):
    with open(path, 'r', encoding='utf-8') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
        f.close()
    with open(path, 'w', encoding='utf-8') as f:
        flag = 0
        for line in lines:
            if key in line and '#' not in line:
                leftstr=line.split(":")[0]
                newline = "{0}: {1}".format(leftstr, value)
                line = newline
                f.write('%s\n' % line)
                flag = 1
            else:
                f.write('%s' % line)
        f.close()
        return flag

# 获取当前文件的绝对路径
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
print(fileNamePath)

# 获取配置文件的路径
yamlPath = os.path.join(fileNamePath,'application.yml')
print(yamlPath)
changeYamlConfig(yamlPath,"active:","cccc")