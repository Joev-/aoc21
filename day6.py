f = open('./inputs/day6.txt')
data = f.readlines()[0]

fish_states_that_it_is_a_fish = [int(x) for x in data.split(',')]

def fish_count(timeperiod):
    # 0, 1, 2, 3, 4, 5, 6, 7, 8
    states_that_are_not_a_fish = [0] * 9

    for x in fish_states_that_it_is_a_fish:
        states_that_are_not_a_fish[x] += 1

    for _ in range(timeperiod):
        out_with_old = states_that_are_not_a_fish.pop(0)
        states_that_are_not_a_fish[6] += out_with_old
        states_that_are_not_a_fish.append(out_with_old)
    return sum(states_that_are_not_a_fish)

print(fish_count(80))
print(fish_count(256))
