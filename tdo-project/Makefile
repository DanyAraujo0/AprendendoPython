run:
	poetry run uvicorn store.main:app --reload

test: 
	poetry run pytest

test-matching:
	poetry run pytest -s -rx -k ${K} --pdb store ./tests/ 
	# $ variavel onde faz o teste exemplo o nome da funcao