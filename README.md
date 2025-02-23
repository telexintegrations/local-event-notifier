## Local  Event Notifier
Local  Event Notifier built using FastAPI  Docker for containerization, Poetry for dependency management, and a Makefile for task automation.

### Features
- Fetches events based on city, and category.
- Docker for easy containerization and deployment.
- Poetry for managing dependencies and packaging.
- Pre-commit hooks for enforcing code quality and consistency before committing code.
- Sends events to Telex.

### Prerequisites
Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/)
- [Poetry ](https://python-poetry.org/)
- [Make](https://makefiletutorial.com/)
- [Pre-commit](https://pre-commit.com/)(for managing hooks)
- [Pytest](https://docs.pytest.org/en/stable/)- Testing framework


### Getting Started Installation & Local setup
Clone the repository
 ```shell
 git clone https://github.com/telexintegrations/local-event-notifier

 cd local-event-notifier
 ```
Create and activate a virtual environment: [install pyenv](https://github.com/pyenv/pyenv#installation)

#### Alternatively, using Python's built-in venv:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Set up dependencies with Poetry
Poetry is used for managing the Python dependencies. You can install them with:
 ```shell
 poetry install
 ```

### Install pre-commit hooks
Pre-commit hooks help enforce code quality before committing changes.
To install and configure pre-commit hooks:
1. Install pre-commit globally:
 ```shell
pip install pre-commit
 ```
2. Install the pre-commit hooks:
 ```shell
 pre-commit install
 ```
3. Run all hooks on all files (initial check):
 ```shell
 pre-commit run --all-files
 ```
#####  Pre-commit Hooks Overview
The following pre-commit hooks are configured for this project to ensure code quality:
- Code Style: Automatically formats code using black, sorts imports with isort, and checks for PEP 8 compliance with flake8.
- Code Quality: Verifies that docstrings are present, removes trailing whitespace, checks for correct Python syntax, and ensures logging is used correctly.
- Configuration Validation: Checks the correctness of TOML and YAML files, and ensures the Poetry configuration is set up properly.
5. Install project  Dependencies
```shell
poetry install
 ```
6. Run the Application
```shell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
## �� Documentation

## Endpoints

- **URL**: `api/integration.json`
- **Method**: `GET`
- **Body**: No body but a QUERY in form of an integer should be passed
- **Response**:
  ```json
    
    {
    "data": {
        "date": {
            "created_at": "2025-02-19",
            "updated_at": "2025-02-19"
        },
        "descriptions": {
            "app_description": "Fetches local events based on chosen city or location and posts updates on the Telex channel",
            "app_logo": "https://my-portfolio-343207.web.app/MyLogo2.png",
            "app_name": "Local event Notifier",
            "app_url": "https://local-event-notifier.onrender.com/api/integration.json",
            "background_color": "#fff"
        },
        "integration_category": "Monitoring & Logging",
        "integration_type": "interval",
        "is_active": true,
        "key_features": [
            "Fetches events based on city, and category.",
            "Sends events to Telex.",
            "Notifys users of events.",
            "post events at intervals."
        ],
        "settings": [
            {
                "label": "interval",
                "type": "text",
                "required": true,
                "default": "0 * * * *"
            },
            {
                "label": "city",
                "type": "text",
                "required": true,
                "default": "Berlin"
            },
            {
                "label": "limit",
                "type": "text",
                "required": true,
                "default": "10"
            },
            {
                "label": "category",
                "type": "dropdown",
                "required": true,
                "default": "Music",
                "options": [
                    "Music",
                    "Arts",
                    "Sports",
                    "Food",
                    "Business",
                    "Tech",
                    "Health",
                    "Science",
                    "Education",
                    "Fashion",
                    "Film",
                    "Literature",
                    "Religion",
                    "Politics",
                    "Charity",
                    "Community",
                    "Family",
                    "Holiday",
                    "Other"
                ]
            }
        ],
        "tick_url": "https://local-event-notifier.onrender.com/api/tick",
        "target_url": "https://ping.telex.im/v1/webhooks/01951fa7-6d0e-753d-ba67-e9ea376bcce4"
    }

    }
  ```
- **URL**: `api/tick` 
- **Method**: `POST`
- **Body**:
```json
{
  "channel_id": "string",
  "return_url": "string",
  "settings": [
    {
      "label": "city",
      "type": "string",
      "required": true,
      "default": "Berlin"
    },
 {
      "label": "category",
      "type": "string",
      "required": true,
      "default": "Music"
    },
 {
      "label": "limit",
      "type": "string",
      "required": true,
      "default": "10"
    }
  ]
}
```
- **Response**:
  ```json
   {
    "message": "[{'title': 'Cage The Elephant - Europe 2025', 'url': 'https://www.ticketmaster.de/event/cage-the-elephant-europe-2025-tickets/1476430159?language=en-us', 'start_time': '2025-02-21', 'venue': 'TBA'}, {'title': 'Gracie Abrams: The Secret of Us Tour', 'url': 'https://www.ticketmaster.de/event/gracie-abrams-the-secret-of-us-tour-tickets/548575?language=en-us', 'start_time': '2025-02-22', 'venue': 'TBA'}, {'title': 'Gracie Abrams: The Secret of Us Tour | VIP Packages', 'url': 'https://www.ticketmaster.de/event/gracie-abrams-the-secret-of-us-tour-%7C-vip-packages-tickets/548693?language=en-us', 'start_time': '2025-02-22', 'venue': 'TBA'}, {'title': 'Teddy Swims - I’ve Tried Everything But Therapy Tour', 'url': 'https://www.ticketmaster.de/event/teddy-swims-ive-tried-everything-but-therapy-tour-tickets/552817?language=en-us', 'start_time': '2025-02-23', 'venue': 'TBA'}, {'title': \"Teddy Swims: I've Tried Everything But Therapy | VIP Tour Package\", 'url': 'https://www.ticketmaster.de/event/teddy-swims-ive-tried-everything-but-therapy-%7C-vip-tour-package-tickets/552893?language=en-us', 'start_time': '2025-02-23', 'venue': 'TBA'}, {'title': 'Lexa Gates - The Elite Vessel Tour', 'url': 'https://www.ticketmaster.de/event/lexa-gates-the-elite-vessel-tour-tickets/555771?language=en-us', 'start_time': '2025-02-23', 'venue': 'TBA'}, {'title': 'Oscar and the Wolf', 'url': 'https://www.ticketmaster.de/event/oscar-and-the-wolf-tickets/553845?language=en-us', 'start_time': '2025-02-23', 'venue': 'TBA'}, {'title': 'Oscar and the Wolf | Merch Upgrade (no Ticket)', 'url': 'https://www.ticketmaster.de/event/oscar-and-the-wolf-%7C-merch-upgrade-no-ticket--tickets/553871?language=en-us', 'start_time': '2025-02-23', 'venue': 'TBA'}, {'title': 'ericdoa - europe tour 2025', 'url': 'https://www.ticketmaster.de/event/ericdoa-europe-tour-2025-tickets/845240353?language=en-us', 'start_time': '2025-02-23', 'venue': 'TBA'}, {'title': 'Franz Ferdinand - UK / European Tour 2025', 'url': 'https://www.ticketmaster.de/event/franz-ferdinand-uk-european-tour-2025-tickets/552335?language=en-us', 'start_time': '2025-02-24', 'venue': 'TBA'}]",
    "username": "Local Notifier",
    "event_name": "Notifier Event",
    "status": "success"
   }
  ```
  **Response2**: On  the telex  UI, the response look like:
  ![alt text](<Screenshot 2025-02-21 at 17.13.42.png>)

## Tests
To run  unit tests locally
```shell
pytest
```
