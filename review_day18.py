# -*- coding: utf-8 -*-
"""
复习总结 · 第 18 天（2026-11-01）

今天时间少（被学校比赛 PPT 卡住），只学了一样：or / and 与短路

  1. 真值表：or 有一个真就真；and 两个都真才真
  2. 短路：or 碰上第一个 True 就收工，右边连算都不算
  3. continue：这一圈到此为止，跳下一行数据
  4. 合并两道岗的前提：parts 必须先算出来
  5. 顺序的实战价值：把"检查长度"放左边，保护右边的 parts[1]

运行方式：直接跑，没有外部文件依赖。
"""

# ============================================================
# 1. 短路：怎么"看见"它真的没算右边
# ============================================================
print("===== 1. 短路演示 =====")


def probe(name, result):
    """一个会出声的检查：每次被调用都会打印一行。"""
    print(f"   >>> 计算了 {name}")
    return result


print("or 的情况（左边是 True）：")
if probe("A", True) or probe("B", True):
    print("   条件成立")

print("or 的情况（左边是 False）：")
if probe("A", False) or probe("B", True):
    print("   条件成立")

print("and 的情况（左边是 False）：")
if probe("A", False) and probe("B", True):
    print("   条件成立")

# 观察：某些 probe 完全没有打印出来 —— 那就是"根本没被计算"
#
#   or  ：A 真 → 不看 B
#   and ：A 假 → 不看 B


# ============================================================
# 2. 真值表
# ============================================================
print("===== 2. 真值表 =====")

print(True or True)      # True
print(True or False)     # True
print(False or True)     # True   ← 有一个真就真
print(False or False)    # False

print(True and True)     # True   ← 两个都真才真
print(True and False)    # False
print(False and True)    # False
print(False and False)   # False


# ============================================================
# 3. continue：这一圈到此为止
# ============================================================
print("===== 3. continue =====")

for v in [220, 1500, 12]:
    if v < 1000:
        print(f"  {v} 太小，跳过")
        continue                 # ← 下面的 print 不再执行
    print(f"  {v} 是高压，收下")


# ============================================================
# 4. 合并两道岗（注意 split 必须先做）
# ============================================================
print("===== 4. 合并两道岗 =====")

lines = ["节点A,220", "", "220", "节点B,12.5"]

for line in lines:
    line = line.strip()
    parts = line.split(",")                  # 先切，否则 len(parts) 会报错
    if line == "" or len(parts) != 2:        # 两个条件，一个 if 解决
        print(f"  丢弃: {line!r}")
        continue
    print(f"  收下: {parts[0]} = {parts[1]}")

# 顺带发现："".split(",") 得到 ['']，长度 1
# 所以空行本来就会被"段数岗"抓住，line == "" 只是写得更直白。


# ============================================================
# 5. 顺序 = 保险（防越界）
# ============================================================
print("===== 5. 顺序就是保险 =====")

for line in ["节点A,220", "220"]:
    parts = line.split(",")
    # 把"检查长度"放左边：只有一段时，右边 parts[1] 完全不会被访问
    if len(parts) != 2 or not parts[1].isdigit():
        print(f"  丢弃: {line!r}")
        continue
    print(f"  收下: {parts[0]} = {parts[1]}")

# 如果把顺序反过来写 parts[1].isdigit() or len(parts) != 2
# 那么 "220" 这一行会先在 parts[1] 处越界报错。
# 短路让"写在左边的"先算 —— 把长度检查放左边，就是给右边上保险。


print()
print("===== 第 18 天小结 =====")
print("1. or：有一个真就真；and：两个都真才真")
print("2. 短路：or 碰上 True、and 碰上 False，右边连算都不算")
print("3. continue：这一圈剩下的代码全跳过，直接下一行")
print("4. 合并两道岗前，parts 必须先算出来")
print("5. 条件顺序有讲究：把长度检查放左边，保护 parts[1] 不越界")