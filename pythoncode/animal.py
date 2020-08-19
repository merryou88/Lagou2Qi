# 创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
import yaml


class Animal:
    name: 'default'
    color: 'default'
    age: 1
    sex: 'default'

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def call(self):
        print(f'{self.name} could call')

    def run(self):
        print(f'{self.name} could run')


# 创建子类【猫】，继承【动物类】
# - 复写父类的__init__方法，继承父类的属性，
#
# - 添加一个新的属性，毛发=短毛，
#
# - 添加一个新的方法， 会捉老鼠，
#
# - 复写父类的‘【会叫】的方法，改成【喵喵叫】
class Cat(Animal):
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.maofa = 'duanmao'

    def catch_mouse(self):
        print(f'{self.name} could catch mouse')

    def call(self):
        # super(Cat, self).call()
        print(f"{self.name} could  miaomiao call")


# 创建子类【狗】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属性，
#
# - 添加一个新的属性，毛发=长毛，
#
# - 添加一个新的方法， 会看家，
#
# - 复写父类的【会叫】的方法，改成【汪汪叫】
class Dog(Animal):
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.maofa = 'changmao'

    def look_home(self):
        print(f'{self.name} could look after home')

    def call(self):
        print(f"{self.name} could wangwang call")


# 创建一个猫猫实例
# - 调用捉老鼠的方法
#
# - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
with open('animal.yml') as f:
    datas = yaml.safe_load(f)

dog_info = datas['dog']
cat_info = datas['cat']
# print(datas)
# print(dog_info)
mycat = Cat(cat_info['name'], cat_info['color'], cat_info['age'], cat_info['sex'])
mycat.catch_mouse()
print(f'{mycat.name} 颜色是：{mycat.color} 年龄是：{mycat.age} 性别是：{mycat.sex} 毛发是：{mycat.maofa}.捉到了老鼠')

# 创建一个狗狗实例
# - 调用【会看家】的方法
#
# - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
mydog = Dog(dog_info['name'], dog_info['color'], dog_info['age'], dog_info['sex'])
mydog.look_home()
print(f'{mydog.name},颜色：{mydog.color} 年龄：{mydog.age} 性别：{mydog.sex} 毛发：{mydog.maofa}')
