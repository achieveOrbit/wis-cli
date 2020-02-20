
make:
	pyinstaller --clean wis.spec

clean:
	rm -Rf __pycache__ build dist
	rm -Rf src/__pycache__
	rm src/*.pyc
	rm profiling_data

profile:
	python3 -m cProfile -o profiling_data wis.py terminy
	snakeviz profiling_data
