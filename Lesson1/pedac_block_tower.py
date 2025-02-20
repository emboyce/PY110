def calculate_leftover_blocks(blocks):
    blocks_avail = blocks
    layer = 1
    while True:
        blocks_needed = layer**2
        if blocks_needed > blocks_avail:
            return blocks_avail
        else:
            layer += 1
            blocks_avail -= blocks_needed


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(13)) # True
