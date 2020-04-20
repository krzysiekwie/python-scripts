def break_even():


    ret_price = float(input('retail price $: '))
    ret_margin = float(input('retail margin %: ')) * 0.01
    m_contrib_margin_pc = float(input('manufacturer contribution margin %: ')) * 0.01

    ad_budget = float(input('ad budget $: '))


    m_c_m_dollar = ret_price * (1 -ret_margin) * m_contrib_margin_pc
    print("Manufacturer Contrib Margin ${}".format(m_c_m_dollar))

    break_even_units = ad_budget/ m_c_m_dollar
    print("Break Even Units: {}".format(break_even_units))


break_even()
