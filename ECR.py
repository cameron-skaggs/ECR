#This is the constructor for the ECR class
class Ecr:

    def __init__(self, number, initiator, owner, status):
        self.number = number
        self.initiator = initiator
        self.owner = owner
        self.status = status

    def get_owner(self):
        return self.owner
    def get_status(self):
        return self.status
