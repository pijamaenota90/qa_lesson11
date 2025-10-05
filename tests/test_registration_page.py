from pages.registration_page import RegistrationPage
from users import create_student


def test_student_registration_form():
    registration_page = RegistrationPage()
    student = create_student()

    # WHEN
    registration_page.open()
    registration_page.register(student)
    registration_page.submit()
    # THEN
    registration_page.should_have_registered(student)

