import matplotlib.pyplot as plt

def visualize_tape(tape, head_position):
    """Visualiza la cinta de Turing.

    Args:
        tape: Una lista representando la cinta.
        head_position: La posición del cabezal en la cinta.
    """

    plt.figure(figsize=(10, 2))
    plt.axis('off')
    plt.text(0, 0, ' '.join(tape), ha='center')
    plt.plot(head_position, 0, 'ro', markersize=15)
    plt.show()

def simulate_turing_machine(tape, transitions):
    """Simula una máquina de Turing.

    Args:
        tape: Una lista representando la cinta inicial.
        transitions: Un diccionario definiendo la función de transición.

    Returns:
        La cinta final después de la operación.
    """

    head_position = 0
    state = 'A'

    while state != '@':
        visualize_tape(tape, head_position)  # Visualiza la cinta actual
        symbol = tape[head_position]
        next_state, write_symbol, direction = transitions[(state, symbol)]
        tape[head_position] = write_symbol
        if direction == '>':
            head_position += 1
        elif direction == '<':
            head_position -= 1
        state = next_state

    return tape

# Inicializamos la cinta para representar 8 + 7
tape = ['1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1']  # 8 + 7
# Definimos las transiciones para esta operación específica
transitions = {
    ('A', '1'): ('A', '1', '>'),
    ('A', '0'): ('B', '0', '>'),
    ('B', '1'): ('B', '1', '>'),
    ('B', '0'): ('@', '1', '>')
}

final_tape = simulate_turing_machine(tape, transitions)

# Convertimos la cinta final en un número decimal y lo imprimimos
result_decimal = sum(2**i for i, bit in enumerate(reversed(final_tape)) if bit == '1')
print("Resultado decimal:", result_decimal)
