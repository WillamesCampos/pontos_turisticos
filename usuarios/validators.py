from rest_framework.exceptions import ValidationError
from validate_docbr import CPF, CNPJ


def valida_documento(value):
    '''
        Valida CPF e CNPJ dependendo do tamanho do documento passado.
    '''
    if len(value) == 11:
        cpf = CPF()
        try:
            assert cpf.validate(value)
        except AssertionError:
            raise ValidationError(
                {
                    'erro': 'Documento inválido!'
                }
            )
    elif len(value) == 14:
        cnpj = CNPJ()
        try:
            assert cnpj.validate(value)
        except AssertionError:
            raise ValidationError(
                {
                    'erro': 'Documento inválido!'
                }
            )
    else:
        raise ValidationError(
            {
                'erro': 'Documento inválido!'
            }
        )

    return value
