class Contact:
    def __init__(self, phone_number, name, email, photo, id=None):
        self._id = id
        self._phone_number = phone_number
        self._name = name
        self._email = email
        self._photo = photo
    
    @property
    def id(self):
        return self._id
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email
    
    @property
    def photo(self):
        return self._photo

    def builder(self):
        return Contact.Builder(self)
    
    class Builder:
        def __init__(self, contact):
            self._id = contact.id
            self._phone_number = contact.phone_number
            self._name = contact.name
            self._email = contact.email
            self._photo = contact.photo
        
        def id(self, id):
            self._id = id
            return self
        
        def phone_number(self, phone_number):
            self._phone_number = phone_number
            return self
        
        def name(self, name):
            self._name = name
            return self
        
        def email(self, email):
            self._email = email
            return self
        
        def photo(self, photo):
            self._photo = photo
            return self
        
        def build(self):
            return Contact(id=self._id, phone_number=self._phone_number, name=self._name, email=self._email, photo=self._photo)
    
    