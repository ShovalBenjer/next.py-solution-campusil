def check_id_valid(id_number):
    """
    Check if the given ID number is valid.

    Parameters
    ----------
    id_number : int
        A 9-digit number to be checked.

    Returns
    -------
    bool
        True if the ID is valid, False otherwise.

    Notes
    -----
    - The function checks the validity of the ID number based on the following steps:
        1. Verify that the length of the ID number is 9, and it is of type int.
        2. Convert the ID number to a string for iteration.
        3. Create a multiplied_list where every even-positioned digit in the ID number is multiplied by 2.
        4. Create a summed_list where numbers greater than 10 have their two digits summed up,
           and then sum all the resulting numbers together.
        5. Return True if the sum in summed_list is divisible by 10 without a remainder, indicating a valid ID.
           Otherwise, return False.

    Raises
    ------
    ValueError
        If the provided ID number is not a 9-digit integer.

    """
    id_str = str(id_number)

    if len(id_str) != 9 or not id_str.isnumeric():
        raise ValueError("Invalid ID number. Please provide a 9-digit integer.")

    multiplied_list = [int(digit) * 2 if (index + 1) % 2 == 0 else int(digit) for index, digit in enumerate(id_str)]
    summed_list = sum([num if num < 10 else (num // 10) + (num % 10) for num in multiplied_list])
    return summed_list % 10 == 0


class IDIterator:
    """
    An iterator class that generates valid ID numbers within a given range.

    Parameters
    ----------
    id_ : int
        The starting ID number from which to generate new IDs.

    Methods
    -------
    __iter__()
        Returns the iterator object itself.
    __next__()
        Generates the next valid ID number within the specified range.

    Notes
    -----
    - The `IDIterator` class generates valid ID numbers based on a starting ID.
    - The validity of each ID number is determined by the `check_id_valid` function.
    - The iterator generates the next valid ID number in each iteration until a valid ID is found.
    - The class implements the iterator protocol by defining the `__iter__` and `__next__` methods.

    """

    def __init__(self, id_):
        """
        Initialize the IDIterator object with a starting ID.

        Parameters
        ----------
        id_ : int
            The starting ID number from which to generate new IDs.
        """
        self.id_ = id_

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns
        -------
        IDIterator
            The iterator object itself.
        """
        return self

    def __next__(self):
        """
        Generate the next valid ID number within the specified range.

        Returns
        -------
        int
            The next valid ID number.

        Raises
        ------
        StopIteration
            If a valid ID number cannot be found within the range.

        Notes
        -----
        - The method uses a while loop to continuously increment the ID number until a valid ID is found.
        - The validity of each ID number is checked using the `check_id_valid` function.
        - If a valid ID is found, it is returned as the next ID number.
        - If a valid ID cannot be found within the range, a StopIteration exception is raised.
        """
        while True:
            if check_id_valid(self.id_):
                current_id = self.id_
                self.id_ += 1
                return current_id
            else:
                self.id_ += 1


def id_generator(id_number):
    """
    A generator function that generates valid ID numbers within a given range.

    Parameters
    ----------
    id_number : int
        The starting ID number from which to generate new IDs.

    Yields
    ------
    int
        The next valid ID number within the specified range.

    Notes
    -----
    - The `id_generator` function generates valid ID numbers based on a starting ID.
    - The validity of each ID number is determined by the `check_id_valid` function.
    - The generator generates the next valid ID number in each iteration until a valid ID is found.
    - The function uses a while loop to continuously increment the ID number until a valid ID is found.
    - The generation of ID numbers stops when the maximum valid ID number is reached (999999999).

    Raises
    ------
    ValueError
        If the provided starting ID number is not a 9-digit integer.

    """

    if len(str(id_number)) != 9 or not isinstance(id_number, int):
        raise ValueError("Invalid starting ID number. Please provide a 9-digit integer.")

    while id_number <= 999999999:
        if check_id_valid(id_number):
            yield id_number
        id_number += 1


def main():
    """
    Main function for generating new ID numbers.

    This function prompts the user to enter an ID number and a choice of either using an iterator or a generator
    to generate new ID numbers based on the provided starting ID. It then generates and prints the next 10 valid
    ID numbers.

    Raises
    ------
    ValueError
        If the provided ID number is not a 9-digit integer or the choice is invalid.
    RuntimeError
        If the function is interrupted by the user.

    """
    try:
        new_id = input("Enter ID: ")
        if len(new_id) != 9 or not new_id.isnumeric() or int(new_id) < 100000000:
            raise ValueError("Invalid ID number. Please enter a 9-digit number greater than or equal to 100000000.")
        start_id = int(new_id)

        choice = input("Enter 'it' for iterator or 'gen' for generator: ")

        if choice == "it":
            iterator = IDIterator(start_id)
            new_ids = []
            for _ in range(10):
                try:
                    new_id = next(iterator)
                    new_ids.append(new_id)
                except StopIteration:
                    break

        elif choice == "gen":
            generator = id_generator(start_id)
            new_ids = [next(generator) for _ in range(10)]

        else:
            raise ValueError("Invalid choice. Please enter 'it' or 'gen'.")

        for id_num in new_ids:
            print(id_num)

    except ValueError as error:
        print(str(error))
    except KeyboardInterrupt:
        raise RuntimeError("Function interrupted by the user.")


if __name__ == "__main__":
    main()
