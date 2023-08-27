# U.S. States Game

The U.S. States Game is an interactive learning game that challenges players to guess the names of all 50 U.S. states on a map of the United States. The game is implemented using the Turtle graphics library in Python and utilizes a CSV file containing the names and coordinates of the states.

## How to Play

1. A map of the United States is displayed with all states' names hidden.
2. The player is prompted to input the name of a U.S. state.
3. If the guessed state name is correct, its name is revealed on the map.
4. The player can continue guessing state names until all 50 states are guessed or the player chooses to quit.
5. If the player guesses all 50 states, they have the option to replay or quit.

## Features

- The game displays a map of the United States and prompts the player to guess state names.
- The game keeps track of the player's progress, displaying the score as the number of correctly guessed states out of 50.
- Once a state name is guessed correctly, it is displayed on the map's corresponding location.
- If the player completes all 50 states, they have the option to replay the game or quit.

## Files

- **main.py:** The main script that initializes the game environment, manages gameplay, and user interaction.
- **50_states.csv:** Contains the data for all 50 U.S. states, including their names and coordinates.
- **blank_states_img.gif:** Image of the blank U.S. map for display in the game.

## Dependencies

- Turtle Graphics Library: The game uses the Turtle graphics library to create the graphics and animations.
- Pandas Library: The game uses the Pandas library to read the state data from the CSV file.
