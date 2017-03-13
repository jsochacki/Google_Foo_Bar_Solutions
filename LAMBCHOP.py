def answer(src, dest):
    try:
        assert ( isinstance(src, int) and isinstance(dest, int) )
    except AssertionError as e:
        raise SystemExit('You need to enter and integer'
                         'for this function to work')
    else:
        try:
            assert ( ( 0 <= src <= 63 ) and ( 0 <= dest <= 63) )
        except AssertionError as e:
            raise SystemExit('This function only accepts integers'
                             'between and including 0 and 63')

    possible_moves = [[1, 2], [-1, 2], [1, -2], [-1, -2],
                      [2, 1], [-2, 1], [2, -1], [-2, -1]]

    square_dimension = 8
    locations = \
        [[row_value, column_value]
                    for column_value in range(0, square_dimension)
                    for row_value in range(0, square_dimension)]

    possible_locations = [locations[src]]
    goal_position = locations[dest]
    moves = 0

    if possible_locations == goal_position:
        return moves

    while goal_position not in possible_locations:
        current_possible_locations = []
        for PossibleLocation in possible_locations:
            for Move in possible_moves:
                Column = PossibleLocation[0] + Move[0]
                Row = PossibleLocation[1] + Move[1]
                if (0 <= Column <= 7) and \
                   (0 <= Row <= 7):
                   current_possible_locations.append([Column, Row])
        possible_locations = current_possible_locations
        moves = moves + 1
    return moves