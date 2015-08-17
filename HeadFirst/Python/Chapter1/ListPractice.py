#-------------------------------------------------------------------------------
# Name:        ListPractice
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

print(movies[1])

cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(cast[1])

cast.append("Gilliam")
print(cast)

cast.pop()
print(cast)

cast.extend(["Gilliam", "Chapman"])
print(cast)

cast.remove("Chapman")
print(cast)

cast.insert(0, "Chapman")
print(cast)

#----

fav_movies = ["The Holy Grail", "The Life of Brain"]
for each_flick in fav_movies:
    print(each_flick)

#----

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman",
                ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print("\nList of Lists")
print(movies[4][1][3])
print(movies)
isinstance(movies, list)
isinstance(movies, int)
