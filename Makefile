.PHONY: build serve docker-build docker-run extract

# Assemble blog pages from content + templates
build:
	python3 scripts/build_site.py

# Split existing blogs/ into content/ + data/ (migration helper)
extract:
	python3 scripts/extract_blog_content.py
	python3 scripts/build_site.py

# Local preview (requires Python 3)
serve:
	python3 -m http.server 8080

docker-build:
	docker build --platform linux/amd64 -t sugamdocker35/website:v3 .

docker-run:
	docker run -d --name site -p 80:80 sugamdocker35/website:v3

# Legacy aliases
run: docker-run
