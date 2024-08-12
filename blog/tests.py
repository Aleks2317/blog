from django.test import SimpleTestCase  #  Поскольку пока не задействована база данных, мы импортируем SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        ''' Проверка URL. При положительном ответе возвращает HTTP код состояния 200. '''
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_url_available_by_name(self):
        ''' Проверка имени url'''
        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)

    def test_template_name_correct(self):
        ''' проверка на правильность вызываемого шаблона '''
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "blog/index.html")

    def test_template_content(self):
        ''' Проверка на зодержимае шаблона '''
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Index")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_location(self):
        ''' Проверка URL. При положительном ответе возвращает HTTP код состояния 200. '''
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        ''' Проверка имени url'''
        response = self.client.get(reverse("about"))
        self.assertEquals(response.status_code, 200)

    def test_template_name_correct(self):
        ''' проверка на правильность вызываемого шаблона '''
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "blog/about.html")

    def test_template_content(self):
        ''' Проверка на зодержимае шаблона '''
        response = self.client.get(reverse("about"))
        self.assertContains(response, "О нас")
# Для запуска тестов python manage.py test
