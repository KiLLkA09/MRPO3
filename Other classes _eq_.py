class Customer:
    def __init__(self, customer_id, name, contact_info, address):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.address = address

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return False
        return (self.customer_id == other.customer_id and
                self.name == other.name and
                self.contact_info == other.contact_info and
                self.address == other.address)

class Seller:
    def __init__(self, seller_id, name, contact_info, position):
        self.seller_id = seller_id
        self.name = name
        self.contact_info = contact_info
        self.position = position

    def __eq__(self, other):
        if not isinstance(other, Seller):
            return False
        return (self.seller_id == other.seller_id and
                self.name == other.name and
                self.contact_info == other.contact_info and
                self.position == other.position)
