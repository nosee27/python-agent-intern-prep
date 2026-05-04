#描述符：实现了 __get__、__set__、__delete__ 的类。
class Descriptor:
    def __get__(self,instance,owner):
        print(f"获取{instance}的属性")
        return instance._value
    def __set__(self,instance,value):
        print(f"设置{instance}的属性为{value}")
        instance._value=value
class MyClass:
    atter=Descriptor()
    def __init__(self):
        self._value=None
obj=MyClass()
obj.atter=10
print(obj.atter)
