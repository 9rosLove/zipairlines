# ✈️ ZipAirlines REST API

## 🔧 Installing using GitHub
1. Clone the repository from GitHub:
    ```bash
    git clone htthps://github.com/9rosLove/zipairlines.git
    cd zipairlines
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate a virtual enviroment:
    - For Windows🪟:
    ```bash
    .\venv\Scripts\activate
    ```
    - For Linux🐧 and MacOS🍏:
    ```bash
    source venv/bin/activate
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set the environment variables for bot configuration and secret key:
    
   - For Linux🐧 and MacOS🍏
   ```bash
    export DJANGO_SECRET_KEY=<your db hostname>
    export DJANGO_DEBUG=<True_or_False>
    ```
    - For Windows🪟
    ```shell
    set DJANGO_SECRET_KEY=<your db hostname>
    set DJANGO_DEBUG=<True_or_False>
                    ...
    ```


7. Migrate the database:
    ```bash
    pyahon manage.py makemigrations
    python manage.py migrate
    ```
8. Start the development server:
    ```bash
    python manage.py runserver
    ```
## 🐋 Run with docker
1. Make sure Docker is installed.
2. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```
##  Testing
1. Run tests with coverage:
    ```bash
    coverage run python manage.py test
    ```
2. Generate coverage report:
    ```bash
    coverage report
    ```
