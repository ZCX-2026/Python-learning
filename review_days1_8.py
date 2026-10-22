# -*- coding: utf-8 -*-
"""
Python 复习总纲（第 1~8 天）
用法：在 PyCharm 里直接运行这个文件，一行行看打印结果，对照注释复习。
电气味例子：电压、节点、电流。
"""

# ============================================================
# 第 1 块：函数 —— 定义(写菜谱) ≠ 执行(做菜)
# ============================================================
print("===== 第 1 块：函数 =====")


def show_voltage(v):        # <-- def 这一行只是"写菜谱"，函数体现在不会跑
    print(f"这个节点电压是:{v}")


show_voltage(220)           # <-- 这一行才叫"调用"，菜谱才真正执行
show_voltage(380)


def add_head(a, b):         # 参数通过小括号里的变量名接收数据，不依赖 input()
    return a + b            # return 把结果"交出去"，谁调用谁拿到


result = add_head(3, 5)     # 3 传给 a，5 传给 b，返回值被 result 接住
print(result)               # ➜ 8


# ============================================================
# 第 2 块：列表 —— 小盒子，中括号装着
# ============================================================
print("===== 第 2 块：列表 =====")

voltages = [220, 380, 110, 12, 660, 1000, 1500, 2000]
print(len(voltages))        # 长度 ➜ 8
print(sum(voltages))        # 总和
print(max(voltages))        # 最大值 ➜ 2000
print(min(voltages))        # 最小值 ➜ 12

voltages.append(500)        # 在末尾追加
print(voltages)             # 现在多了一个 500

print(660 in voltages)      # in 问"在不在里面" ➜ True
print(999 in voltages)      # ➜ False

# sorted(a) 返回【新列表】，a 不变
new_list = sorted(voltages)
print(new_list)             # 从小到大排好的新列表
print(voltages)             # 原列表还是原顺序，没被动过

# a.sort() 直接改【原列表】，返回值是 None
voltages.sort()
print(voltages)             # 原列表被排好了
print(voltages.sort())      # ➜ None（它自己不返回东西）


# ============================================================
# 第 3 块：循环 —— for 遍历 / while 带刹车；累加初值0、累乘初值1
# ============================================================
print("===== 第 3 块：循环 =====")

total = 0                   # 累加的"篮子"，初值必须是 0
for v in voltages:          # 每个 v 依次是列表里的一个值
    total = total + v       # 这一行在循环里，每圈都执行
print(total)                # 这一行缩进退回到循环外，只执行一次

# while 必须有"刹车"，否则死循环
count = 0
while count < 3:            # 刹车：count 越来越大，早晚不满足条件
    print(f"第 {count} 圈")
    count = count + 1       # 这一行是关键，没有它 count 永远 < 3


# ============================================================
# 第 4 块：输入 + 格式化 f-string（花括号外是文字，花括号内是运算）
# ============================================================
print("===== 第 4 块：输入与格式化 =====")

# input() 永远返回【字符串】，要算数字必须 int()
# name = input("请输入节点名:")
# v = int(input("请输入电压值:"))     # 运行时会停住等你打字

a = 1
b = 4
print(f"{a}/{b}")           # 斜杠在花括号外 → 文字 ➜ 1/4（分数样子）
print(f"{a/b}")             # 斜杠在花括号内 → 运算 ➜ 0.25（小数）
print(f"{a/b:.1%}")         # 百分比，保留 1 位小数 ➜ 25.0%


# ============================================================
# 第 5 块：文件读 —— with open(路径, encoding="utf-8") as f
#          注意：f.read() 和 for line in f 不能混用
# ============================================================
print("===== 第 5 块：文件读写 =====")

# 先写一个演示文件（"w" 会清空重写，write 不会自动加换行）
with open("_复习demo.txt", "w", encoding="utf-8") as f:
    f.write("220\n")
    f.write("380\n")
    f.write("\n")           # 故意写一个空行，用来演示 continue
    f.write("1500\n")

# 再读出来：strip() 脱换行 → 判空 continue → append(int(...))
read_result = []
with open("_复习demo.txt", encoding="utf-8") as f:
    for line in f:                    # 一行一行读
        line = line.strip()           # 脱掉换行符和空格
        if line == "":                # 空行保护：遇空行跳过，别让 int('') 炸
            continue
        read_result.append(int(line)) # 转成数字装进列表
print(read_result)                    # ➜ [220, 380, 1500]，空行没进来


# ============================================================
# 第 6 块：筛选套路 —— 空篮子 → for → if → append
# ============================================================
print("===== 第 6 块：筛选 =====")

high = []                   # 第 1 步：空篮子
for v in read_result:       # 第 2 步：for 遍历
    if v >= 1000:           # 第 3 步：if 过滤条件
        high.append(v)      # 第 4 步：符合的装进篮子
print(high)                 # ➜ [1500]


# ============================================================
# 第 7 块：函数化重构 —— 把"读文件""写报告"提成函数 = 能换数据的工具
# ============================================================
print("===== 第 7 块：函数化重构 =====")


def read_number(filename):
    """读一个每行一个数字的文件，返回数字列表（自动跳过空行）。"""
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            result.append(int(line))
    return result


def write_report(filename, voltages_data, high_data):
    """把统计结果写进文件。"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== 电压统计报告 ===\n")
        f.write(f"共读到:{len(voltages_data)}个电压值\n")
        f.write(f"高压节点:{high_data}\n")
        f.write(f"占比:{len(high_data) / len(voltages_data):.1%}\n")


# 换一个文件，同一套函数照常工作 —— 这就是"工具"的意义
data = read_number("_复习demo.txt")
high_nodes = []
for v in data:
    if v >= 1000:
        high_nodes.append(v)
write_report("_复习报告.txt", data, high_nodes)
print("报告已写出，去 _复习报告.txt 看看")


# ============================================================
# 第 8 块：切片 —— 中括号里的冒号，取头不取尾
# ============================================================
print("===== 第 8 块：切片 =====")

nodes = [220, 380, 110, 12, 660, 1000, 1500, 2000]
# 位置:    0    1    2   3    4     5      6      7

print(nodes[0:3])           # 取位置 0,1,2（3 不取）➜ [220, 380, 110]
print(nodes[:3])            # 省起点 = 从头 ➜ [220, 380, 110]
print(nodes[5:])            # 省终点 = 到尾 ➜ [1000, 1500, 2000]
print(nodes[2:5])           # ➜ [110, 12, 660]

print(nodes[::2])           # 步长 2，隔一个取 ➜ [220, 110, 660, 1500]
print(nodes[::-1])          # 负步长 = 倒着取 ➜ 整个列表反序
print(nodes[6:2:-1])        # 倒着取，终点 2 不取 ➜ [1500, 1000, 660, 12]

# 切片返回【新列表】，原列表不动
cut = nodes[0:2]
print(len(nodes))           # 还是 8，没被切短