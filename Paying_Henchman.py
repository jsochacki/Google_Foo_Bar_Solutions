def answer(total_lambs):
    try:
        assert isinstance(total_lambs, int)
    except AssertionError as e:
        raise SystemExit('You need to enter and integer'
                         'for this function to work')
    else:
        try:
            assert ( 10 <= total_lambs <= 1000000000 )
        except AssertionError as e:
            raise SystemExit('This function only accepts integers'
                             'between and including 10 and 10e9')

    LAMS = total_lambs
    level = 0
    while int(total_lambs) >= 0:
        total_lambs = int(total_lambs - (0b1 << level))
        if int(total_lambs) >= 0:
            level = level + 1

    least_henchmen = level

    total_lambs = LAMS
    level = 0
    hench_pay = []
    while int(total_lambs) >= 0:
        if level >= 2:
            hench_pay.extend([hench_pay[level - 2] + hench_pay[level - 1]])
        else:
            hench_pay.extend([1])
        total_lambs = int(total_lambs - hench_pay[level])
        if int(total_lambs) >= 0:
            level = level + 1

    most_henchmen = level

    return (most_henchmen - least_henchmen)
   # %%
