make lint:
	flake8 --exclude=*/migrations/*,*/views/*,./pontos_turisticos/* --exit-zero