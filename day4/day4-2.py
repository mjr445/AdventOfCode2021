def number_was_called(number, drawn_numbers):
    if number in drawn_numbers:
        return True
    return False

class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.num_rows = len(board)
        self.num_cols = len(board[0])
    
    def __str__(self):
        return f"{self.board}"

    def win(self, drawn_numbers):
        for row in range(self.num_rows):
            bingo = True
            for col in range(self.num_cols):
                if number_was_called(self.board[row][col], drawn_numbers):
                    continue
                else:
                    bingo = False
                    break
            if bingo:
                return True
        
        for col in range(self.num_rows):
            bingo = True
            for row in range(self.num_cols):
                if number_was_called(self.board[row][col], drawn_numbers):
                    continue
                else:
                    bingo = False
                    break
            if bingo:
                return True
        
        return False
    
    def sum_unmarked_board_numbers(self, drawn_numbers):
        total_sum = 0

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                number = self.board[row][col]
                if not number_was_called(number, drawn_numbers):
                    total_sum = total_sum + int(number)
        return total_sum


with open("day4.txt", "r") as file:
    all_drawn_numbers = tuple(file.readline().strip().split(","))
    bingo_boards = []
    for line in file:
        if line == '\n':
            board = (tuple(file.readline().strip().split()), 
            tuple(file.readline().strip().split()), 
            tuple(file.readline().strip().split()), 
            tuple(file.readline().strip().split()),
            tuple(file.readline().strip().split()))

            bingo_boards.append(BingoBoard(board))

    drawn_numbers = set(all_drawn_numbers[:-1])
    previous_number = all_drawn_numbers[-1]
    all_drawn_numbers_reversed = tuple(reversed(all_drawn_numbers[:-1]))

    last_board_found = False

    for number in all_drawn_numbers_reversed:
        for board in bingo_boards:
            if not board.win(drawn_numbers):
                last_board = board
                last_number = previous_number
                last_board_found = True
                break
        
        if last_board_found:
            break

        drawn_numbers.remove(number)
        previous_number = number
    
    drawn_numbers.add(last_number)
    print(last_board.sum_unmarked_board_numbers(drawn_numbers) * int(last_number))