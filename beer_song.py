def num_beers(n):
    if n <= 0:
        print " 0 Bottles of beer on the wall"
    else:
        print n, "Bottles of beer on the wall "
        print n, "Bottles of beer"
        print "If one of those bottles should happen to fall"
        print (n -1), "Bottles of beer on the wall\n"

        num_beers(n-1)

num_beers(99)
