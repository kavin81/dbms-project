# Password Manager – Tech Stack

| Layer       | Category         | Tool/Library       | Purpose              |
|-------------|------------------|--------------------|----------------------|
| **Frontend**| Framework        | `nextjs`           | React framework      |
|             | Store            | `zustand`          | State management     |
|             | Types            | `zod`              | Schema validation    |
|             | Styling          | `tailwind`         | Utility CSS          |
|             | UI Components    | `shadcn`           | UI kit               |
|             | Data Fetching    | `react-query`      | Caching/fetching     |
|             | HTTP Client      | `axios`            | API requests         |
| **Backend** | ORM              | `sqlmodel`         | DB models            |
|             | Migrations       | `alembic`          | DB migrations        |
|             | DB Driver        | `asyncmy`          | MySQL async driver   |
|             | API Framework    | `fastapi`          | API server           |
|             | ASGI Server      | `uvicorn`          | Runs FastAPI         |
|             | Form Parser      | `python-multipart` | File upload support  |
|             | Hashing          | `argon2-cffi`      | Password hashing     |
|             | Crypto           | `cryptography`     | Encryption utils     |
|             | Validation       | `pydantic[email]`  | Email checks         |
|             | Config           | `pydantic-settings`| Env settings         |
| **Database**| Engine           | `mysql`            | Primary DB           |
