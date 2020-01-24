class ArrogantProfessor(Professor):
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)