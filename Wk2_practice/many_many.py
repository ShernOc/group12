# 3. Many-to-Many Relationship: Students and Clubs

#student class      
class Students:
    def __init__(self,name):
        self.name = name 
        self._clubs= []
   
    def add_club(self,club):
        if club not in self._clubs:
            self._clubs.append(club)
            club.add_students(self)
            
    #Show the list of students 
    def list_club(self):
        # if not self.club
        for club in self._clubs:
            print(f"{self.name} has joined the {club.name} club" )
    
#Clubs class     
class Clubs:
    def __init__(self,name):
        self.name = name
        self._members = []
         
    def add_students(self,student):
        if student not in self._members: 
            self._members.append(student) 

    def list_club_members(self):
        club_members = [students.name for students in self._members]
        return f" {', '.join(club_members)}"
    
        
        
# student objects
mary = Students("Mary")
maluki= Students("Maluki")
jacob= Students("Jacob")
sarah= Students("Sarah")

#club objects
music= Clubs("Music")
games = Clubs("Games")
computer= Clubs("Computer")

#adding clubs to the students 
mary.add_club(music)
mary.add_club(games)
maluki.add_club(computer)
maluki.add_club(music)
sarah.add_club(games)

#Adding students to the clubs
music.add_students(mary)
music.add_students(maluki)
games.add_students(sarah)
computer.add_students(maluki)
computer.add_students(jacob)

#Call the functions 
#list of students in various clubs 
print (f"{music.name} club has {music.list_club_members()}") # mary, maluki 
print(f"{computer.name} club has {computer.list_club_members()}")  #maluki, jacob
print(f"{games.name} club has {games.list_club_members()}") # sarah,mary 

#list of student. 
maluki.list_club() #computer, music
mary.list_club() # music , games 

