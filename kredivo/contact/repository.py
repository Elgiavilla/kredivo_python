from .models import ORMContact
from .entities import Contact

class ContactRepository:
    def _decode_db_contact(self, db_contact):
        return Contact(id=db_contact.id,phone_number=db_contact.phone_number, name=db_contact.name, email=db_contact.email, photo=db_contact.photo)
    
    def get_all_contact(self):
        all_contacts = ORMContact.objects.values().order_by('-id')
        contacts = []
        for all_contact in all_contacts:
            contacts.append(all_contact)
        return contacts 


    def get_contact_by_id(self, id):
        try:
            db_contact = ORMContact.objects.get(id=id)
            return self._decode_db_contact(db_contact)
        except ORMContact.DoesNotExist:
            return "No data valid"

    def crate_new_contact(self, contact):
        db_contact = ORMContact.objects.create(phone_number=contact.phone_number, name=contact.name, email=contact.email, photo=contact.photo)
        return self._decode_db_contact(db_contact)

    def update_contact(self, contact):
        orm_contact = ORMContact.objects.get(id=contact.id)
        orm_contact.phone_number = contact.phone_number
        orm_contact.name = contact.name
        orm_contact.email = contact.email
        orm_contact.photo = contact.photo
        orm_contact.save()
        return self._decode_db_contact(orm_contact)

    def delete_contact(self, id):
        orm_contact = ORMContact.objects.get(id=id)
        orm_contact.delete()
        return self._decode_db_contact(orm_contact)