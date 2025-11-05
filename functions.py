antennaes = int(input("How many antennaes are there? \n"))
eyes = int(input("How many eyes are there?\n"))

def alien_id (an, ey):
    if an >= 3 and ey <=4:
        print("TroyMartian")
    if an <= 6 and ey >= 2:
        print("VladSaturnian")
    if an <= 2 and ey <= 3:
        print("GraemeMercurian")

alien_id(antennaes,eyes)