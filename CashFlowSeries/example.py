import CashFlowSeries as cfs

if __name__ == '__main__':
    # calculate annuity
    amount = 100000
    annual_rate = 0.05
    years = 10
    ann = cfs.Annuity(amount,annual_rate,years)
    print(ann.calc_final_value())
    print(ann.calc_present_value())
    # calculate delayed annuity
    amount = 1
    annual_rate = 0.05
    years = 30
    delay = 9
    ann = cfs.Annuity(amount, annual_rate, years, delay)
    print(ann.calc_present_value())
    # calculate a series of unequal cash flows with a percentage of 2
    cashflows = [0,4000,0,8000,0,7000,0,10000]
    rate_per_period = 0.02
    ucf = cfs.UnequalCashFlow(cashflows,rate_per_period)
    print(ucf.calc_final_value())
    # calculate pv of a series of cashflows in two ways
    payment = 20000
    cashflows = [0,0,0, payment,payment,payment,payment]
    rate_per_period = 0.08
    ucf = cfs.UnequalCashFlow(cashflows,rate_per_period)
    ann = cfs.Annuity(payment, rate_per_period, 4,3)
    print(ucf.calc_present_value())
    print(ann.calc_present_value())
    # calculate a series of cashflows
    cashflows = [20000,20000,20000,30000]
    rate_per_period = 0.08
    ucf = cfs.UnequalCashFlow(cashflows,rate_per_period)
    print(ucf.calc_present_value())
    # calculate the present value of a lumpsum that has a 5% rate that is
    # applied monthly
    future_value = 5000
    annual_rate = 0.05
    monthly_rate = 0.05/12
    years = 3
    months = years*12
    ls = cfs.LumpSum(future_value,monthly_rate,months)
    print(ls.calc_pv())