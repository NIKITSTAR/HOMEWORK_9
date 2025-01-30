import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


admin = User(full_name='admina adminovych', email='super+admin@gmail.com', current_address='Moscow, Lenina, 25', permanent_address='Moscow, Rasskazovo, 25')
#guest = User('harry', 'potter@hg.com')