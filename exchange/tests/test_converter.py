from django.test import TestCase


class TestConversionCase(TestCase):
    fixtures = ['./exchange/tests/fixtures/fixtures.json']

    def test_conversion_result(self):
        data = {
            'currency_from': 'USD',
            'currency_to': 'EUR',
            'amount': 2,

        }
        response = self.client.post("/convert/", data)
        self.assertEqual(b'{"result": 1.824506}', response.content)

    def test_negative_amount(self):
        data = {
            'currency_from': 'USD',
            'currency_to': 'EUR',
            'amount': -2,

        }
        response = self.client.post("/convert/", data)
        self.assertEqual(
            b'{"errors": {"amount": ["Ensure this value is greater than or equal to 0."]}}',
            response.content)

    def test_not_number_amount(self):
        data = {
            'currency_from': 'USD',
            'currency_to': 'EUR',
            'amount': 'not number',

        }
        response = self.client.post("/convert/", data)
        self.assertEqual(
            b'{"errors": {"amount": ["Enter a number."]}}',
            response.content)

    def test_incorrect_currency_length(self):
        data = {
            'currency_from': 'incorrect',
            'currency_to': 'EUR',
            'amount': 1,

        }
        response = self.client.post("/convert/", data)
        self.assertContains(
            response,
            b'{"errors": {"currency_from": ["Ensure this value has',
        )

    def test_incorrect_currency(self):
        data = {
            'currency_from': 'INC',
            'currency_to': 'EUR',
            'amount': 1,

        }
        response = self.client.post("/convert/", data)
        self.assertEqual(
            response.content,
            b'{"errors": {"currency_from": ["Not valid currency"]}}'
        )

    def test_empty_amount(self):
        data = {
            'currency_from': 'USD',
            'currency_to': 'EUR',
            'amount': '',

        }
        response = self.client.post("/convert/", data)
        self.assertEqual(
            response.content,
            b'{"errors": {"amount": ["This field is required."]}}'
        )

    def test_empty_from_currency(self):
        data = {
            'currency_from': '',
            'currency_to': 'EUR',
            'amount': 1,

        }
        response = self.client.post("/convert/", data)
        self.assertEqual(
            response.content,
            b'{"errors": {"currency_from": ["This field is required."]}}'
        )

    def test_empty_to_currency(self):
        data = {
            'currency_from': 'USD',
            'currency_to': '',
            'amount': 1,

        }
        response = self.client.post("/convert/", data)
        self.assertEqual(
            response.content,
            b'{"errors": {"currency_to": ["This field is required."]}}'
        )
