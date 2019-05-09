from .repository import ContactRepository
from .interactors import GetAllContactInteractor, GetContactByIdInteractor, CreateNewContactInteractor, UpdateContactInteractor, DeleteContactInteractor
from .views import ContactView, ContactDetailView

def create_contact_repo():
    return ContactRepository()

def create_get_all_contact_interactor():
    return GetAllContactInteractor(contact_repo=create_contact_repo())

def create_new_contact_interactor():
    return CreateNewContactInteractor(contact_repo=create_contact_repo())

def create_contacts_view(request, **kwargs):
    return ContactView(get_all_contact_interactor=create_get_all_contact_interactor(), 
            create_new_contact_interactor=create_new_contact_interactor())

def create_get_contact_interactor():
    return GetContactByIdInteractor(contact_repo=create_contact_repo())

def create_update_contact_interactor():
    return UpdateContactInteractor(contact_repo=create_contact_repo())

def create_delete_contact_interactor():
    return DeleteContactInteractor(contact_repo=create_contact_repo())

def create_contact_view(request, **kwargs):
    return ContactDetailView(get_contact_interactor=create_get_contact_interactor(), update_contact_interactor = create_update_contact_interactor(), delete_contact_interactor=create_delete_contact_interactor())