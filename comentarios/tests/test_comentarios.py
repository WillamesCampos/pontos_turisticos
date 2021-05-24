from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from comentarios.models import Comentario, ComentarioMotivo


class TestComentario(APITestCase):
    fixtures = [
        'comentarios/fixtures/motivos_comentarios.json'
    ]

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

        motivos_queryset = ComentarioMotivo.objects.all()

        cls.motivos = {}
        for motivo in motivos_queryset:
            cls.motivos[motivo.descricao] = {
                'descricao': motivo.descricao,
                'instancia': motivo
            }

        cls.comentario = Comentario.objects.create(
            comentario='Comentario Teste',
            motivo=cls.motivos['Gostei.']['instancia'],
            aprovado=True
        )

    def test_listar_comentarios(self):
        url = '/backend/comentarios/'
        response = self.client.get(
            url, format='json'
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data[0]['codigo'],
            str(self.comentario.codigo)
        )
        self.assertEqual(
            response.data[0]['motivo'],
            self.comentario.motivo.codigo
        )
        self.assertTrue(response.data[0]['aprovado'])
        self.assertFalse(response.data[0]['improprio'])
