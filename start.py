from src.domain import Board
from src.services import Services
from src.user_interface import UserInterface


def run_program():
    matrix_size = 7
    number_of_apples = 10
    snake_board = Board(matrix_size, number_of_apples)
    board_services = Services(snake_board)
    user_interface = UserInterface(board_services)
    user_interface.run_program()


run_program()
