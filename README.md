# Zenith Vault

Zenith Vault is a SaaS application built with Django for the backend. It allows users to manage books, papers, and other internet text content, track reading progress, provide translation and note-taking features, and share libraries and contents with other users.

## Features

 - User Authentication and Profile Management
 - Content Management (CRUD operations for books, papers, and internet text content)
 - Library Management (Create and manage libraries of contents)
 - Reading Progress Tracking
 - Translation and Note-Taking
 - Content Sharing

## Project Structure

 - `backend/` - The Django backend

## Prerequisites

 - Python 3.x
 - PostgreSQL

## Installation

### Backend

 1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/zenith-vault.git
    cd zenith-vault/backend
    ```

 2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

 3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

 4. **Set up PostgreSQL database:**
    Create a PostgreSQL database and user, and update the `DATABASES` setting in `zenithvault_backend/settings.py` with your database credentials.

 5. **Run database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

 6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

 7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

 The following endpoints are available in the API:

 - **Authentication and User Management:**
   - `/api/auth/login/` - Login
   - `/api/auth/logout/` - Logout
   - `/api/auth/registration/` - Registration
   - `/api/auth/password/reset/` - Password reset
   - `/api/auth/password/change/` - Password change

 - **User Profiles:**
   - `/api/users/profiles/` - User profiles

 - **Content Management:**
   - `/api/contents/` - CRUD operations for contents

 - **Library Management:**
   - `/api/users/libraries/` - Create and manage libraries
   - `/api/users/library-contents/` - Manage library contents
   - `/api/users/shared-contents/` - Manage shared contents

### Running Tests

 To run the tests, use the following command:

 ```bash
 python manage.py test
 ```

### Settings

 The primary settings are located in `zenithvault_backend/settings.py`. Adjust these settings according to your development and production environments.

## Contributing

 Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

 This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

 For questions or feedback, please open an issue in the repository or contact the project maintainer.
