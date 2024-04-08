from sys import stdin

ascii_map = [
    [
        " _ ",
        "| |",
        "|_|"
    ],
    [
        "   ",
        "  |",
        "  |"
    ],
    [
        " _ ",
        " _|",
        "|_ "
    ],
    [
        " _ ",
        " _|",
        " _|"
    ],
    [
        "   ",
        "|_|",
        "  |"
    ],
    [
        " _ ",
        "|_ ",
        " _|"
    ],
    [
        " _ ",
        "|_ ",
        "|_|"
    ],
    [
        " _ ",
        "  |",
        "  |"
    ],
    [
        " _ ",
        "|_|",
        "|_|"
    ],
    [
        " _ ",
        "|_|",
        " _|"
    ]
]

def process_number(rows):
    tot = len(rows[0]) // 3
    actual_nums = []
    for i in range(0, tot + 1):
        seg1 = rows[0][i*3:i*3+3]
        seg2 = rows[1][i*3:i*3+3]
        seg3 = rows[2][i*3:i*3+3]
        if seg1 != "" and seg2 != "" and seg3 != "":
            actual_nums.append(ascii_map.index([seg1, seg2, seg3]))
    return actual_nums

def main():
    buf = []
    for _, line in enumerate(stdin):
        buf.append(line[:-1])
        if len(buf) == 3:
            nums = process_number(buf)
            stage_1 = [x*2 if (i + 1) % 2 == 0 else x for i, x in enumerate(reversed(nums))]
            stage_2 = sum([sum([int(c) for c in str(x)]) for x in stage_1])
            valid = stage_2 % 10 == 0
            print(f"{''.join([str(x) for x in nums])} {'VALID' if valid else 'INVALID'}")            
            buf = []
    
main()

