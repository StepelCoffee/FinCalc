import math
from Calculus import NumericalRoots as numroot

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


def stated_rate(effective_rate:float,compound_periods_per_year:int) -> float:
    return periodic_rate(effective_rate,compound_periods_per_year)*compound_periods_per_year


def stated_rate_continuous(effective_rate:float) -> float:
    return math.log(effective_rate+1, math.e)


def get_period_from_rates(stated_annual_rate:float, effective_annual_rate:float):
    r = numroot.RootFinder(1, 20, 0.01)
    args = (90, 5)
    #roots = r.find(f, *args)

if __name__ == '__main__':
    # for i in [1,2,4,6,12,365]:
    #     print(future_value(75000,0.07,6,i))
    #     print(effective_annual_rate(0.07,i))
    # print(future_value_continuous(75000,0.07,6))
    # print(effective_annual_rate_continuous(0.07))
    for i in [1, 2, 4, 6, 12, 365]:
        print(periodic_rate(0.08,i))
        print(stated_rate(0.08,i))
    print(stated_rate_continuous(0.08))
