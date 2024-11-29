from django.test import TestCase

class DocumentTest(TestCase):
    def test_document_creation(self):
        document = Document.objects.create(
            document_number='12345',
            document_file='path/to/file.pdf'
        )
        self.assertEqual(document.document_number, '12345')
