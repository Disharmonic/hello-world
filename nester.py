#!/usr/bin/env python

# Global variable, is this what we intended?
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle",
            "Terry Jones"]]]


def print_lol(the_list):
    """This is the "nester.py" module, and it provides one function
     called print_lol() which prints lists that may or may not include nested
     lists."""

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

# A magic invocation method. You can include python files at the top of a
# module like the following snippet:
# import nester
#
# If the above is how this code is executed, this method below will not run.
# This condition is only ever true, if invoked like the following examples:
# $ python nester.py
# ./nester.py

if __name__ == '__main__':
    print_lol(movies)
