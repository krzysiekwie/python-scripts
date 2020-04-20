def customer_lifetime_value():

    margin = float(input('margin: '))
    ret_cost = float(input('ret cost: '))
    ret_rate = float(input('ret rate: '))
    disc_rate = float(input('disc rate: '))
    before_after = input("pay before [b] or after? [any key] ")

    short_marg = margin - ret_cost
    print("short-term margin {}".format(short_marg))

    if before_after == "b":
        long_term_m = (1+disc_rate)/(1+disc_rate-ret_rate)
    else:
        long_term_m = ret_rate/(1+disc_rate-ret_rate)
    print("long-term multiplier {}".format(long_term_m))

    clv = short_marg * long_term_m
    print("clv {}".format(clv))

customer_lifetime_value()
