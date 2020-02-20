
profile:
	python3 -m cProfile -o profiling_data wis.py terminy
	snakeviz profiling_data