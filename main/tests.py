from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_not_contains_unexpected_text(self):
        response = Client().get('/main/')
        unexpected_text = 'Unexpected Texts'
        self.assertNotContains(response, unexpected_text)

