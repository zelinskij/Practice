#-------------------------------------------------------------------------------
# Name:        Excercise 1, p13
# Purpose:     Chapter 1 Practice
#
# Author:      Jason Zelinski
#
# Created:     07/08/2015
# Copyright:   (c) Jason Zelinski 2015
#-------------------------------------------------------------------------------

movies = ["The Holy Grail",
          "The Life of Brain",
          "The Meaning of Life"]

movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)
print(movies)

movies = ["The Holy Grail", 1975,
          "The Life of Brain", 1979,
          "The Meaning of Life", 1983]
print(movies)