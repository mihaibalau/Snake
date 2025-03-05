# Snake
 A Python-based command-line Snake game, being my subject for a first university semester exam. Simple yet challenging.

## Key Features
* Texttable library used
* Layered architecture
* Inheritance
* Polymorphism
* Gameplay interaction
* Apple placement system
* Game over conditions

## Code Structure
* domain.py: Defines the Board class, encapsulating the game state
* services.py: Contains the Services class, managing game logic
* user_interface.py: Implements the UserInterface class for handling user input
* start.py: Entry point of the game, initializing objects and starting the game loop

## How To Play

Start the game by running the `start.py` file. A formatted table will appear, where:

- `*` represents the head of the snake,
- `+` represents the body of the snake,
- `a` marks the apples.

You can control the snake's direction using the following commands: `up`, `down`, `left`, or `right`. Alternatively, you can use the `move` command to advance the snake in its current direction.
