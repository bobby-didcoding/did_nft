# DID_NFT

Hi there.
This project will enable you to create NFT's using Python and Django

### Local Development Setup
1. Clone this repo `git clone --branch full-code git@github.com:bobby-didcoding/did_nft.git`

### Install Redis for Celery
1. Install 'Ubuntu' and set up Redis (https://www.youtube.com/watch?v=_nFwPTHOMIY)
2. Download `Ubunto` from `windows store` and launch app
3. create a username (must be an email) & password
4. Now create redis repository `sudo apt-add-repository ppa:redislabs/redis`
5. Now update and upgrade packages `sudo apt-get update` then `sudo apt-get upgrade`
6. Now install Redis `sudo apt-get install redis-server`
### Config
7. Create a `.env` file from the `.env.template` and fill-in the environment variables specific to your setup (eg. DB
   name, user and password)
8. Set up a virtual environment `python -m venv env`
9. Activate virtual environment `cd env/scripts && activate && cd ../..`
10. Install dependencies for your local environment by running `pip install -r requirements.txt`
11. Run `python manage.py migrate`
11. Run `python manage.py collectstatic`

### Fire up servers
12. Open Ubuntu terminal and fire up a Redis server `redis-server`
13. Open another Ubuntu and set up a Redis CLI `redis-cli`
14. Open new cmd in root and use this command `celery -A nft.celery worker --pool=solo -l info` to fire up a celery worker
15. Run `python manage.py runserver`

### Production Setup with Docker
1. Follow tutorial at https://didcoding.com/tutorial/create-nfts-using-django/
