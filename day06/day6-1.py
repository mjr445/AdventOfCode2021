AFTER_N_DAYS = 80

eight_day_timer = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0
}

six_day_timer = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}

def move_six_day_timers(six_day_timer):
    six_day_timer[0], six_day_timer[1], six_day_timer[2], six_day_timer[3], six_day_timer[4], six_day_timer[5], six_day_timer[6] = six_day_timer[1], six_day_timer[2], six_day_timer[3], six_day_timer[4], six_day_timer[5], six_day_timer[6], six_day_timer[0]
    return six_day_timer

def move_eight_day_timers(eight_day_timer):
    eight_day_timer[0], eight_day_timer[1], eight_day_timer[2], eight_day_timer[3], eight_day_timer[4], eight_day_timer[5], eight_day_timer[6], eight_day_timer[7] = eight_day_timer[1], eight_day_timer[2], eight_day_timer[3], eight_day_timer[4], eight_day_timer[5], eight_day_timer[6], eight_day_timer[7], eight_day_timer[8]
    return eight_day_timer

with open("day6.txt") as file:
    numbers = file.readline().strip().split(",")
    numbers = [int(number) for number in numbers]
    intermediate_eights = 0

    for number in numbers:
        six_day_timer[number] = six_day_timer[number] + 1

    for i in range(AFTER_N_DAYS):
        six_day_timer = move_six_day_timers(six_day_timer)
        eight_day_timer = move_eight_day_timers(eight_day_timer)

        six_day_timer[6] = six_day_timer[6] + intermediate_eights
        eight_day_timer[8] = six_day_timer[6]

        intermediate_eights = eight_day_timer[0]
        eight_day_timer[0] = 0
    
    total_flies = sum(six_day_timer.values()) + sum(eight_day_timer.values()) + intermediate_eights
    print(total_flies)
