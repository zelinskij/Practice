#-------------------------------------------------------------------------------
# Name:        Excercise 2, p20
# Purpose:     Chapter 1 Practice
#
# Author:      Jason Zelinski
#
# Created:     07/08/2015
# Copyright:   (c) Jason Zelinski 2015
#-------------------------------------------------------------------------------

import etree

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman",
                ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

##for each_item in movies:
##    if isinstance(each_item, list):
##        for nested_item in each_item:
##            if isinstance(nested_item, list):
##                for deeper_item in nested_item:
##                    print("Deeper Item: {0}".format(deeper_item))
##            else:
##                print("Nested Item: {0}".format(nested_item))
##    else:
##        print("Each Item: {0}".format(each_item))

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)