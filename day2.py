# acess list items
thislist = [ "wild", "animals", "forest", "melon"]
print(thislist[-2:-3])
print(thislist[:4])
thislist = ["apple", "banana", "melon", "cherry", "wind"]
if "apple" in thislist:
    print("Yes, 'apple' is in list")

    thislist[1] = "blackcurrant"
    print(thislist)
    thislist[1:3] = ["blackcurrant", "forest"]
    print(thislist)
    thislist.insert(4, "gump")
    print(thislist)
