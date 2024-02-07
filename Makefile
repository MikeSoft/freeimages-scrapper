buildandrun:
	docker-compose down -v
	docker-compose up -d --build --force-recreate --no-deps

run:
	docker-compose up -d

build:
	docker-compose build --force-rm --no-cache

down:
	docker-compose down

restart:
	docker-compose restart

createadmin:
	docker-compose run web python manage.py createsuperuser --username admin --email admin@admin.com

test:
	docker-compose run web python manage.py test

list-services:
	@echo "Services using build:"
	@yq e '.services | to_entries | .[] | select(.value.build) | .key' docker-compose.yml
	@echo "\nServices using image:"
	@yq e '.services | to_entries | .[] | select(.value.image) | .key' docker-compose.yml

list-build-services-prefixed:
	@dir=$$(basename "$$(pwd)") && \
	echo "Services built with directory prefix:" && \
	yq e '.services | to_entries | .[] | select(.value.build) | .key' docker-compose.yml | xargs -I {} echo $$dir"_"{}
