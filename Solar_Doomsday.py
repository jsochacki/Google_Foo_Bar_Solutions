import math

def answer(area):
    try:
        assert isinstance(area, int)
    except AssertionError as e:
        raise SystemExit('You need to enter and integer'
                         'for this function to work')
    else:
        try:
            assert 1 <= area <= 1000000
        except AssertionError as e:
            raise SystemExit('This function only accepts integers'
                             'between and including 1 and 1,000,000')
    output_list = []
    material_left = area
    while material_left > 0:
        integer_root = int(math.sqrt(material_left))
        current_sheet_area = integer_root ** 2
        if integer_root > 1:
            output_list.extend([current_sheet_area])
            material_left = material_left - current_sheet_area
        else:
            output_list.extend([current_sheet_area] * int(material_left))
            material_left = 0
    return output_list
# %%