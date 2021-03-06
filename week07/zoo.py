class

class Cat(Zoo):
    # 类属性
    yell = 'meow'

    def __init__(self, name,tpye,somatotype,nature):
        # 普通字段
        self.name = name
        self.type = type
        self.somatotype = somatotype
        self.nature = nature

class Dog(Zoo):
    # 类属性
    yell = 'woof'

    def __init__(self, name,tpye,somatotype,nature):
        # 普通字段
        self.name = name
        self.type = type
        self.somatotype = somatotype
        self.nature = nature

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')


'''
定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
'''

'''
动物类以虚基类来实现，
猫和狗分别继承动物类
动物类为名字属性和添加动物方法
'''