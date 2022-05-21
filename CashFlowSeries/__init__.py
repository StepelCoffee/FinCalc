from typing import List


class Annuity:
    def __init__(self,amount: float, rate_per_period: float, periods: int, payment_delay: int = 0):
        self.__amount = amount
        self.__rate = rate_per_period
        self.__time_periods = periods
        self.__payment_delay = payment_delay

    def calc_final_value(self) -> float:
        return self.__amount*((1+self.__rate)**self.__time_periods-1)/self.__rate

    def calc_present_value(self) -> float:
        pv = self.__amount*(1-1/(1+self.__rate)**self.__time_periods)/self.__rate
        if self.__payment_delay > 0:
            pv = pv/((1+self.__rate) ** self.__payment_delay)
        return pv


class UnequalCashFlow:
    def __init__(self, amount: List[float], rate_per_period: float):
        self.__amount = amount
        self.__rate = rate_per_period
        self.__time_periods = len(amount)

    def calc_final_value(self) -> float:
        total = 0
        for i in range(1,self.__time_periods+1):
            total += self.__amount[i-1]*((1+self.__rate)**(self.__time_periods-i))
        return total

    def calc_present_value(self) -> float:
        total = 0
        for i in range(1,self.__time_periods+1):
            total += self.__amount[i-1]/((1+self.__rate)**i)
        return total


class LumpSum:
    def __init__(self, future_value: float, rate_per_period: float, periods: int):
        self.__future_value = future_value
        self.__rate = rate_per_period
        self.__time_periods = periods

    def calc_pv(self) -> float:
        return self.__future_value / (1+self.__rate)**self.__time_periods



