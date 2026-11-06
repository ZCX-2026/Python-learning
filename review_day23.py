# -*- coding: utf-8 -*-
"""
复习总结 · 第 23 天（2026-11-06）  一个完整的程序（范文）

今天没有新知识。这份文件是一整个能跑的程序，从读文件 → 统计 → 写报告。

它把你这 23 天学的都用上了：
  函数、参数、return、多返回值      （Day01-07、Day19、Day21）
  列表、len / sum / max / min      （Day01-08）
  文件读写、"w"、\\n                 （Day01-08）
  strip / 判空 / split / 三道岗     （Day13-17）
  try / except                     （Day17）
  字典、in / get / items 遍历       （Day22-23）
  :.2f 格式化                       （Day16）

你可以把它当模板：以后写新的数据处理程序，照着这个骨架改。

运行方式：直接跑。
  会生成 _demo_day23.csv（输入）和 _demo_day23_report.txt（输出）
"""

# ============================================================
# 第 1 步：造一份演示数据（真实数据里这些脏东西都会出现）
# ============================================================
print("===== 第 1 步：准备数据 =====")


def make_demo_file(filename):
    """写一份带脏数据的演示文件。"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("进线柜,380\n")
        f.write("照明回路,220\n")
        f.write("备用电源,110\n")
        f.write("\n")                 # 脏①：空行
        f.write("水泵,1500\n")
        f.write("风机,\n")            # 脏②：电压是空的
        f.write("电梯,660,合格\n")     # 脏③：多了一段
        f.write("空调,220\n")


make_demo_file("_demo_day23.csv")
print("已生成 _demo_day23.csv（5 条好数据 + 3 条脏数据）")


# ============================================================
# 第 2 步：读文件 → 字典 {名字: 电压}
# ============================================================
print("===== 第 2 步：读文件 =====")


def read_nodes(filename):
    """读 CSV（每行：名字,电压），返回字典 {名字: 电压}。

    四道岗：
      1. 空行            if line == "": continue
      2. 段数不对         if len(parts) != 2: continue
      3. 转不了小数       try / except ValueError
      4. 名字和电压成对   一起进字典（字典本身就不会错位）
    """
    info = {}                             # 空字典，不是空列表
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()           # 脱
            if line == "":                # 岗一
                continue
            parts = line.split(",")       # 切
            if len(parts) != 2:           # 岗二
                continue
            try:
                v = float(parts[1])       # 取
            except ValueError:
                continue                  # 岗三：转不了就整行丢掉
            info[parts[0]] = v            # 存：键 = 名字，值 = 电压
    return info                           # 交回一个字典


info = read_nodes("_demo_day23.csv")
print(info)


# ============================================================
# 第 3 步：统计并打印
# ============================================================
print("===== 第 3 步：统计 =====")


def show_stats(info):
    """打印统计结果。数据为空时直接返回，避免除零。"""
    if len(info) == 0:                    # 边界：空字典
        print("没有读到任何数据")
        return

    count = len(info)
    total = sum(info.values())            # .values() 取出所有电压
    avg = total / count
    max_v = max(info.values())
    min_v = min(info.values())

    print(f"共 {count} 个回路")
    print(f"平均电压:{avg:.2f}")
    print(f"最高电压:{max_v}   最低电压:{min_v}")

    # 最高电压出现在哪个回路？（字典才能做到：知道值，也知道名字）
    for name, v in info.items():
        if v == max_v:
            print(f"最高电压出现在:{name}")


show_stats(info)


# ============================================================
# 第 4 步：写报告文件
# ============================================================
print("===== 第 4 步：写报告 =====")


def write_report(filename, info):
    """把报告写进文件。没有 return，所以调用时不要用 = 接。"""
    if len(info) == 0:
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== 回路电压报告 ===\n")
        f.write(f"共读到:{len(info)}个回路\n")
        f.write("--- 明细 ---\n")
        for name, v in info.items():
            f.write(f"{name}: {v}V\n")
        f.write("--- 汇总 ---\n")
        f.write(f"平均:{sum(info.values()) / len(info):.2f}V\n")
        f.write(f"最高:{max(info.values())}V\n")
        f.write(f"最低:{min(info.values())}V\n")


write_report("_demo_day23_report.txt", info)
print("报告已写入 _demo_day23_report.txt")
print()


# ============================================================
# 第 5 步：把报告读回来看一眼
# ============================================================
print("===== 第 5 步：报告内容 =====")

# 这里用 read() 一口气读完 —— 注意：一个 with 里只能二选一
#   要么 f.read()
#   要么 for line in f
with open("_demo_day23_report.txt", encoding="utf-8") as f:
    print(f.read())


# ============================================================
# 这个程序的骨架，记住这五步
# ============================================================
#
#   ① 准备数据      make_demo_file()
#   ② 读 + 清洗     read_nodes()   → 返回字典
#   ③ 统计          show_stats()   → 打印
#   ④ 写报告        write_report() → 写文件
#   ⑤ 检查结果      读回来看看
#
# 三个函数各干一件事，互不干扰：
#   想换数据源 → 只改第 ② 步
#   想换报告格式 → 只改第 ④ 步


# ============================================================
# 周末可以练的 5 个改造（你有两天没课，挑着做）
# ============================================================
# 1. 把 read_nodes 改成返回"两个列表"（names 和 voltages），
#    体会一下字典和两个列表各自好在哪。
#
# 2. 增加一个"高压回路"的筛选：把电压 >= 1000 的单独列出来，
#    在报告里单开一段。
#
# 3. 增加平均值的四舍五入版本：同时打印两位小数和整数（round）。
#
# 4. 让 write_report 也返回一行摘要文字（return），
#    然后在外面 print 出来 —— 复习"有 return 才接得住"。
#
# 5. 把演示数据换成你真实的一个数据文件（比如 nodes_csv），
#    看程序会不会因为格式不一样而漏数据。
#
# 改造完每个都要跑一遍，确认输出合理再往下。


print()
print("===== 第 23 天小结 =====")
print("1. 完整程序 = 准备数据 → 读清洗 → 统计 → 写报告 → 检查")
print("2. 一个函数只干一件事，能换数据就是好结构")
print("3. 字典把名字和值绑在一起，不怕错位")
print("4. 空数据要先判断，再算平均（否则除零）")
print("5. read() 和 for line in f 在同一个 with 里只能二选一")