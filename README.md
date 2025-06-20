# 📚 BookPedia – Online Bookstore

**BookPedia** is a professional-grade online bookstore built with the Django framework. It allows users to browse, search, purchase, and review books with a secure and modern e-commerce experience. Designed for learning and showcasing full-stack Django development.

---

## 🚀 Features(Till now)

- A Full Functionable online store
- Individual book detail pages with review feature
- Custom user authentication system
- Django admin panel customization

---

## 🛠️ Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** PostgreSQL  
- **Payments:**  
- **Version Control:** Git + GitHub  
- **Deployment:**  

---

## Project Structure  
```
bookpedia/ 
├── accounts/           # Custom user model & authentication 
├── books/              # Book & review models, views, templates 
├── pages/              # Static pages like Home, About 
├── templates/          # Global and app-specific templates 
├── static/             # Static files (CSS, JS) 
├── manage.py 
├── requirements.txt 
├── docker-compose.yml 
└── .env                # Environment variables 
 ```


## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/bookpedia.git
cd bookpedia
```
### 2. Create .env File
Create a .env file at the root with environment variables like:
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
API=your-api-key
```

### 3. Run with Docker (Recommended)
```
docker-compose up --build
```

### 4. Apply Migrations
```
docker-compose exec web python manage.py migrate
```
### 5. Create Superuser
```
docker-compose exec web python manage.py createsuperuser
```
### 6. Access the App

App: http://127.0.0.1:8000

Admin: http://127.0.0.1:8000/admin

### 🧪 Testing
```
docker-compose exec web python manage.py test
```


📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

🙋‍♂️ Author
Mahfuz Hossain
Backend Developer | Django Enthusiast
