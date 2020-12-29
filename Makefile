install:
	poetry install

reinstall:
	poetry --force-reinstall

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl
