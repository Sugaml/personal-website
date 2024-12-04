build:
	docker build --platform linux/amd64  -t sugamdocker35/website:v3 .

run:
	docker run -d --name site -p 80:80 sugamdocker35/website:v3