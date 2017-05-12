class Patients(object):
    def __init__(self, id, name, allergies, bed_number):
        self.id = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = 0


class Hospital(object):
    def __init__(self):
        self.patients = []
        self.name = "Coding Dojo"
        self.capacity = 5

    def admit(self, person):
            if (self.patients >= self.capacity):
                print "Hospital is full"
            else:
                print "Patient is admitted"
                self.patients.append(person)
                self.bed_number += 1
        return self

    def discharge(self):




