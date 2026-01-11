# My Professional Portfolio (Django)

This repository contains my personal portfolio, showcasing my expertise as an **Odoo Python Developer** and **AI Researcher**.

## 🛠 Tech Stack
- **Python:** 3.12+
- **Framework:** Django
- **Deployment:** Static generation via django-distill
- **Special features:** Multi-language (Malagasy/French/English), NLP showcase

## 🚀 Getting Started

Follow these steps to set up the project locally:

### 1. Prerequisites
Ensure you have **Python 3.12** installed.

### 2. Environment Setup
Create a virtual environment to keep your dependencies organized:
```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
Install the main requirements and the specific libraries needed for image processing and static generation:
```bash
# Update pip
pip install --upgrade pip

# Install core requirements
pip install -r requirements.txt

# Install specific project tools
pip install Pillow
pip install django-distill
pip install python-decouple

```
