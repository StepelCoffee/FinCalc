import TwoAssetPortfolio as tp

if __name__ == '__main__':
    weights = [0.8,0.2]
    risks = [0.1621,0.3311]
    returns = [0.0993,0.1820]
    cov = 0.005

    pf = tp.TwoAssetPortfolio(weights, risks, returns, tp.cov_to_corr(cov,risks))

    print(pf.get_portfolio_return())
    print(pf.get_portfolio_risk())