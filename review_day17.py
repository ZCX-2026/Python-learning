# -*- coding: utf-8 -*-
"""
复习总结 · 第 17 天（2026-10-31）

今天做了一次第 1~8 天的闭卷自测（12 题），暴露 3 个洞，然后学了 try/except。

  1. 订正：sorted 返回新列表；a.sort() 改原列表并返回 None
  2. 订正：f.read() 和 for line in f 不能混用（磁带放到底了）
  3. 订正：append 缩进在循环外 → 只执行一次
  4. 新课：try / except 兜底，pass 与 continue 的危险差别
  5. 完整程序：读带坏行和带小数的 CSV → 清洗 → 统计

运行方式：直接跑。会生成 _demo_day17.csv
"""

# ============================================================
# 1. 订正：sorted 与 .sort()（今天自测错的那个）
# ============================================================
print("===== 1. sorted 与 .sort() =====")

a = [3, 1, 2]
print(sorted(a))     # [1, 2, 3]  ← 复印一份来排序，交给你新列表
print(a.sort())      # None       ← 把原件重排，但什么都不交给你
print(a)             # [1, 2, 3]  ← 原件已经被排好了

# 记忆法：
#   sorted(a)  只交货不动手 → 返回新列表
#   a.sort()   动手不交货   → 返回 None


# ============================================================
# 2. 订正：f.read() 和 for line in f 不能混用
# ============================================================
print("===== 2. read 与 for 不能混用 =====")

with open("_demo_day17.csv", "w", encoding="utf-8") as f:
    f.write("节点A,220\n")
    f.write("节点B,380\n")

# 想成录音带：read() 一口气放到底，磁带停在末尾
with open("_demo_day17.csv", encoding="utf-8") as f:
    data = f.read()          # 读完了，指针在末尾
    for line in f:
        print("这一行永远不会执行：", line)

print(data)                  # 内容都在 data 里
# 结论：read() 和 for line in f 二选一，别混着用。


# ============================================================
# 3. 订正：append 缩进放错层
# ============================================================
print("===== 3. append 放错层 =====")

result = []
with open("_demo_day17.csv", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        result.append(parts[0])      # ← 在循环里，每行加一次

print(result)                        # ['节点A', '节点B']

# 如果把上面这行 append 缩进退到 for 外面：
#   只执行一次，而且用的是循环结束后 line 的值
#   → 结果只有一条（甚至可能 int("") 报错）


# ============================================================
# 4. 新课：try / except
# ============================================================
print("===== 4. try / except =====")

for s in ["220", "12.5", "节点A", ""]:
    try:
        print(f"{s!r:12} → 转成功: {float(s)}")
    except ValueError:
        print(f"{s!r:12} → 转不了，跳过")

# 执行逻辑：
#   进入 try → 没出错就往下走，跳过 except
#   哪行出错 → 立刻跳到 except，try 里剩下的行不再执行
#   执行完 except → 继续往下，程序不崩


# ============================================================
# 5. 重点：pass 与 continue 的差别（会悄悄错位！）
# ============================================================
print("===== 5. pass 还是 continue =====")

# 错误写法（危险）：
#     try:
#         v = float(parts[1])
#     except ValueError:
#         pass                     ← 出错了但继续往下走
#     names.append(parts[0])       ← 名字进了篮子
#     voltages.append(v)           ← 电压却是"上一圈留下的 v" → 错位！
#
# 正确写法：
#     except ValueError:
#         continue                 ← 整行丢弃，名字和电压都不收
#
# 一句话：pass = 出错了还接着走（危险）；continue = 这行不要了（安全）。


# ============================================================
# 6. 完整程序：带坏行、带小数的 CSV → 清洗 → 统计
# ============================================================
print("===== 6. 完整程序 =====")


def count_over(values, limit):
    """数一数列表里有几个数 >= limit。"""
    count = 0
    for v in values:
        if v >= limit:
            count = count + 1
    return count


# 造一份脏数据：空行、没逗号、空电压、多一段、带小数，全齐
with open("_demo_day17.csv", "w", encoding="utf-8") as f:
    f.write("节点A,220\n")
    f.write("节点B,380\n")
    f.write("\n")                  # 脏：空行
    f.write("节点C,1500\n")
    f.write("220\n")               # 脏：没逗号
    f.write("节点D,\n")            # 脏：电压空
    f.write("节点E,660,合格\n")     # 脏：多一段
    f.write("节点F,12.4\n")        # 干净，但带小数

names = []          # 篮子建在循环外面
voltages = []

with open("_demo_day17.csv", encoding="utf-8") as f:
    for line in f:
        line = line.strip()                 # 脱
        if line == "":                      # 岗一：空行
            continue
        parts = line.split(",")             # 切
        if len(parts) != 2:                 # 岗二：段数不对
            continue
        try:                                # 岗三：转成小数，转不了就丢整行
            v = float(parts[1])
        except ValueError:
            continue
        names.append(parts[0])              # 取
        voltages.append(v)

print(names)        # ['节点A', '节点B', '节点C', '节点F']
print(voltages)     # [220.0, 380.0, 1500.0, 12.4]
print(f"平均电压:{sum(voltages) / len(voltages):.2f}")   # 528.10
print(f"高压节点(>=1000):{count_over(voltages, 1000)} 个")  # 1 个


print()
print("===== 第 17 天小结 =====")
print("1. sorted 返回新列表；a.sort() 改原列表并返回 None")
print("2. f.read() 和 for line in f 不能混用（磁带放到底了）")
print("3. append 缩进在循环外 → 只执行一次")
print("4. try/except 兜底：转得动就收，转不动就跳过")
print("5. except 里用 continue 不用 pass，否则两个列表悄悄错位")
print("6. 三道岗：空行 → 段数 → try转小数")