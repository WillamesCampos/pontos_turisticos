from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario, ComentarioMotivo
from usuarios.models import User, Perfil
from comum.models import Endereco


class TestAvaliacoes(APITestCase):
    fixtures = [
        'comentarios/fixtures/motivos_comentarios.json'
    ]

    @classmethod
    def setUpTestData(cls):
        endereco = Endereco.objects.create(
            latitude="30°11'22''",
            longitude="136°17'29''",
            cep='45908-766',
            descricao='Rua Tal.'
        )

        perfil = Perfil.objects.create(
            documento='32211145753'
        )
        cls.usuario = User.objects.create(
            first_name='Fulano',
            last_name='de Tal',
            email='fulano@email.com',
            username='fulano@email.com',
            password='123',
            perfil=perfil,
            endereco=endereco
        )

        cls.motivo_comentario = ComentarioMotivo.objects.all().first()
        cls.comentario = Comentario.objects.create(
            comentario='Um comentario de teste.',
            aprovado=True,
            motivo=cls.motivo_comentario
        )

        cls.avaliacao = Avaliacao.objects.create(
            usuario=cls.usuario,
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
