
def get_two_sum_dataset():
    data = list()
    set_1 = dict(
        nums=[2, 7, 11, 15],
        target=9,
        result=[0, 1]
    )
    set_2 = dict(
        nums=[3, 2, 4],
        target=6,
        result=[1, 2]
    )
    set_3 = dict(
        nums=[3, 3],
        target=6,
        result=[0, 1]
    )
    data.append(set_1)
    data.append(set_2)
    data.append(set_3)

    return data
