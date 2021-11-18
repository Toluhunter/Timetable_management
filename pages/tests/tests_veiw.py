from django.test import TestCase

# Create your tests here

class TestVeiw(TestCase):

    def setUp(self):

        self.response_home = self.client.get("/")
        self.response_about = self.client.get("/about/")
        self.response_contact = self.client.get("/contact/")
        return super().setUp()

    def test_status_code(self):

        self.assertEquals(self.response_about.status_code, 200)
        self.assertEquals(self.response_home.status_code, 200)
        self.assertEquals(self.response_contact.status_code, 200)
    
    def test_template_used(self):

        self.assertTemplateUsed(self.response_about, "about.html")
        self.assertTemplateUsed(self.response_home, "index.html")
        self.assertTemplateUsed(self.response_contact, "contact.html")