play: .venv
	pipenv run python src/pysnake.py

.venv:
	pipenv install
