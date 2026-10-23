# -*- coding: utf-8 -*-
"""
复习总结 · 第 9~10 天（2026-10-23）

今日主题：
  1. 排序：sorted 与 .sort() 的区别、reverse=True、返回 None 的那一个
  2. 切片边界：取头不取尾、"位置"和"第几个"差 1
  3. 完整程序：从空白文件写出 读文件 → 排序 → 取前 3 → 写报告
  4. 两个概念：return 是"交货"；判空只在"数据进门"时做一次

运行方式：直接跑。会自动生成 _demo_nodes.txt 和 _demo_report.txt
"""

# ============================================================
# 1. 排序：sorted 与 .sort()
# ============================================================
print("===== 1. 排序 =====")

nodes = [220, 380, 110, 12, 660, 1000, 1500, 2000]

print(sorted(nodes))                  # 新列表，从小到大；原列表不动
print(sorted(nodes, reverse=True))    # 新列表，从大到小
print(nodes)                          # 还是原来的顺序，没被动过

print(nodes.sort())                   # None：它改原列表，但"不交货"
print(nodes)                          # 现在原列表本身被排成升序了

# 一句话：sorted 只交货不动手；.sort() 动手不交货。
# 所以  x = nodes.sort()  之后，x 是 None，不是列表。


# ============================================================
# 2. 切片边界：取头不取尾
# ============================================================
print("===== 2. 切片边界 =====")

nodes = [220, 380, 110, 12, 660, 1000, 1500, 2000]
# 位置:   0    1    2    3    4     5      6      7
# 第几个: 1    2    3    4    5     6      7      8
# 口诀：位置 = 第几个 - 1

print(nodes[1:4])   # [380, 110, 12]      位置 1,2,3；终点 4 不取
print(nodes[5:])    # [1000, 1500, 2000]  从位置 5 一直到尾
print(nodes[:4])    # [220, 380, 110, 12] 从头取到位置 3
print(nodes[4:])    # [660, 1000, 1500, 2000] 从位置 4（660）开始


# ============================================================
# 3. 完整程序：读文件 → 排序 → 取前 3 → 写报告
# ============================================================
print("===== 3. 完整程序 =====")

# 3.0 先造一个数据文件，保证这段代码在任何电脑上都能跑
#     write 不会自动换行，所以每行末尾要自己补 \n
with open("_demo_nodes.txt", "w", encoding="utf-8") as f:
    for v in [230, 400, 115, 12, 690, 1050, 1600, 2100]:
        f.write(f"{v}\n")


def read_number(filename):
    """读文件：一行一个数字，返回列表；空行自动跳过。"""
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()          # 先脱换行
            if line == "":               # 再判空（顺序不能反）
                continue
            result.append(int(line))     # 最后转数字装进篮子
    return result                        # return 在循环外：交出一整个列表


def write_report(filename, nodes):
    """写报告：把统计结果写进新文件。注意：不 return，所以返回 None。"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== 节点巡检报告 ===\n")
        f.write(f"共读到:{len(nodes)}个节点\n")
        f.write(f"最高电压:{max(nodes)}\n")
        f.write(f"最低电压:{min(nodes)}\n")
        f.write(f"重点巡检节点:{nodes[:3]}\n")


data = read_number("_demo_nodes.txt")
data.sort(reverse=True)                  # 从高到低
write_report("_demo_report.txt", data)   # 没有 return，所以不加 =
print("报告已写入 _demo_report.txt")


# ============================================================
# 4. 两个概念
# ============================================================
print("===== 4. 两个概念 =====")

# 概念一：return 是"交货"。
# 有 return → 用 = 接住；没有 return → 干完活交出来的是 None。
x = write_report("_demo_report.txt", data)
print(x)        # None

# 概念二：判空只在"数据进门"时做一次。
#   read_number 处理的是外部文件，可能有空行 → 必须 strip + continue
#   write_report 里的内容是自己造的字符串 → 没有脏数据要防

# 概念三（边界）：空列表时，len 是 0，max/min 会被卡住
empty = []
print(len(empty))    # 0，安全
# print(max(empty))  # 取消注释会报错：max() 不接受空序列
# 所以写报告前，先想一句：这批数据会不会是空的？


print()
print("===== 今日要点 =====")
print("1. sorted 返回新列表；.sort() 改原列表且返回 None")
print("2. 切片取头不取尾；位置 = 第几个 - 1")
print("3. 完整程序 = 读 → 处理 → 写，每一步一个小函数")
print("4. 有 return 才用 = 接；没有 return 得到 None")
print("5. 判空只做在数据进门的地方")