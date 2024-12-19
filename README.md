# Quantum Tic-Tac-Toe

## Overview
Quantum Tic-Tac-Toe combines quantum principles with a classical user interface to create a unique and engaging game experience. This project leverages **Cirq** for quantum mechanics and **Pygame** for the UI, showcasing quantum concepts such as **superposition**, **entanglement**, and **measurement**.

---

## Prerequisites

1. **Python Environment**: Ensure Python 3.8 or higher is installed.
2. **Install Dependencies**: Use the provided `requirements.txt` file to install all necessary libraries.

    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Game

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/PeroxideParadox/Quantum-Simulation-Game.git
    cd Quantum-Simulation-Game
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Game**:

    ```bash
    python quantum_tic_tac_toe.py
    ```

4. **Play the Game**:
    - The game starts with an empty 3x3 grid.
    - Each cell initially exists in a quantum superposition.
    - Players alternate turns by clicking on empty cells.
    - Once all cells are filled, the quantum state collapses into classical outcomes, determining the winner or a draw.


## Steps for Creating and Using the Executable

### 1. Create an Executable

To distribute the game as a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile quantum_tic_tac_toe.py
```

### 2. Locate the Executable

- After running the command, `PyInstaller` generates a `dist` and `build` directory in your current working directory.
- Inside this `dist` directory, you will find the standalone executable file named `quantum_tic_tac_toe` (on macOS/Linux) or `quantum_tic_tac_toe.exe` (on Windows).

### 3. Run the Executable

- **On Windows**: 
  - Open a terminal or navigate to the `dist` directory in File Explorer.
  - Double-click the `quantum_tic_tac_toe.exe` file to launch the game.
  - Alternatively, you can open a terminal in the `dist` directory and run:
    ```bash
    quantum_tic_tac_toe.exe
    ```

- **On macOS/Linux**:
  - Open a terminal and navigate to the `dist` directory.
  - Run the executable with:
    ```bash
    ./quantum_tic_tac_toe
    ```

  If you encounter a permission error on macOS/Linux, make the file executable:
  ```bash
  chmod +x quantum_tic_tac_toe
  ./quantum_tic_tac_toe
  ```

### 4. Play the Game

- The game’s interface will appear as a GUI window.


## Features

1. **Quantum Superposition**:
   - All cells start in a quantum superposition of states.

2. **Measurement**:
   - Once the grid is full, unoccupied cells collapse into classical states.

3. **Winning Conditions**:
   - The game checks rows, columns, and diagonals for a winner.
   - If all cells are occupied without a winner, it results in a draw.


## Deployment

To distribute the game:

1. **Create an Executable**:

    ```bash
    pip install pyinstaller
    pyinstaller --onefile quantum_tic_tac_toe.py
    ```

2. **Share the Executable**:
   - The generated executable file can be shared with players who don't have Python installed.
