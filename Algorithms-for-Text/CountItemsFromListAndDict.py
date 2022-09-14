# on 14 - 9 - 2022
# how to count items in python used lists snd dictionaries.

from http.client import FOUND


def CountItems():

    itemsfound = 0
    itemsnotfound = 0

    DictionaryItems = {"Iphone":20 , "Samsung":50 , "Motorila":10}
    ListsItems      = ["Iphone" , "Samsung" ,"Hawawi"]

    for objects , count in DictionaryItems.items():

        if objects in ListsItems :

            itemsfound += count 

        else :

            itemsnotfound += count

    print(f" The Count items fount in list and dictionary is {itemsfound} And the count items not fount is {itemsnotfound}")

CountItems()