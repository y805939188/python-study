# 数值
#   int
#   float
# 布尔
# 字符串
#   str
# 列表
#   list
# 元组
#   tuple
# 集合
#   set
# 字典
#   dict
ding = 0;
print(type(ding)); # <class 'str'>
ding = 1;
print(type(ding)); # <class 'int'>
ding = 1.1;
print(type(ding)); # <class 'float'>
ding = [1,2,3];
print(type(ding)); # <class 'list'>
ding = (1,2,3);
print(type(ding)); # <class 'tuple'>
ding = {1,2,3};
print(type(ding)); # <class 'set'>
ding = { 'ding1': 666, 'ding2': 888 };
print(type(ding)); # <class 'dict'>

age = 18;
print('丁爷今年%d岁' % age); # 用这种方法做模板字符串
# %s 是指代字符串类型
# %d 是指代有符号的十进制整数
# %f 是指代浮点数
# %c 是指代字符
weight = 53.66666;
print('体重是%.2f' % weight); # %.2f 表示保留2位小数
stu_id = 1;
print('学号是%04d' % stu_id); # %03d 表示中间用三位0补齐

# 或
print(f'学号是{stu_id}'); # 这样也可以

print('hello', end='\n'); # 可以指定结束符号 默认是 \n

# 可以输入s
# res1 = input('请输入\n');
# print(res1);

# # type(int(res1));
# float(res1);
# str(res1);
# print(tuple(res1)); # ('1',)
# print(list(res1)); # ['1']

num1, float1, str1 = 10, 0.5, 'ding';
print(num1); # 10
print(float1); # 0.5 
print(str1); # ding

# 逻辑运算符
# 返回结果和js一样
# and
# or
# not

print(1 < 2 and 2 < 3); # True
"""
这个三引号也是注释
ddddd
"""

if True:
  print(9999);
  ding = 999;
  print(ding);

if False:
  print(1234);
else:
  print(3456);
print(2345); # 能输出 这个是按照缩进来的

if(True): # 不能写大括号哦 会被识别成集合
  { print(98876) }
elif ding:
  ding = 999;
elif 1 <= ding <= 777: # 牛逼 还特么能这么写
  ding = 888;

a = 1;
b = 2;
c = a if a > b else b; # a > b ? a : b
print(c); # 2

i = 1;
while i <= 5:
  print(i);
  i += 1; # python里头没法直接写 i++

str1 = 'dingye';

for i in str1:
  print(i);
else :
  print('whilt和for循环可以和else配合着用 else 里就是当循环正常执行完之后要执行的语句');
  print('如果循环是break了就不会执行');

str2 = 'dingye';
print(str2[1]); # i


# 切片
# 字符串、列表、元组都支持切片操作
# 相当于split 只是最后多了个"步长"
name = '123456';
print(name[2:5:1]); # 345
print(name[2:5]); # 345
print(name[:5]); # 12345
print(name[1:]); # 23456
print(name[0:5:2]) # 135
print(name[0:5:3]) # 14
print(name[::-1]); # 654321

name = 'ding and dingdingding and dingdingdingding and';
print(name.find('and')); # 5 返回下标
print(name.find('and', 10)); # 22 后面的参数表示起始位置
print(name.find('and', 40, 100)); # 43 后面俩参数第三个参数表示结束位置
print(name.find('niubi')); # -1

print(name.index('and')); # 5
# 也有仨参数 和find用法基本一样只不过如果查找的不存在会直接报错

print(name.count('and')) # 3 表示出现的次数
print(name.count('and', 30)) # 1

# 同理还有 rfind 和 rindex

print(name.replace('and', 'niubi', 3)) # 第一个参数表示旧的 第二个表示新的 第三个表示替换次数
print(name.replace('and', 'niubi', 1)) # 如果传1 则只有第一个and会被替换

print(name.split('and')) # ['ding', ' dingdingding ', 'dingdingdingding ', '']
print(name.split('and', 1)) # 第二个参数表示分割次数 这样传1就只有第一个and会被分割

str1 = 'ding1';
str2 = 'ding2';
print(str1.join(str2)); # 合并字符串

print(name.capitalize()); # 首字母大写

print(name.title()); # 所有首字母大写

print(name.lower()); # 所有大写转小写

