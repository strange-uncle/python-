def read1():
    with open('E:\Github\practise_file_operation\中文目录\新建文本文档.txt','r') as f:
        print(f.read())


def read2():
    with open('E:\Github\practise_file_operation\中文目录\新建文本文档.txt', 'r') as f:
        for l in f:
            print(l)


def read3():
    with open('E:\Github\practise_file_operation\中文目录\新建文本文档.txt','r') as f:
        lines = f.readlines()
    # 下面的代码可以访问上面WITH里面的lines
    print(lines)
    
    
def print_test_txt():
    with open('E:\\Github\\practise_file_operation\\中文目录\\test.txt', 'r') as f:
        print('here is result:')
        print(f.readlines())


def read_write():
    with open('E:\\Github\\practise_file_operation\\中文目录\\test2.txt', 'r+') as f:
        print(f.readlines())
        f.seek(0)
        print(f.read())
        f.seek(0)
        f.write('666')

 
def w_plus():
    with open('E:\\Github\\practise_file_operation\\中文目录\\test.txt', 'w+') as f:
        f.write('999')
         

# a+是append下的读写模式. 和r+不同的是， a+在读取文件的时候会把文件指针放到文件末尾，
# 所以需要调用seek来移动文件的读取指针到第一个位置，然后才能读取出前面的内容
def append_plus():
    with open('E:\\Github\\practise_file_operation\\中文目录\\test.txt', 'a+') as f:
        print('a+ mode, read first then write.')
        # nothing
        f.read()
        f.seek(0)
        print(f.readlines())
        # seek移动文件指针，影响了接下来的写入操作
        f.seek(0)
        f.write('999')


# as a means append, so get error: UnsupportedOperation: not readable
def append_read():
    with open('E:\\Github\\practise_file_operation\\中文目录\\test.txt', 'a') as f:
        print(f.readlines())
  

def replace_pic():
    with open('E:\Github\practise_file_operation\中文目录\A.jpg','wb') as f1:
        with open('E:\Github\practise_file_operation\中文目录\B.jpg', 'rb') as f2:
            d2 = f2.read()
        f1.write(d2)
    
    
if __name__ == '__main__':
    # read1()
    # read2()
    # read3()
    # read_write()
    # w_plus()
    # append_plus()
    # read_write()
    # append_plus()
    # print_test_txt()
    # append_read()
    # replace_pic()
    pass
