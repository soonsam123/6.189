class Speel:
    def __init__(self, incantation, name):
        self.incantation = incantation
        self.name = name
    def __str__(self):
        return self.name + ' ' + self.incantation + "\n" + self.get_description()
    def get_description(self):
        return "No description"
    def execute(self):
        print self.incantation
class Accio(Speel):
    def __init__(self):
        Speel.__init__(self, "Accio", "Summoning Charm")
    def get_description(self):
        return "This cram summons an object to the caster, potentially over a significant distance"
class Confundo(Speel):
    def __init__(self):
        Speel.__init__(self, "Confundo", "Confundus Charm")
    def get_description(self):
        return "Causes the victim to become confused and befuddled"
def study_speel(speel):
    print speel
speel = Accio()
print speel.execute()
#'Accio'
#None
study_speel(speel)
#Summoning Charm Accio
#No description
study_speel(Confundo())
#Confundus Charm Confundo
#Causes the victim to become confused and befuddled

print "------------------------------------------"#Organazing
#**************************Exercise 4.6***********************
class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num
class CampusAddress(Address):
    def __init__(self, office_number):
        self.office_number = office_number
        Address.__init__(self, "Massachusetts Ave", 77)
Sarina_addr = CampusAddress("32-G904")
print Sarina_addr.office_number
#'32-G904'
print Sarina_addr.street_name
#'Massachusetts Ave'
print Sarina_addr.number
#77
