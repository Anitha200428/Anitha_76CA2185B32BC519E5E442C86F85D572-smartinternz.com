class player:
  def play(self): 
     print("The player is playing cricket.")

class Batsman(player): 
  def play(self):
     print("The batsman is batting.")

class bowler(player):
  def play(self):
     print("The bowler is bowling.")

batsman=Batsman()
bowler=bowler()

batsman.play()
bowler.play()
