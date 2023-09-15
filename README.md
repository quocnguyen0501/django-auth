# BASIC AUTHENTICATION DJANGO

- python3
- django

## Feature:

- OAuth (Google Auth)
- Mail Verification

## Script

1. Start docker:
    ```bash
   cd cotainer/ && docker-compose up -d
    ```
   
2. Install and Migrate:
   ```
   make install && make migrate
   ```
   
3. Start app:
   ```bash
   make run
   ```
   
#### Note

- Add credential of email and information on google cloud console (client_id and secret_key) before start app.