# Day 12 | 2026-05-05 | @dataclass 与 field

## @dataclass
- 装饰器，自动生成 __init__、__repr__、__eq__
- 必须写类型注解：name: str
- 适合数据容器类，减少样板代码

## field() 关键参数
- default_factory=list：可变默认值，每个实例独立
- repr=False：字段不显示在打印输出中
- compare=False：不参与 == 比较
- init=False：不在 __init__ 参数中

## 为什么 list 不能用 default=[]？
- Python 默认参数只创建一次，所有实例共享
- 用 default_factory=list，每个实例创建时新建列表

