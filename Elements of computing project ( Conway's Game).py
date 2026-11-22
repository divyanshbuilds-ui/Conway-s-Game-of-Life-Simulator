
import time

# CONWAY'S GAME OF LIFE SIMULATOR

# Starting patterns
PATTERNS = {
    "glider": [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ],

    "blinker": [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],

    "block": [
        [1, 1],
        [1, 1]
    ]
}

SIZE = 20
MAX_GENERATIONS = 100


# Create the main grid
def create_grid(pattern):
    grid = []

    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            row.append(0)
        grid.append(row)

    start_row = (SIZE - len(pattern)) // 2
    start_col = (SIZE - len(pattern[0])) // 2

    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            grid[start_row + i][start_col + j] = pattern[i][j]

    return grid


# Count living neighbours
def count_neighbours(grid, row, col):
    count = 0

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):

            if i == row and j == col:
                continue

            if 0 <= i < SIZE and 0 <= j < SIZE:
                if grid[i][j] == 1:
                    count += 1

    return count


# Create the next generation
def next_generation(grid):
    new_grid = []

    for i in range(SIZE):
        row = []

        for j in range(SIZE):
            neighbours = count_neighbours(grid, i, j)

            if grid[i][j] == 1:


                # Survival rule
                if neighbours == 2 or neighbours == 3:
                    row.append(1)
                else:
                    row.append(0)

            else:

                # Birth rule
                if neighbours == 3:
                    row.append(1)
                else:
                    row.append(0)

        new_grid.append(row)

    return new_grid


# Display the grid
def display_grid(grid, generation):
    print("\nGeneration:", generation)

    for row in grid:
        for cell in row:
            if cell == 1:
                print("■", end=" ")
            else:
                print(".", end=" ")
        print()

    print("----------------------------------------")


# Run the simulation
def run_simulation(pattern):

    grid = create_grid(pattern)

    # Store previously visited patterns
    previous_states = {}

    generation = 0

    while generation < MAX_GENERATIONS:

        display_grid(grid, generation)

        current_state = str(grid)

        # Check for repeating pattern
        if current_state in previous_states:
            old_generation = previous_states[current_state]

            print("\nPattern is repeating!")
            print("It repeated after",
                  generation - old_generation, "generations.")
            break

        previous_states[current_state] = generation

        # Calculate next generation
        new_grid = next_generation(grid)

        # Check for stable pattern
        if new_grid == grid:
            print("\nPattern is stable!")
            break

        grid = new_grid
        generation += 1

        time.sleep(0.2)

    else:

        print("\nMaximum generations reached!")

    print("\nTotal Generations:", generation)
    print("Simulation completed!")


# MAIN PROGRAM
print("================================")
print("   CONWAY'S GAME OF LIFE")
print("================================")

print("1. Glider")
print("2. Blinker")
print("3. Block")

choice = input("Choose a pattern (1, 2 or 3): ")

if choice == "1":
    run_simulation(PATTERNS["glider"])

elif choice == "2":
    run_simulation(PATTERNS["blinker"])

elif choice == "3":
    run_simulation(PATTERNS["block"])

else:
    print("Invalid choice! Please select 1, 2 or 3.")