print(name.upper()); # 所有小写转大写

print(name.lstrip()); # 删除左侧空白字符

print(name.rstrip()); # 删除右侧空白字符

print(name.strip()); # 删除两侧空白字符

print(name.ljust(100, '.')); # 在100个字符内 居左对齐 超出的地方用 . 占位

print(name.rjust(100, '.')); # 在100个字符内 居右对齐 超出的地方用 . 占位

print(name.center(100, '.')); # 在100个字符内 居中对齐 超出的地方用 . 占位

print(name.startswith('x')); # 判断是否以x开头

print(name.endswith('x')); # 判断是否以x结尾

name = 'dddddd';
print(name.isalpha()); # 是否所有字符都是字母
print(name.isalnum()); # 是否所有字符都是num或字母
print(name.isdigit()); # 是否所有字符都是num
print(name.isspace()); # 是否所有字符都是空格


ding = [1, 2, 3, 4, 5]; # 一个列表
print(ding.index(2)) # 1
print(ding.count(1)) # 1 看1出现了几次
print(len(ding)) # 5 len对 字符串 列表 字典 和元组是公共方法
print(len('ding')) # 4

print('2' not in ding)
print(2 in ding) # 判断xx是否存在于列表中

ding.append([6])
print(ding) # 增加
ding.extend([6])
print(ding) # 会把列表拆开再添加 就等于 ding.append(6) 或 ding.append(6)
ding.insert(1, 'ding')
print(ding) # 插入

del(ding[1]) # 删除列表
print(ding)
del(ding); # 可以删除列表

ding = [1, 2, 3, 4, 5]; # 一个列表
print(ding.pop()) # 5
print(ding) # pop会影响原列表
print(ding.pop(2)) # 可以删除指定索引 相当于把index=2的删掉
ding.reverse()
print(ding) # 反向
ding.sort()
print(ding) # 默认升序排序
# ding.sort(key=xxxx, reverse=bool) # 可以传参 根据某个key排序 并按照升序降序排列
ding.sort(reverse=False)
ding.sort(reverse=True)
ding1 = ding.copy() # 负责一份儿
print(ding1)
ding2 = [1, 2, 3]
ding3 = [ding2, 4, 5]
ding4 = ding3.copy() # 浅拷贝
ding4[0][1] = 666
print(ding4)
print(ding2) # copy是浅拷贝

for i in ding4:
  print(i)


# 元组
ding1 = (1, 2, 3, 6, 5, 6)
print(len(ding1))
print(ding1[3])
# ding1[3] = 666 元组内的东西不能被修改
print(ding1.index(6)) # 5
print(ding1.count(6)) # 2

# 字典
ding1 = { "ding1": 666, "ding2": 888 }
print(ding1) # 字典相当于js对象 但是key必须加引号
print(ding1.get('ding1')) # 666
print(ding1.get('niubi')) # None
print(ding1.keys()) # dict_keys(['ding1', 'ding2'])
print(ding1.values()) # dict_values([666, 888])
print(ding1.items()) # dict_items([('ding1', 666), ('ding2', 888)])

for key in ding1.keys():
  print(key)
for value in ding1.values():
  print(value)
for item in ding1.items():
  print(item)

# 集合
ding1 = {1, 2, 3, 4, 5, 6} # 集合中的数据会自动去重的
print(set('123456')) # 会随机顺序生成123456的集合
print(type(set('666'))) # <class 'set'> 注意 直接用{} 创建set的话 type会返回 dist
print(set('666'))
ding1.add(7) # 追加单个值
print(ding1)
# ding1.add([8,9]) 报错
ding1.update([7,8,9]) # 追加序列
print(ding1)
ding1.remove(7) # 追加序列 指定数据不存在会报错
print(ding1)
ding1.discard(8) # 追加序列 指定数据不存在不会报错
print(ding1)
print(ding1.pop()) # 删除第一位数据并返回
print(ding1)
print(2 in ding1)

# 列表和元组 支持 + *
print([1,2,4] + [4,5,6]) # [1,2,3,4,5,6]
print((1,2,4) + (4,5,6)) # (1,2,3,4,5,6)
# print([1,2,4] + (4,5,6)) # 报错
# print({ ding1: 666 } + { ding2: 888 }) 报错
# print({1,2,4} + {4,5,6}) # 报错

