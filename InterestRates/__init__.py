import math
from typing import List

from Calculus import NumericalRoots as numRoot

def future_value(investment: float,interest_rate: float, years: int, compound_periods_per_year: int) -> float:
    return investment*(1+interest_rate/compound_periods_per_year)**(years*compound_periods_per_year)


def future_value_continuous(investment: float,interest_rate: float, years: int) -> float:
    return investment*math.exp(interest_rate*years)


def effective_annual_rate(interest_rate:float,compound_periods_per_year:int) -> float:
    return (1+ interest_rate/compound_periods_per_year)**compound_periods_per_year-1


def effective_annual_rate_continuous(interest_rate:float) -> float:
    return math.exp(interest_rate)-1


def periodic_rate(effective_rate:float,compound_periods_per_year:int) -> float:
    return (effective_rate+1)**(1/compound_periods_per_year)-1


def stated_annual_rate(effective_rate:float,compound_periods_per_year:int) -> float:
    return periodic_rate(effective_rate,compound_periods_per_year)*compound_periods_per_year


def stated_rate_continuous(effective_rate:float) -> float:
    return math.log(effective_rate+1, math.e)


def rate_fun_zero(m : float, effective_rate: float, stated_rate: float) -> float:
    return (1 + stated_rate / m)**m - 1 - effective_rate


def closest_compounding_frequency(m: List[int],effective_rate: float, stated_rate: float) -> int:
    closest = 0
    best_value = abs(rate_fun_zero(m[0],effective_rate,stated_rate))
    for i in range(1, len(m)):
        cur_val = abs(rate_fun_zero(m[i],effective_rate,stated_rate))
        if cur_val < best_value:
            closest = i
            best_value = cur_val
    return m[closest]


def get_period_from_rates(stated_rate:float, effective_rate:float):
    r = numRoot.RootFinder(1, 365, 1)
    args = (effective_rate, stated_rate)
    roots = r.find(rate_fun_zero, *args)
    return roots

if __name__ == '__main__':
    # for i in [1,2,4,6,12,365]:
    #     print(future_value(75000,0.07,6,i))
    #     print(effective_annual_rate(0.07,i))
    # print(future_value_continuous(75000,0.07,6))
    # print(effective_annual_rate_continuous(0.07))
    #for i in [1, 2, 4, 6, 12, 365]:
    #    print(periodic_rate(0.08,i))
    #   print(stated_annual_rate(0.08,i))
    #print(stated_rate_continuous(0.08))
    #print(get_period_from_rates(0.04,0.0408))
    #investment = 1000000
    #rate = 0.03
    #years = 4
    #continously_compounded = future_value_continuous(investment,rate,years)
    #daily_compounded = future_value(investment,rate,years,365)
    #print(continously_compounded-daily_compounded)
    #ret = closest_compounding_frequency([4,12,52],0.1047,0.1)
    #ret = future_value_continuous(2000,0.06,4)
    #ret = effective_annual_rate(0.2,12)
    ret = stated_annual_rate(0.12,4)
    print(ret)