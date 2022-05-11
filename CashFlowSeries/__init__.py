from typing import List


class Annuity:
    def __init__(self,amount: float, rate_per_period: float, periods: int):
        self.__amount = amount
        self.__rate = rate_per_period
        self.__time_periods = periods

    def calc_final_value(self) -> float:
        return self.__amount*((1+self.__rate)**self.__time_periods-1)/self.__rate

    def calc_present_value(self) -> float:
        return self.__amount*(1-1/(1+self.__rate)**self.__time_periods)/self.__rate


class UnequalCashFlow:
    def __init__(self,amount: List[float], rate_per_period: float, periods: int):
        self.__amount = amount
        self.__rate = rate_per_period
        self.__time_periods = periods

    def calc_final_value(self) -> float:
        total = 0
        for i in range(1,self.__time_periods+1):
            total += self.__amount[i-1]*((1+self.__rate)**(self.__time_periods-i))
        return total


class LumpSum:
    def __init__(self, future_value: float, rate_per_period: float, periods: int):
        self.__future_value = future_value
        self.__rate = rate_per_period
        self.__time_periods = periods

    def calc_pv(self) -> float:
        return self.__future_value / (1+self.__rate)**self.__time_periods



if __name__ == '__main__':
    ann = Annuity(1000,0.12,5)
    print(ann.calc_final_value())
    print(ann.calc_present_value())
    ucf = UnequalCashFlow([0,4000,0,8000,0,7000,0,10000],0.02,8)
    print(ucf.calc_final_value())
    ls = LumpSum(5000,0.05/12,3*12)
    print(ls.calc_pv())