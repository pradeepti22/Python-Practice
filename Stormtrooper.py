class Stormtrooper:
    StormtrooperCount=0;

    def __int__(self, ID, Rank, Height, Weight):
        self.ID = IDNumber
        self.Rank = Rank
        self.Height = Height
        self.Weight = Weight

        Stormtrooper.StormtrooperCount +=1

    def Moves(self, destination):
        print('I am moving to ' + destination)

    def FiresWeapon(self, target):
        print('I am firing at ' + target)

    def Reports(self):
        print('I am Stormtrooper' + self.ID)
