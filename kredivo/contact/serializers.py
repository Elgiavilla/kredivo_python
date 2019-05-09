class MultipleContactSeralizer:
    @staticmethod
    def seralize(contacts):
        return [ContactSerializers.serialize(contact) for contact in contacts]

class ContactSerializers(object):
    @staticmethod
    def serialize(contact):
        return {
            'id': str(contact.id),
            'phone_number':contact.phone_number,
            'name':contact.name,
            'email':contact.email,
            'photo':contact.photo
        }