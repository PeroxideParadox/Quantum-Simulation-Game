import pygame
import cirq
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quantum Tic-Tac-Toe")

# Fonts
FONT = pygame.font.SysFont("Arial", 50)

# Quantum Mechanics
def create_quantum_circuit():
    qubits = cirq.LineQubit.range(9)  # 9 cells for Tic-Tac-Toe
    circuit = cirq.Circuit()

    # Apply superposition to all cells initially
    for q in qubits:
        circuit.append(cirq.H(q))  # Hadamard gate for superposition

    return circuit, qubits

def measure_qubits(circuit, qubits):
    circuit.append(cirq.measure(*qubits, key="result"))
    simulator = cirq.Simulator()
    result = simulator.run(circuit)
    measurements = result.measurements["result"][0]
    return measurements

# Game Mechanics
def check_winner(board):
    # Define winning positions
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]

    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != 0:
            return board[pos[0]]
    return 0

def draw_board(board):
    screen.fill(WHITE)

    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), 3)
        pygame.draw.line(screen, BLACK, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), 3)

    # Draw Xs and Os
    for i, cell in enumerate(board):
        x = (i % 3) * CELL_SIZE + CELL_SIZE // 2
        y = (i // 3) * CELL_SIZE + CELL_SIZE // 2
        if cell == 1:
            pygame.draw.line(screen, BLUE, (x - 50, y - 50), (x + 50, y + 50), 5)
            pygame.draw.line(screen, BLUE, (x + 50, y - 50), (x - 50, y + 50), 5)
        elif cell == -1:
            pygame.draw.circle(screen, RED, (x, y), 50, 5)

    pygame.display.flip()

# Main Game Loop
def quantum_tic_tac_toe():
    circuit, qubits = create_quantum_circuit()
    board = [0] * 9  # 0: Empty, 1: Player 1, -1: Player 2
    player = 1
    running = True
    quantum_measured = False

    while running:
        draw_board(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN and not quantum_measured:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                cell_index = row * 3 + col

                if board[cell_index] == 0:  # Check if cell is empty
                    board[cell_index] = player
                    player *= -1

                    # Simulate measurement if all cells are filled
                    if all(cell != 0 for cell in board):
                        measurements = measure_qubits(circuit, qubits)
                        print("Quantum Measurements:", measurements)

                        for i, m in enumerate(measurements):
                            if board[i] == 0:  # Resolve superposition to a classical state
                                board[i] = 1 if m == 1 else -1

                        quantum_measured = True

        winner = check_winner(board)
        if winner != 0:
            draw_board(board)
            text = FONT.render(f"Player {1 if winner == 1 else 2} Wins!", True, BLACK)
            screen.blit(text, (WIDTH // 4, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        if quantum_measured and all(cell != 0 for cell in board):
            draw_board(board)
            text = FONT.render("Draw!", True, BLACK)
            screen.blit(text, (WIDTH // 3, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    pygame.quit()

if __name__ == "__main__":
    quantum_tic_tac_toe()
