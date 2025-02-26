import random
import time


# Function to do insertion sort (like sorting playing cards)
def insertion_sort(a_list):
    # Record the start time
    start_time = time.time()

    # Loop through the list, starting from the second element
    for index in range(1, len(a_list)):
        # Store the current value we're looking at
        current_value = a_list[index]
        # Store the position of the previous element
        position = index - 1

        # Keep moving the current value back until it's in the right place
        while position >= 0 and a_list[position] > current_value:
            # Shift the previous element forward
            a_list[position + 1] = a_list[position]
            # Move to the next previous element
            position = position - 1

        # Put the current value in its correct spot
        a_list[position + 1] = current_value

    # Record the end time
    end_time = time.time()

    # Return how long it took
    return end_time - start_time


# Function to do shell sort (an improved insertion sort)
def shell_sort(a_list):
    # Record the start time
    start_time = time.time()

    # Start with large gaps and gradually reduce them
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        # Loop through each sublist
        for start_position in range(sublist_count):
            # Sort the sublist using a gap insertion sort
            gap_insertion_sort(a_list, start_position, sublist_count)

        # Reduce the gap size for the next iteration
        sublist_count = sublist_count // 2

    # Record the end time
    end_time = time.time()

    # Return how long it took
    return end_time - start_time


# Helper function for shell sort (like insertion sort with gaps)
def gap_insertion_sort(a_list, start, gap):
    # Loop through the sublist, starting from the second element
    for i in range(start + gap, len(a_list), gap):
        # Store the current value we're looking at
        current_value = a_list[i]
        # Store the position of the previous element
        position = i - gap

        # Keep moving the current value back until it's in the right place
        while position >= 0 and a_list[position] > current_value:
            # Shift the previous element forward
            a_list[position + gap] = a_list[position]
            # Move to the next previous element
            position = position - gap

        # Put the current value in its correct spot
        a_list[position + gap] = current_value


# Function to use Python's built-in sort (very fast!)
def python_sort(a_list):
    # Record the start time
    start_time = time.time()

    # Use Python's built-in sort function
    a_list.sort()

    # Record the end time
    end_time = time.time()

    # Return how long it took
    return end_time - start_time


def main():
    # Different sizes of lists to test
    list_sizes = [500, 1000, 5000]

    # Number of times to run each sort for each list size
    num_iterations = 100

    # All the sort functions we want to test
    sort_functions = [insertion_sort, shell_sort, python_sort]

    # Names of the sort functions (for printing)
    function_names = ["Insertion Sort", "Shell Sort", "Python Sort"]

    # Loop through each list size
    for size in list_sizes:
        print(f"\nList size: {size}")  # Print the current list size

        # Loop through each sort function
        for func, name in zip(sort_functions, function_names):
            total_time = 0.0  # Keep track of total time for this function

            # Run the sort many times to get an average
            for _ in range(num_iterations):
                # Create a random list of numbers
                a_list = random.sample(range(size * 10), size)

                # Sort the list using the current function
                time_taken = func(a_list)

                # Add the time taken to the total time
                total_time += time_taken

            # Calculate the average time
            average_time = total_time / num_iterations

            # Print the results for this function and list size
            print(f"{name} took {average_time:10.7f} seconds to run, on average")


# Run the main function if this script is executed
if __name__ == '__main__':
    main()