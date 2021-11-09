from keyboard import *
from random import *
def start():
    """Teeme valik kellega mängime 
    Tagastame m muutuja int formaadis
    :rtype: int
    """
    print("Kivi,Käärid,Paber")
    m=3
    while m not in [1,2]:
        try:
            m=int(input("Kellega mängime?\n1-botid \n2-robotiga"))
        except:
            ValueError
    return m
def bot_vs_bot(v1:list,v2:list):
    """Robotite mäng
    Näitame ekraanile võitja nime
    :param list v1: järjend esimese roboti jaoks
    :param list v2: järjend teise rovoti jaoks
    """
    while True:
        print("Kas mängime? esc-välja,enter-mängime")
        if read_key()=="esc":
            break
        elif read_key()=="enter":
            p1=choise(v1)
            print("Esimene bot:",p1)
            p2=choise(v2)
            print("Teine bot: ",p2)
       if p1==p2
       print("Viik")
       elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
           print("Võitis 1")
       else:
           print("Võitis 2")

