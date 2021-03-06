from datetime import datetime, timedelta
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from atracoes.models import Atracao
from comum.models import Endereco


class TestAtracao(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_listar_atracoes(self):
        endereco = Endereco.objects.create(
            latitude="30°11'22''",
            longitude="136°17'29''",
            cep='45908-766',
            descricao='Rua Tal.'
        )
        atracao = Atracao.objects.create(
            nome='Uma atração teste',
            funciona_feriados=False,
            ativo=True,
            idade_minima=10,
            horario_abertura=datetime.now(),
            horario_fechamento=datetime.now() + timedelta(hours=8),
            endereco=endereco
        )

        url = '/backend/atracoes/'
        response = self.client.get(
            url, format='json'
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data[0]['codigo'],
            str(atracao.codigo)
        )
        self.assertEqual(
            response.data[0]['nome'],
            atracao.nome
        )
        self.assertEqual(
            response.data[0]['idade_minima'],
            atracao.idade_minima
        )
        self.assertTrue(response.data[0]['ativo'])
