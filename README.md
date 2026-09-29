# ShopNest Backend

ShopNest is a scalable e-commerce backend built with **Python, FastAPI, Strawberry GraphQL, and PostgreSQL**.

The project is designed with a layered architecture that separates GraphQL API handling, business logic, and database access. It is being developed with production-oriented practices such as repository/service separation, input validation, logging, error handling, pagination, and automated testing.

---

## 🚀 Project Overview

ShopNest provides backend services for an e-commerce platform, including:

- Product catalog management
- Product search
- Category and subcategory filtering
- Product sorting
- Pagination
- Inventory information
- GraphQL API
- Repository/service architecture
- Automated product repository tests
- Logging and error handling

Upcoming modules include authentication, customers, shopping cart, orders, and administration.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Backend programming language |
| FastAPI | Web framework |
| Strawberry GraphQL | GraphQL API |
| PostgreSQL | Relational database |
| psycopg2 | PostgreSQL database connectivity |
| Uvicorn | ASGI server |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source control and collaboration |

---

## 🏗️ Architecture

ShopNest follows a layered backend architecture:

```text
Client
   │
   ▼
GraphQL API
   │
   ▼
FastAPI
   │
   ▼
GraphQL Resolver Layer
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
PostgreSQL
