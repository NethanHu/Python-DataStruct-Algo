

def move_disk(disk_level: int, from_pole: int, to_pole: int):
    print(f"Moving disk[{disk_level}] from Pillar#{from_pole} to Pillar#{to_pole}")

def move_tower(level: int, from_pole: int, with_pole: int, to_pole: int):
    if level >= 1:
        # 对于当前盘子，把中间的2号柱子当成缓冲，把自己挪过去
        move_tower(level - 1, from_pole, to_pole, with_pole)
        # 把下面的的盘子移到终点3号柱子
        move_disk(level, from_pole, to_pole)
        # 回到自己这里。把自己从2号缓冲柱子移到终点3号柱子
        move_tower(level - 1, with_pole, from_pole, to_pole)

move_tower(3, 1, 2, 3)