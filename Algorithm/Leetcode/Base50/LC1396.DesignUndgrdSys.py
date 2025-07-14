from collections import defaultdict
from typing import List

"""
地铁系统跟踪不同车站之间的乘客出行时间，并使用这一数据来计算从一站到另一站的平均时间。

实现 UndergroundSystem 类：
void checkIn(int id, string stationName, int t)
通行卡 ID 等于 id 的乘客，在时间 t ，从 stationName 站进入
乘客一次只能从一个站进入
void checkOut(int id, string stationName, int t)
通行卡 ID 等于 id 的乘客，在时间 t ，从 stationName 站离开
double getAverageTime(string startStation, string endStation)
返回从 startStation 站到 endStation 站的平均时间
平均时间会根据截至目前所有从 startStation 站 直接 到达 endStation 站的行程进行计算，也就是从 startStation 站进入并从 endStation 离开的行程
从 startStation 到 endStation 的行程时间与从 endStation 到 startStation 的行程时间可能不同
在调用 getAverageTime 之前，至少有一名乘客从 startStation 站到达 endStation 站
你可以假设对 checkIn 和 checkOut 方法的所有调用都是符合逻辑的。如果一名乘客在时间 t1 进站、时间 t2 出站，那么 t1 < t2 。所有时间都按时间顺序发生。
"""
class UndergroundSystem:

    def __init__(self):
        self.in_station: dict[int, tuple[str, int]] = defaultdict(tuple)
        self.records: dict[tuple[str, str], List[int]] = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_station[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_sn, start_t = self.in_station[id]
        self.records[(start_sn, stationName)].append(t - start_t)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_t: List[int] = self.records[(startStation, endStation)]
        return sum(travel_t) / len(travel_t)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)