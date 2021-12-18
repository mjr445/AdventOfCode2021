def handle_value_based_on_packet_type(new_value, final_value, packet_type_id):
    if final_value is None:
        return new_value

    if packet_type_id == 0:
        return new_value + final_value

    elif packet_type_id == 1:
        return new_value * final_value

    elif packet_type_id == 2:
        return min(new_value, final_value)

    elif packet_type_id == 3:
        return max(new_value, final_value)

    elif packet_type_id == 5:
        return int(final_value > new_value)
        
    elif packet_type_id == 6:
        return int(final_value < new_value)
    else:  # ID is 7
        return int(new_value == final_value)

def read_sub_packet(packet, starting_index, max_packet_length=None):

    if max_packet_length:
        max_index = max_packet_length + starting_index
    
    packet_version_index_end, packet_type_id_index_end = starting_index+3, starting_index+6
    packet_version = int(packet[starting_index:packet_version_index_end], 2)
    packet_type_id = int(packet[packet_version_index_end:packet_type_id_index_end], 2)

    is_literal_value = packet_type_id == 4  # If not, it's an operator

    if is_literal_value:

        not_encountered_final_group = True

        starting_index = packet_type_id_index_end
        final_value = ""
        final_sub_packet_length = 0

        while not_encountered_final_group:
            not_encountered_final_group = packet[starting_index] == "1"

            starting_index = starting_index + 1
            ending_index = starting_index + 4

            if max_packet_length and ending_index > max_index:
                ending_index = max_index
                not_encountered_final_group = False
            
            final_value = final_value + packet[starting_index:ending_index]
            final_sub_packet_length = final_sub_packet_length + 1 + ending_index - starting_index

            starting_index = ending_index
        
        final_value = int(final_value, 2)
    
    else:  # It's an operator
        final_value = None
        current_length_of_sub_packets = 0

        length_type_id = packet[packet_type_id_index_end]
        if length_type_id == "0":
            length_of_sub_packets_index_start = packet_type_id_index_end + 1 
            new_sub_packet_index_start = length_of_sub_packets_index_start + 15

            max_length_of_sub_packets = int(packet[length_of_sub_packets_index_start:new_sub_packet_index_start], 2)  # Next 15 bits
            while current_length_of_sub_packets != max_length_of_sub_packets:
                sub_packet_value, sub_packet_length = read_sub_packet(packet, new_sub_packet_index_start, max_length_of_sub_packets - current_length_of_sub_packets)

                final_value = handle_value_based_on_packet_type(sub_packet_value, final_value, packet_type_id)
                current_length_of_sub_packets = current_length_of_sub_packets + sub_packet_length
                new_sub_packet_index_start = new_sub_packet_index_start + sub_packet_length
            
            final_sub_packet_length = current_length_of_sub_packets + 15
            
        else:
            number_of_sub_packets_index_start = packet_type_id_index_end + 1 
            new_sub_packet_index_start = number_of_sub_packets_index_start + 11
            
            number_of_sub_packets = int(packet[number_of_sub_packets_index_start:new_sub_packet_index_start], 2)  # Next 11 bits

            for _ in range(number_of_sub_packets):
                sub_packet_value, sub_packet_length = read_sub_packet(packet, new_sub_packet_index_start, max_packet_length)

                final_value = handle_value_based_on_packet_type(sub_packet_value, final_value, packet_type_id)
                current_length_of_sub_packets = current_length_of_sub_packets + sub_packet_length
                new_sub_packet_index_start = new_sub_packet_index_start + sub_packet_length
        
            final_sub_packet_length = current_length_of_sub_packets + 11
        
        final_sub_packet_length = final_sub_packet_length + 1
    
    final_sub_packet_length = final_sub_packet_length + 6
    return final_value, final_sub_packet_length


with open("day16.txt", "r") as file:
    final_sum = 0
    packet = file.readline().strip()
    
    number_of_leading_zeros = 0
    while packet[number_of_leading_zeros] == "0":
        number_of_leading_zeros = number_of_leading_zeros + 1
    
    packet = bin(int(packet, 16))[2:]  # Hex to Binary

    missing_leading_zeros = 4 - len(packet) % 4
    if missing_leading_zeros != 4:
        packet = ("0" * missing_leading_zeros) + packet
    if number_of_leading_zeros != 0:
        packet = "0000" * number_of_leading_zeros + packet
    
    final_sum, _ = read_sub_packet(packet, 0)
    print(final_sum)
