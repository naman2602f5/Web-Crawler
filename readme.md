# Web Crawler

### Designed and implemented a web crawler whose primary task is to discover and list all product URLs across multiple e-commerce websites.
 
- move to project directory


- change different .env variables in .env as per your choice.


- Install python3
- install venv for your 3.X.* version 
    ```sh
      sudo apt install python3.<X>-venv
    ```
- Create a local environment
    ```sh
      python3 -m venv env`
    ```

- Activate your environment 
    ```sh
        source env/bin/activate
    ```

- Install application dependencies : 
    ```sh
    pip install -r requirements.txt
    ```


# Redis Set-up using Docker
- Install docker 
  ```sh
    sudo apt install docker
    ```
  
- Provide permission to root user in docker using command
    ```sh
        sudo chmod 777 /var/run/docker.sock
    ```
  
- Run the following commands to run redis container
    ```sh
        docker-compose up -d --build
    ```
  
# Start the application

- Run the application using command
    ```sh
        flask run
    ```
  
- Run the celery worker in another terminal using command
    ```sh
        celery -A main.celery worker --loglevel=info
    ```
  
- After the application start browse to this API URL `http://localhost:5000/api/v1/crawl`


- For Swagger API documentation browse to `http://localhost:5000/webCrawler/doc`


- Sample request for the API:
    `{
         "domains": ["goosegreaseshop.com", "books.toscrape.com", "www.cratejoy.com"]
    }`


- For more domains for testing, refer to `DomainUrlList.txt`