print([1,2,4] * 2) # [1, 2, 4, 1, 2, 4]
print((1,2,4) * 2) # (1, 2, 4, 1, 2, 4)

# 公共方法
# len()
# del 或 del()
# max()
# min()
# range(start, end, step) 生成从start到end的数字 步长为step 供for循环使用
# enumerate(可遍历对象, start=0) 返回元组 (index, value) 一般在for循环中使用
for i in range(1, 10, 2):
  print(i) # 打印 1 3 5 7 9

for i in enumerate([1, 3, 5]):
  print(i) # 打印 (0, 1) (1, 3) (2, 5)

print('------')

for i in enumerate([1, 3, 5], 2): # 第二个参数表示索引从几开始
  print(i) # 打印 (2, 1) (3, 3) (4, 5)

ding1 = [1,2,3,4]
ding2 = {1,2,3,4}
ding3 = (1,2,3,4)

# 元组、列表、集合 这仨 可以相互转换
print(tuple(ding1))
print(tuple(ding2))
print(list(ding2))
print(list(ding3))
print(set(ding1))
print(set(ding3))

# 推导式
# 只要 列表、字典、集合 这仨具有推导式
# 用一个表达式创建一个有规律的列表或控制一个有规律的列表

list1 = [ i for i in range(10) ] # 列表推导式 生成一个包含1~10的列表
print(list1)
print(i for i in range(10)) # 这个也能打印出来 是一个可迭代的对象
list2 = [ i for i in range(10) if i % 2 == 0 ] # 推导式可带if
print(list2) # [ 0, 2, 4, 6, 8 ]
list3 = [ (i, j) for i in range(1, 3) for j in range(5, 7) ] # 可以多for循环
print(list3) # [(1, 5), (1, 6), (2, 5), (2, 6)]


# 字典推导式
# 快速合并列表为字典或提提取字典中目标数据
dict1 = { i: i**2 for i in range(5) }
print(dict1) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
dict2 = { list1[i]: list2[i] for i in range(len(list1)) }
print(dict2) # {1: 6, 2: 7, 3: 8, 4: 9, 5: 0}
dict3 = { "ding1": 1, "ding2": 2, "ding3": 3 }
print({ key: value for (key, value) in dict3.items() if value == 1 }) # {'ding1': 1}

# 集合推导式
list1 = [1,2,3]
set1 = { i ** 2 for i in list1 }
print(set1) # {1, 4, 9}






# def 函数
def funcName(args):
  """
    这里是函数的说明文档 必须是第一行且用多行注释的方式
    :param a: 参数1
    :param b: 参数2
  """;
  print(args);
  return args + '6666';

print(funcName('dingye')) # dingye6666

# 关键字参数
def testName1(a, b, c = 666): # 也可以给参数默认值
  print(a)
  print(b)
  print(c)
testName1(b = 1, a = 2) # 可以通过定义关键字的方式打乱传参顺序

def testName2(*args): # 变长参数
  print(args); # (1,2,3)
testName2(1,2,3)

def testName3(**args): # 变长参数
  print(args); # (1,2,3)
testName3(a=1,b=2,c=3) # {'a': 1, 'b': 2, 'c': 3}

# 元组拆包
def testName4():
  return 1, 2;
print(testName4()) # (1, 2)
num1, num2 = testName4()
print(num1, num2)

# 字典拆包
dict1 = { 'ding1': 111, 'ding2': 222 }
item1, item2 = dict1;
print(item1, item2) # ding1 ding2

a = 1;
b = 2;
a, b = b, a;
print(a, b)
[a, b] = [b, a];
print(a, b)
(a, b) = (b, a);
print(a, b)

# id
a = 1;
print(id(a)) # id() 返回的值相当于是内存中的地址(十进制表示的)
b = [1]
c = b
print(id(b), id(c))
c[0] = 66
print(b)

# 把引用类型作为参数的话传进来也是引用类型
def test(a):
  a += a;
  print(a);
  print(id(a));

d = [1, 2, 3]
test(d);
print(d)
print(id(d))

# 可变类型: 列表、字典、集合
# 不可变累心: 整数、浮点数、字符串、元组
