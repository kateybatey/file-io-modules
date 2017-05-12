""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.
    fruits = open(filename)
    return fruits.read().split("\n")



def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    #results = []

    for item in fruit_list_1:
        if item in fruit_list_2:
            print item



# Call your functions at the bottom, after they've been defined.
fruit_list_1 = open_and_read_file("fruits_1.txt")
fruit_list_2 = open_and_read_file("fruits_2.txt")
compare(fruit_list_1, fruit_list_2)