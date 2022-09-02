# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):
    desktop_path = "d:\\temp\\333\\"  # 新创建的txt文件的存放路径
    with open("d:\\temp\\333\\name.txt", "r", encoding='utf-8') as f:
        for line in f:
            print(line)
            full_path = desktop_path + line.strip("\n") + '.txt'  # 也可以创建一个.doc的word文档
            file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    # file.close()


text_create('mytxtfile', 'Hello world!')
# 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!


