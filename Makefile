.PHONY: all run

run: all
	node testg.js

all: graphs.js testg.js

%.js: %.ls
	lsc -dc $^

