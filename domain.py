import random

from texttable import Texttable


class Board:
    def __init__(self, matrix_size, number_of_apples):
        self.__board = []
        self.__direction = "up"
        self.__matrix_size = matrix_size
        self.__head_location = (0, 0)
        self.__snake_segments = []
        for index in range(0, matrix_size):
            self.__board.append([])
            for secundary_index in range(0, matrix_size):
                self.__board[index].append(" ")
        self.place_the_snake_in_center_of_the_board(matrix_size)
        self.place_the_apples_random_on_board(number_of_apples)

    @property
    def get_direction(self):
        return self.__direction

    @get_direction.setter
    def get_direction(self, value):
        self.__direction = value

    @property
    def get_values(self):
        return self.__board

    @property
    def get_size(self):
        return self.__matrix_size

    @property
    def get_head_location(self):
        return self.__head_location

    @get_head_location.setter
    def get_head_location(self, value):
        self.__head_location = value

    @property
    def get_last_snake_segment(self):
        snake_tail = self.__snake_segments[0]
        self.__snake_segments.pop(0)
        return snake_tail

    def add_snake_segment(self, location):
        self.__snake_segments.append(location)

    def place_a_segment_on_board(self, column, row, segment):
        self.__board[column][row] = segment

    def place_the_snake_in_center_of_the_board(self, matrix_size):
        middle = matrix_size/2
        middle = int(middle)
        self.__board[middle-1][middle] = "*"
        self.__head_location = (middle-1, middle)
        self.__board[middle][middle] = "+"
        self.__board[middle+1][middle] = "+"
        self.__snake_segments.append((middle+1, middle))
        self.__snake_segments.append((middle, middle))
        self.__snake_segments.append((middle-1, middle))

    def place_the_apples_random_on_board(self, number_of_apples):
        while number_of_apples > 0:
            random_row = random.randint(0, self.__matrix_size-1)
            random_column = random.randint(0, self.__matrix_size-1)
            if self.availabe_location_to_place_apple(random_row, random_column):
                self.__board[random_column][random_row] = "a"
                number_of_apples -= 1

    def availabe_location_to_place_apple(self, row, column):
        if self.__board[column][row] == "*":
            return False
        if self.__board[column][row] == "+":
            return False
        if self.__board[column][row] == "a":
            return False
        if row > 0:
            if self.__board[column][row-1] == "a":
                return False
        if row < self.__matrix_size - 1:
            if self.__board[column][row+1] == "a":
                return False

        if column > 0:
            if self.__board[column-1][row] == "a":
                return False

        if column < self.__matrix_size - 1:
            if self.__board[column+1][row] == "a":
                return False

        return True

    def print_board(self):
        printed_board = Texttable()
        for index in range(0, self.__matrix_size):
            printed_board.add_row(self.__board[index])
        return printed_board.draw()
