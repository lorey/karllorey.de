.RECIPEPREFIX = >

.PHONY: all build open

all: clean build open

build:
> nikola build

open:
> xdg-open output/index.html

clean:
> rm -rf output
> rm -rf cache
> rm -rf .doit.db.db