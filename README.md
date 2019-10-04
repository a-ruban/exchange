### Prerequisites
You need to have docker and docker-compose installed.
docker - https://linuxize.com/post/how-to-install-and-use-docker-on-ubuntu-18-04/

docker-compose - https://linuxize.com/post/how-to-install-and-use-docker-on-ubuntu-18-04/


## Running the application

```
docker-compose -f docker-dev-compose.yml up
```
## Converter endpoint
GET /convert/

![UI example](https://i.imgur.com/Vff7EUe.png)

POST /convert/

curl -d "currency_from=USD&currency_to=EUR&amount=5" http://127.0.0.1:8000/convert/

```
{"result": 0.16829196061782317}
```

# Running tests
docker-compose -f docker-dev-compose.yml run web python manage.py test



