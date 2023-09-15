#define the base class player
class player:
  def play (self):
    print("the player is playing cricket")
#define the derved class Batsman
class Batsman (player):
  def play (self):
      print("the batsman is batting")
#define the derived class bowler
class Bowler (player):
  def play (self):
    print ("the bowler is bowling.")
#creat object of batsman and bowler classes
batsman=Batsman()
bowler=Bowler()
#call the play() method for each object
batsman.play()
bowler.play()