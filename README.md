# Kaun Banega Crorepati (KBC) Quiz Game

This project is a command-line (CLI) implementation of the famous Indian quiz show, **Kaun Banega Crorepati** (KBC), created using Python. The game features multiple-choice questions, and the player advances through levels to win virtual money based on correct answers.

## Features
- Multiple-choice questions with four options.
- Levels with increasing difficulty.
- Virtual money prize based on levels.
- Lifelines (e.g., 50:50, Phone a Friend) for players to get assistance.
- Progress tracking, including prize money at each level.

## Technologies Used
- Python 3.x
- `random` module for randomizing questions and lifelines.
- `time` module for adding delays and enhancing gameplay experience.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/M-Nadeem-B/KBC-repo/KBC-Quiz-Game.git
    cd KBC-Quiz-Game
    ```

2. Install any required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

   > *Note: There are no external dependencies for the CLI version of this game.*

3. Run the game:

    ```bash
    python kbc_game.py
    ```

## How to Play
1. Start the game by running the script.
2. Read the question and choose the correct answer by typing the corresponding option (A, B, C, or D).
3. Use the available lifelines when you’re unsure about an answer.
4. Keep answering correctly to advance through the levels and win virtual money!

## Game Rules
- The game consists of 15 questions.
- Players must answer each question correctly to move to the next level.
- If a player answers a question incorrectly, they can either choose to end the game or continue using a lifeline.
- Lifelines available are: 50:50 (removes two incorrect options) and Phone a Friend (gives a hint).
- The prize money increases with each level.

## Future Enhancements
- **GUI Version**: A graphical user interface (GUI) version will be implemented after completing the CLI version.
- **Leaderboards**: Adding a leaderboard to track high scores.
- **More lifelines**: Adding additional lifelines such as "Ask the Audience" or "Switch the Question."

## Contributing
If you would like to contribute to the development of this project, feel free to fork the repository, submit issues, or create pull requests.

## License
This project is licensed under the MIT License. For details, see the [LICENSE](LICENSE) file.

## Author
[Nadeem]([https://github.com/M-Nadeem-B])

## Acknowledgements
- The concept of the game is inspired by the Indian TV show **Kaun Banega Crorepati**.
