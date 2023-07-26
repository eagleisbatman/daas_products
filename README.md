# DAAS Products (Development Agent Admistration System)

DAAS Products is a Django-based web application for managing records of Development Agents and their geographical assignments in Ethiopia. 

## Features

The following are the main features of DAAS Products:

**1. Django Admin Interface**

A user-friendly admin interface allows authorized users to create, update, delete, and browse records. The interface uses Django's built-in admin functionality, customized to fit the needs of the application.

**2. User Authentication**

Users must log in to access the application. Django's built-in authentication system is used to manage user accounts, password hashing, sessions, and other related features.

**3. Data Models and Database Integration (Implemented on July 20, 2023)**

Data models are defined for Development Agents, along with several related entities: Gender, Salutation, Marital Status, Education Level, Position, Region, Zone, Woreda, Kebele, and Development Groups. These models are integrated with a PostgreSQL database, allowing data to be stored, retrieved, and manipulated efficiently.

**4. Data Import and Export**

Using the Django Import-Export library, data can be imported and exported in various formats, including CSV, JSON, and Excel. This makes it easy to load initial data into the system, back up the data, or integrate with other systems.

**5. Data Initialization Script**

A script is provided to initialize the database with necessary data for Gender, Salutation, Marital Status, Education Level, and Position from a CSV file.

**6. Environment Configuration**

Sensitive configuration values, such as database credentials, are stored in an `.env` file, which is not included in version control. This helps to keep the configuration secure and flexible across different environments.
