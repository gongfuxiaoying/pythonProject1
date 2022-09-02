import yaml
import os

# 获取当前路径
filePath = os.path.dirname(__file__)
print(filePath)

# 获取当前文件的绝对路径
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
print(fileNamePath)

# 获取配置文件的路径
yamlPath = os.path.join(fileNamePath,'config.yaml')
print(yamlPath)

# 修改yaml配置
with open(yamlPath,'r',encoding='utf-8') as f:
    # print(f.read())
    result = f.read()
    x = yaml.load(result,Loader=yaml.FullLoader)
    print(type(x))
    print(x)
    print(x['metadata']['name'])

    # 修改的值
    x['metadata']['name'] = 'linux-node02'
    print(x)
    with open(yamlPath,'w',encoding='utf-8') as w_f:
        # 覆盖原先的配置文件
        yaml.dump(x,w_f)