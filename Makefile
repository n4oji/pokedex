build: 
	docker-compose -f docker-compose.yml build
up:
	docker-compose -f docker-compose.yml up -d
stop:
	docker-compose -f docker-compose.yml stop
down:
	docker-compose -f docker-compose.yml down -v	
start:
	docker-compose -f docker-compose.yml start
migrations:
	docker exec -it web sh -c 'python3 manage.py makemigrations && python3 manage.py migrate'
bash:
	docker exec -it web sh