import matplotlib.pyplot as plt

def visualize_tape(tape, head_position):
    """Visualizes the Turing machine tape.

    Args:
        tape: A list representing the tape.
        head_position: The current position of the head.
    """

    plt.figure(figsize=(10, 2))
    plt.axis('off')
    plt.text(0, 0, ' '.join(tape), ha='center')
    plt.plot(head_position, 0, 'ro', markersize=15)
    plt.show()

def simulate_turing_machine(tape, transitions):
    """Simulates a Turing machine.

    Args:
        tape: A list representing the initial tape.
        transitions: A dictionary defining the transition function.

    Returns:
        The final tape configuration.
    """

    head_position = 0
    state = 'A'

    while state != '@':
        visualize_tape(tape, head_position)  # Visualize the current tape state
        symbol = tape[head_position]
        next_state, write_symbol, direction = transitions[(state, symbol)]
        tape[head_position] = write_symbol
        if direction == '>':
            head_position += 1
        elif direction == '<':
            head_position -= 1
        state = next_state

    return tape

# Example usage:
tape = ['0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '0']
transitions = {
    ('A', '0'): ('A', '0', '>'),
    ('A', '1'): ('B', '0', '>'),
    ('B', '1'): ('B', '1', '>'),
    ('B', '0'): ('@', '1', '>')
}

final_tape = simulate_turing_machine(tape, transitions)
print(final_tape)

