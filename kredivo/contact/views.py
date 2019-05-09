from django.shortcuts import render

from .serializers import ContactSerializers

# Create your views here.
class ContactView:
    def __init__(self, get_all_contact_interactor=None, create_new_contact_interactor=None):
        self.get_all_contact_interactor = get_all_contact_interactor
        self.create_new_contact_interactor = create_new_contact_interactor

    def get(self):
        contact = self.get_all_contact_interactor.execute()

        body = contact
        status = 200
        return body, status

    def post(self, id=None, phone_number=None, name=None, email=None, photo=None):
        contact = self.create_new_contact_interactor.set_params(id=id, phone_number=phone_number, name=name, email=email, photo=photo).execute()
        body = ContactSerializers.serialize(contact)
        status = 201
        return body, status

class ContactDetailView:
    def __init__(self, get_contact_interactor=None, update_contact_interactor=None, delete_contact_interactor=None):
        self.get_contact_interactor = get_contact_interactor
        self.update_contact_interactor = update_contact_interactor
        self.delete_contact_interactor = delete_contact_interactor
    
    def get(self, id):
        contact = self.get_contact_interactor.set_params(id=id).execute()

        body = ContactSerializers.serialize(contact) 
        status = 200
        return body, status
    
    def put(self, id=None, phone_number=None, name=None, email=None, photo=None):
        contact = self.update_contact_interactor.set_params(id=id, phone_number=phone_number, name=name, email=email, photo=photo).execute()

        body = ContactSerializers.serialize(contact)
        status = 200
        return body, status

    def delete(self, id=None):
        contact = self.delete_contact_interactor.set_params(id=id).execute()

        body = "Has been deleted"
        status = 200
        return body, status