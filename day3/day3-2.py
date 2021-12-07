NUM_BITS = 12

def toggle_nth_bit(x, n):
    """
    First bit is n=0, second bit is n=1, etc.
    :param x:
    :param n:
    """
    return x ^ (1 << n)

def get_nth_bit(x, n):
    """
    First bit is n=0, second bit is n=1, etc.
    """
    return (x >> n) & 1

with open("day3.txt", "r") as file:

    bit_sum = 0
    total_numbers = 0
    numbers = set()

    for line in file:
        line = line[:-1]
        numbers.add(int(line, 2))
        bit = line[0]
        bit_sum = bit_sum + int(bit)
        total_numbers = total_numbers + 1
    
    numbers = sorted(numbers)

    oxygen_rate = co2_rate = 0
    oxygen_min = co2_min = 0
    oxygen_max = co2_max = 2**(NUM_BITS) - 1
    oxygen_start_index = co2_start_index = 0
    oxygen_stop_index = co2_stop_index = total_numbers - 1
    looking_for_oxygen_rate = looking_for_co2_rate = True

    oxygen_bit_sum = co2_bit_sum = bit_sum

    bit_index = 0
    while looking_for_oxygen_rate or looking_for_co2_rate:

        oxygen_total_numbers = len(numbers[oxygen_start_index:oxygen_stop_index+1])
        co2_total_numbers = len(numbers[co2_start_index:co2_stop_index+1])

        if oxygen_bit_sum >= oxygen_total_numbers/2:
            oxygen_min = toggle_nth_bit(oxygen_min, NUM_BITS - (bit_index + 1))
            while numbers[oxygen_start_index] < oxygen_min:
                oxygen_start_index = oxygen_start_index + 1
        else:
            oxygen_max = toggle_nth_bit(oxygen_max, NUM_BITS - (bit_index + 1))
            while numbers[oxygen_stop_index] > oxygen_max:
                oxygen_stop_index = oxygen_stop_index - 1
        
        if co2_bit_sum >= co2_total_numbers/2:
            co2_max = toggle_nth_bit(co2_max, NUM_BITS - (bit_index + 1))
            while numbers[co2_stop_index] > co2_max:
                co2_stop_index = co2_stop_index - 1
        else:
            co2_min = toggle_nth_bit(co2_min, NUM_BITS - (bit_index + 1))
            while numbers[co2_start_index] < co2_min:
                co2_start_index = co2_start_index + 1

        if oxygen_stop_index == oxygen_start_index and looking_for_oxygen_rate:
            oxygen_rate = numbers[oxygen_stop_index]
            looking_for_oxygen_rate = False
        
        if co2_stop_index == co2_start_index and looking_for_co2_rate:
            co2_rate = numbers[co2_stop_index]
            looking_for_co2_rate = False
        
        bit_index = bit_index + 1
        if looking_for_oxygen_rate:
            oxygen_bit_sum = sum(get_nth_bit(number, NUM_BITS - (bit_index + 1)) for number in numbers[oxygen_start_index:oxygen_stop_index+1])

        if looking_for_co2_rate:
            co2_bit_sum = sum(get_nth_bit(number, NUM_BITS - (bit_index + 1)) for number in numbers[co2_start_index:co2_stop_index+1])
            
    print(oxygen_rate * co2_rate)
