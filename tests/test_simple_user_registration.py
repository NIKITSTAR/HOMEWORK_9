from demoqa_tests.application import app
from demoqa_tests.data import users
from demoqa_tests.model.pages.simple_user_registration_page import SimpleUserRegistrationPage


def test_registers_user():
    simple_registration = SimpleUserRegistrationPage()


    simple_registration.open()
    simple_registration.register(users.admin)
    simple_registration.should_have_submited(users.admin)
    print(simple_registration.should_have_submited(users.admin))