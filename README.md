# w

Backend API for w

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Designpythonworldclockui.git))

## Project Structure

```
w/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration
- User login
- User profile management
- Password reset
- Data CRUD operations

## API Endpoints

- `POST /api/register` - Create a new user account.
- `POST /api/login` - Log in to an existing user account.
- `PUT /api/profile` - Update a user's profile information.
- `POST /api/password_reset` - Reset a user's password.
- `GET /api/data` - Get all data.
- `POST /api/data` - Create new data.
- `GET /api/data/{id}` - Get data by id.
- `PUT /api/data/{id}` - Update data by id.
- `DELETE /api/data/{id}` - Delete data by id.

## License

MIT
