def total_net_profit():
    margin = float(input('margin: '))
    ret_cost = float(input('ret cost: '))
    ret_rate = float(input('ret_rate: '))
    customers = int(input("customers: "))
    months = int(input("how many months? "))
    total_tnp = 0
    i = 1
    for i in range(1, months+1):
        print("Month: {}".format(i) )
        print("Customers: {}".format(customers))

        short_marg = margin - ret_cost
        print("short-term margin {}".format(short_marg))

        tnp_current = short_marg * customers
        print("current tnp {}".format(tnp_current))

        customers = customers * ret_rate
        total_tnp = total_tnp + tnp_current
        print("Accrued tnp {}".format(total_tnp))

total_net_profit()
