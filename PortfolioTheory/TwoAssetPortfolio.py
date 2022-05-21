from typing import List
import math


def list_product(x:List[float],y:List[float])-> List[float]:
    return [a * b for a, b in zip(x, y)]


def list_squared(x:List[float]) -> List[float]:
    return list_product(x, x)


class TwoAssetPortfolio:
    def __init__(self,weights: List[float], risks: List[float], returns: List[float], correlation: float):
        self.weights = weights
        self.risks = risks
        self.returns = returns
        self.correlation = correlation

    def get_portfolio_return(self) -> float:
        return sum(list_product(self.weights,self.returns))

    def get_portfolio_risk(self) -> float:
        w_sqr = list_squared(self.weights)
        v_sqr = list_squared(self.risks)
        prod_sqr = sum(list_product(w_sqr, v_sqr))
        cor_term = 2*math.prod(self.weights)*math.prod(self.risks)*self.correlation
        portfolio_var = prod_sqr + cor_term
        return math.sqrt(portfolio_var)


def cov_to_corr(cov:float, risks:List[float]) -> float:
    return cov/math.prod(risks)

