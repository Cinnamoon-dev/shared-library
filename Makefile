build:
	g++ -shared -FPIC -o lib.so lib.cpp

runc: build
	export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
	g++ -o main main.cpp -L. -llib
	./main

runpy:
	python3 code1.py