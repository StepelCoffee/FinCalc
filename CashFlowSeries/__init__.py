from typing import List


class Annuity:
    def __init__(self,amount: float, rate_per_period: float, periods: int):
        self.__amount = amount
        self.__rate = rate_per_period
        self.__time_periods = periods

    def calc_final_value(self) -> float:
        return self.__amount*((1+self.__rate)**self.__time_periods-1)/self.__rate


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



if __name__ == '__main__':
    ann = Annuity(20000,0.09,30)
    print(ann.calc_final_value())
    ucf = UnequalCashFlow([1000,2000,4000,5000,6000],0.05,5)
    print(ucf.calc_final_value())
