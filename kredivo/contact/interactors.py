from enum import Enum

from .entities import Contact

class GetAllContactInteractor:
    def __init__(self, contact_repo):
        self.contact_repo = contact_repo
    
    def execute(self):
        return self.contact_repo.get_all_contact()

class GetContactByIdInteractor:
    def __init__(self, contact_repo):
        self.contact_repo = contact_repo

    def set_params(self, id):
        self.id = id
        return self
    
    def execute(self):
        return self.contact_repo.get_contact_by_id(self.id)

class CreateNewContactInteractor:
    def __init__(self, contact_repo):
        self.contact_repo = contact_repo
    
    def set_params(self, id, phone_number, name, email, photo):
        self.id = id
        self.phone_number = phone_number
        self.name = name
        self.email = email
        self.photo = photo
        return self
    
    def execute(self):
        contact = Contact(id=self.id, phone_number=self.phone_number, name=self.name, email=self.email, photo=self.photo)
        return self.contact_repo.crate_new_contact(contact)

class UpdateContactInteractor:
    def __init__(self, contact_repo):
        self.contact_repo = contact_repo
    
    def set_params(self, id, phone_number, name, email, photo):
        self.id = id
        self.phone_number = phone_number
        self.name = name
        self.email = email
        self.photo = photo
        return self
    
    def execute(self):
        contact = Contact(id=self.id, phone_number=self.phone_number, name=self.name, email=self.email, photo=self.photo)
        return self.contact_repo.update_contact(contact)

class DeleteContactInteractor:
    def __init__(self, contact_repo):
        self.contact_repo = contact_repo

    def set_params(self, id):
        self.id = id
        return self
    
    def execute(self):
        return self.contact_repo.delete_contact(self.id)