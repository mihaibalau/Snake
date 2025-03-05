
class UserInterface:
    def __init__(self, available_services):
        self.__services = available_services

    def run_program(self):
        print("  ~  Welcome to snake game!  ~  \n")
        print(self.__services.get_printed_board())
        print(" ")
        try:
            while True:
                try:
                    new_command = input("Enter your new command: ")
                    option = -1
                    if "move" in new_command:
                        option = self.__services.check_move_input(new_command)
                        move_a_single_box = 1
                        if option == move_a_single_box:
                            self.__services.move_a_single_block()
                        else:
                            self.__services.move_multiple_blocks(option)
                    else:
                        if new_command == "up":
                            self.__services.move_up()
                        elif new_command == "down":
                            self.__services.move_down()
                        elif new_command == "right":
                            self.__services.move_right()
                        elif new_command == "left":
                            self.__services.move_left()
                        else:
                            raise ValueError("Error: Unknown command!")
                    print("\n")
                    print(self.__services.get_printed_board())
                except ValueError as printed_message:
                    print(printed_message)
        except GeneratorExit as printed_message:
            print(printed_message)
