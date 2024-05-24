# Vendor_app
## Setup and Installation
### Environment Setup
1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/vendor-management-system.git
   cd vendor-management-system
2. **Create a virtual environment**

    python -m venv venv
    Activate the virtual environment:
   ```bash
    On Windows:
      venv\Scripts\activate
    On macOS and Linux:
      source venv/bin/activate
3. **Installing Requirements**

    ```bash
    pip install -r requirements.txt

4. **Database Setup**

    ```bash
    python manage.py migrate
    python manage.py createsuperuser
5. **Running the Application**

     ```bash
     python manage.py runserver
     
     click http://127.0.0.1:8000/admin/
6. **API Documentation**

     ```bash
     http://127.0.0.1:8000/api/swagger/
7. **Authentication**

    1. Create a user if you haven't already:
       ```bash
       python manage.py createsuperuser
    2. Genrate token using (post)api/token endpoint.
    3. Set access token in Authorize.
    4. Then access any api you can.    
