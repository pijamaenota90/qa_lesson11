
from pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Alex')
    registration_page.fill_last_name('Alexov')
    registration_page.fill_email('alex.alexov@mail.ru')
    registration_page.select_gender('Male')
    registration_page.fill_mobile_number('1234567890')
    registration_page.select_date_of_birth('26 November,1990')
    registration_page.fill_subjects('History')
    registration_page.fill_hobbies('Reading')
    registration_page.upload_picture('foto.jpg')
    registration_page.fill_address('address')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')

    registration_page.click_submit()
    # THEN
    registration_page.should_registered_user_with(
        full_name='Alex Alexov',
        email='alex.alexov@mail.ru',
        gender='Male',
        mobile_number='1234567890',
        date_of_birth='26 November,1990',
        subjects='History',
        hobbies='Reading',
        upload_picture='foto.jpg',
        address='address',
        state_and_city='NCR Delhi',
    )


