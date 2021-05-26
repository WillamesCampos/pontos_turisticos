from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario, ComentarioMotivo


class TestAvaliacoes(APITestCase):
    fixtures = [
        'comentarios/fixtures/motivos_comentarios.json'
    ]

    @classmethod
    def setUpTestData(cls):
        cls.motivo_comentario = ComentarioMotivo.objects.all().first()
        cls.comentario = Comentario.objects.create(
            comentario='Um comentario de teste.',
            aprovado=True,
            motivo=cls.motivo_comentario
        )

        cls.avaliacao = Avaliacao.objects.create(
            comentario=cls.comentario,
            nota=7,
            ativo=True
        )

        cls.client = APIClient()

    def test_listar_avaliacoes(self):
        url = '/backend/avaliacoes/'
        response = self.client.get(
            url, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]['codigo'],
            str(self.avaliacao.codigo)
        )
        self.assertEqual(
            response.data[0]['comentario'],
            self.avaliacao.comentario.codigo
        )
        self.assertTrue(response.data[0]['ativo'])
        self.assertIsInstance(response.data[0]['nota'], int)
