import time
import random

import random
import time

# Function to do a simple search, checking each item one by one
def sequential_search(a_list, item_to_find):
    # Record the start time
    start_time = time.time()

    # We haven't found the item yet
    found = False

    # Start at the beginning of the list
    position = 0

    # Keep looking until we reach the end of the list or find the item
    while position < len(a_list) and not found:
        # Check if the current item is the one we're looking for
        if a_list[position] == item_to_find:
            # If it is, we found it!
            found = True
        else:
            # If not, move to the next item
            position = position + 1

    # Record the end time
    end_time = time.time()

    # Return whether we found the item and how long it took
    return found, end_time - start_time

# Function to do a search in a sorted list, stopping early if we pass the item
def ordered_sequential_search(a_list, item_to_find):
    # Sort the list first (important for this search to work)
    a_list.sort()

    # Record the start time
    start_time = time.time()

    # We haven't found the item yet
    found = False

    # We haven't passed the item yet
    stop = False

    # Start at the beginning of the list
    position = 0

    # Keep looking until we reach the end, find the item, or pass it
    while position < len(a_list) and not found and not stop:
        # Check if the current item is the one we're looking for
        if a_list[position] == item_to_find:
            # If it is, we found it!
            found = True
        else:
            # If not, check if we've passed the item
            if a_list[position] > item_to_find:
                # If we have, stop searching
                stop = True
            else:
                # If not, move to the next item
                position = position + 1

    # Record the end time
    end_time = time.time()

    # Return whether we found the item and how long it took
    return found, end_time - start_time

# Function to do a binary search (like looking in a phone book)
def binary_search_iterative(a_list, item_to_find):
    # Sort the list first (important for this search to work)
    a_list.sort()

    # Record the start time
    start_time = time.time()

    # We haven't found the item yet
    found = False

    # Start at the beginning and end of the list
    first = 0
    last = len(a_list) - 1

    # Keep looking until we find the item or our search range is empty
    while first <= last and not found:
        # Find the middle item
        midpoint = (first + last) // 2

        # Check if the middle item is the one we're looking for
        if a_list[midpoint] == item_to_find:
            # If it is, we found it!
            found = True
        else:
            # If not, adjust our search range
            if item_to_find < a_list[midpoint]:
                # Search in the first half
                last = midpoint - 1
            else:
                # Search in the second half
                first = midpoint + 1

    # Record the end time
    end_time = time.time()

    # Return whether we found the item and how long it took
    return found, end_time - start_time

# Function to do a binary search using recursion (calling itself)
def binary_search_recursive(a_list, item_to_find):
    # Sort the list first (important for this search to work)
    a_list.sort()

    # Record the start time
    start_time = time.time()

    # Helper function that does the actual searching
    def binary_search_helper(a_list, item_to_find, first, last):
        # If our search range is empty, we didn't find the item
        if first > last:
            return False
        else:
            # Find the middle item
            midpoint = (first + last) // 2

            # Check if the middle item is the one we're looking for
            if a_list[midpoint] == item_to_find:
                # If it is, we found it!
                return True
            else:
                # If not, adjust our search range and call ourselves again
                if item_to_find < a_list[midpoint]:
                    # Search in the first half
                    return binary_search_helper(a_list, item_to_find, first, midpoint - 1)
                else:
                    # Search in the second half
                    return binary_search_helper(a_list, item_to_find, midpoint + 1, last)

    # Call the helper function to start the search
    found = binary_search_helper(a_list, item_to_find, 0, len(a_list) - 1)

    # Record the end time
    end_time = time.time()

    # Return whether we found the item and how long it took
    return found, end_time - start_time

def main():
    # Different sizes of lists to test
    list_sizes = [500, 1000, 5000]

    # Number of times to run each search for each list size
    num_iterations = 100

    # All the search functions we want to test
    search_functions = [sequential_search, ordered_sequential_search, binary_search_iterative, binary_search_recursive]

    # Names of the search functions (for printing)
    function_names = ["Sequential Search", "Ordered Sequential Search", "Binary Search Iterative", "Binary Search Recursive"]

    # Loop through each list size
    for size in list_sizes:
        print(f"\nList size: {size}")  # Print the current list size

        # Loop through each search function
        for func, name in zip(search_functions, function_names):
            total_time = 0.0  # Keep track of total time for this function

            # Run the search many times to get an average
            for _ in range(num_iterations):
                # Create a random list of numbers
                a_list = random.sample(range(size * 10), size)

                # Search for a number that's not in the list (worst case)
                _, time_taken = func(a_list, 99999999)

                # Add the time taken to the total time
                total_time += time_taken

            # Calculate the average time
            average_time = total_time / num_iterations

            # Print the results for this function and list size
            print(f"{name} took {average_time:10.7f} seconds to run, on average")

# Run the main function if this script is executed
if __name__ == '__main__':
    main()