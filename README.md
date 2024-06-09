# Four in a Row

## Project Description:
Four in a Row is a classic two-player game where the objective is to be the first to connect four of one's own discs of the same color in a row, column, or diagonal.

This project implements the game using an Object-Oriented Programming (OOP) approach in Python. The server-side logic is structured around several classes, each responsible for different aspects of the game:

- **Board**: Manages the game board state and provides methods for checking win conditions.
- **Game**: Orchestrates the game flow, including player turns and win detection.
- **Player**: Represents a player in the game, with attributes such as name and color.
- **Server_socket**: Handles communication between the server and clients using sockets.
- **main**: Acts as the entry point for starting the server and running the game loop.

## Table of Contents:
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation:

### Python Server:
- Clone the repository:
 git clone https://github.com/yoav-yamin/Four_in_a_Row.git

- Navigate to the Server directory:
  cd Four_in_a_Row/Server
- Run the server:
  python main.py

### C# Client:
- Navigate to the Client/bin/Debug directory.
- Run the Client.exe file.

## Usage:
Once both the Python server and the C# client are running, the game can be played on the graphical user interface provided by the C# client. Players take turns dropping colored discs onto the grid in an attempt to connect four of their own discs vertically, horizontally, or diagonally. The Python server handles the game logic and communication between players.

## License:
This project is licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/) license.


