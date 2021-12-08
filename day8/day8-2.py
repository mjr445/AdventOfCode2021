TWO_SEGMENT_LOCATION = 0  # 1
THREE_SEGMENT_LOCATION = 1  # 7
FOUR_SEGMENT_LOCATION = 2  # 4
FIVE_SEGMENT_START = 3
SIX_SEGMENT_START = 6
SEVEN_SEGMENT_LOCATION = 9  # 8

mappings = {}

with open("day8.txt", "r") as file:
    final_sum = 0

    for line in file:
        inputs, outputs = line.split("|")

        inputs = sorted(inputs.strip().split(), key=len)
        inputs = [set(input) for input in inputs]
        outputs = outputs.split()

        tr_br = inputs[TWO_SEGMENT_LOCATION]
        mappings['1'] = inputs[TWO_SEGMENT_LOCATION]

        top = inputs[THREE_SEGMENT_LOCATION] - inputs[TWO_SEGMENT_LOCATION]
        mappings['7'] = inputs[THREE_SEGMENT_LOCATION]

        tl_m = inputs[FOUR_SEGMENT_LOCATION] - tr_br
        mappings['4'] = inputs[FOUR_SEGMENT_LOCATION]

        bl_b = inputs[SEVEN_SEGMENT_LOCATION] - tr_br - top - tl_m
        mappings['8'] = inputs[SEVEN_SEGMENT_LOCATION]

        fives = inputs[FIVE_SEGMENT_START:SIX_SEGMENT_START]
        sixes = inputs[SIX_SEGMENT_START:SEVEN_SEGMENT_LOCATION]

        for six_segment in sixes:
            if len((mappings['8'] - six_segment) | tr_br) == 2:
                mappings['6'] = six_segment
                tr = mappings['8'] - six_segment
                br = tr_br - tr
                
            elif len((mappings['8'] - six_segment) | bl_b) == 2:
                mappings['9'] = six_segment
                bl = mappings['8'] - six_segment
                b = bl_b - bl
            
            else:
                mappings['0'] = six_segment
        
        mappings['5'] = mappings['8'] - tr - bl
        for five_segment in fives:
            if len(mappings['5'] | five_segment) == 7:
                mappings['2'] = five_segment
            elif len(mappings['5'] | five_segment) != 5:
                mappings['3'] = five_segment
        
        final_value = ""
        for output in outputs:
            output = set(output.strip())
            for key, val in mappings.items():
                if val == output:
                    final_value = final_value + key
                    break
        final_sum = final_sum + int(final_value)
    print(final_sum)
