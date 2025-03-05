
class Services:
    def __init__(self, board):
        self.__board = board

    def move_a_single_block(self):
        snake_head_column = self.__board.get_head_location[0]
        snake_head_row = self.__board.get_head_location[1]
        new_head_column = snake_head_column
        new_head_row = snake_head_row
        if self.__board.get_direction == "up":
            new_head_column -= 1
        elif self.__board.get_direction == "down":
            new_head_column += 1
        elif self.__board.get_direction == "right":
            new_head_row += 1
        elif self.__board.get_direction == "left":
            new_head_row -= 1
        if self.valid_position_on_table(new_head_column, new_head_row):
            if self.isnt_snake_body(new_head_column, new_head_row):
                if self.is_apple_on_position(new_head_column, new_head_row):
                    # Add the new snake segment location to segments queue
                    self.__board.add_snake_segment((new_head_column, new_head_row))
                    self.__board.get_head_location = (new_head_column, new_head_row)
                    self.__board.place_a_segment_on_board(new_head_column, new_head_row, "*")
                    self.__board.place_a_segment_on_board(snake_head_column, snake_head_row, "+")
                    self.__board.place_the_apples_random_on_board(1)
                else:
                    # Get latest snake segment to remove it from board and queue
                    snake_tail = self.__board.get_last_snake_segment
                    snake_tail_column = snake_tail[0]
                    snake_tail_row = snake_tail[1]
                    self.__board.place_a_segment_on_board(snake_tail_column, snake_tail_row, " ")

                    # Add the new snake segment location to segments queue
                    self.__board.add_snake_segment((new_head_column, new_head_row))

                    # Create new head and make old one normal snake segment
                    self.__board.place_a_segment_on_board(snake_head_column, snake_head_row, "+")
                    self.__board.place_a_segment_on_board(new_head_column, new_head_row, "*")
                    self.__board.get_head_location = (new_head_column, new_head_row)
            else:
                raise GeneratorExit("\n  ~  Game over! You hit the snake body...  ~")
        else:
            raise GeneratorExit("\n  ~  Game over! You hit the edge...  ~")

    def move_multiple_blocks(self, number_of_blocks):
        for index in range(0, number_of_blocks):
            self.move_a_single_block()

    def move_up(self):
        if self.__board.get_direction == "down":
            raise ValueError("Error: 180 grades movement!")
        if self.__board.get_direction == "up":
            raise ValueError(" ")
        self.__board.get_direction = "up"
        self.move_a_single_block()

    def move_down(self):
        if self.__board.get_direction == "up":
            raise ValueError("Error: 180 grades movement!")
        if self.__board.get_direction == "down":
            raise ValueError(" ")
        self.__board.get_direction = "down"
        self.move_a_single_block()

    def move_right(self):
        if self.__board.get_direction == "left":
            raise ValueError("Error: 180 grades movement!")
        if self.__board.get_direction == "right":
            raise ValueError(" ")
        self.__board.get_direction = "right"
        self.move_a_single_block()

    def move_left(self):
        if self.__board.get_direction == "right":
            raise ValueError("Error: 180 grades movement!")
        if self.__board.get_direction == "left":
            raise ValueError(" ")
        self.__board.get_direction = "left"
        self.move_a_single_block()

    @staticmethod
    def check_move_input(inputed_string):
        inputed_string = inputed_string.split(" ")
        if len(inputed_string) == 1:
            if inputed_string[0] == "move":
                return 1
            else:
                raise ValueError("Error: Unknown command!")
        if len(inputed_string) == 2:
            if inputed_string[0] == "move":
                if inputed_string[1].isdigit():
                    return int(inputed_string[1])
            raise ValueError("Error: Command format error!")
        else:
            raise ValueError("Error: Unknown command!")

    def valid_position_on_table(self, column, row):
        if not row >= 0:
            return False
        if not row <= self.__board.get_size - 1:
            return False
        if not column >= 0:
            return False
        if not column <= self.__board.get_size - 1:
            return False
        return True

    def isnt_snake_body(self, column, row):
        if self.__board.get_values[column][row] == '+':
            return False
        return True

    def is_apple_on_position(self, column, row):
        if self.__board.get_values[column][row] == "a":
            return True
        return False

    def get_printed_board(self):
        return self.__board.print_board()
