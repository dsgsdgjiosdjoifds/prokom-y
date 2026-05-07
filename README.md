# Y

Social media backend REST API built with Django REST Framework.
Handles authentication, user profiles, posts, comments, likes, and follows.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` and fill in your credentials:

```bash
cp src/.env.example src/.env
```

Run migrations and start the server:

```bash
python3 src/manage.py migrate
python3 src/manage.py runserver
```

## API Documentation

Interactive docs are available once the server is running:

| URL       | Description                               |
| --------- | ----------------------------------------- |
| `/docs`   | Swagger UI: browse and test all endpoints |
| `/redoc`  | ReDoc: clean read-only reference          |
| `/schema` | Raw OpenAPI 3.0 schema (YAML)             |

All protected endpoints require a `Bearer` JWT token in the `Authorization` header.

## Endpoints

### Auth

| Method | Path             | Auth | Description                        |
| ------ | ---------------- | ---- | ---------------------------------- |
| POST   | `/auth/register` | -    | Register a new user                |
| POST   | `/auth/login`    | -    | Obtain access + refresh token pair |
| POST   | `/auth/refresh`  | -    | Refresh access token               |

### Accounts

| Method | Path                                   | Auth     | Description                 |
| ------ | -------------------------------------- | -------- | --------------------------- |
| GET    | `/accounts/profile`                    | Required | Get own profile             |
| PATCH  | `/accounts/profile`                    | Required | Update own profile          |
| GET    | `/accounts/users/search?q=`            | Required | Search users by username    |
| GET    | `/accounts/users/{username}`           | -        | Get a user's public profile |
| GET    | `/accounts/users/{username}/followers` | Required | List a user's followers     |
| GET    | `/accounts/users/{username}/following` | Required | List who a user follows     |
| POST   | `/accounts/users/{username}/follow`    | Required | Follow a user               |
| DELETE | `/accounts/users/{username}/follow`    | Required | Unfollow a user             |

### Posts

| Method | Path                               | Auth     | Description                    |
| ------ | ---------------------------------- | -------- | ------------------------------ |
| GET    | `/posts`                           | Required | List all posts (paginated)     |
| POST   | `/posts`                           | Required | Create a post                  |
| GET    | `/posts/feed`                      | Required | Posts from followed users      |
| GET    | `/posts/search?q=`                 | Required | Search posts by content        |
| GET    | `/posts/{id}`                      | Required | Get a post                     |
| PATCH  | `/posts/{id}`                      | Required | Update a post (author only)    |
| DELETE | `/posts/{id}`                      | Required | Delete a post (author only)    |
| POST   | `/posts/{id}/like`                 | Required | Like a post                    |
| DELETE | `/posts/{id}/like`                 | Required | Unlike a post                  |
| GET    | `/posts/{id}/comments`             | Required | List comments on a post        |
| POST   | `/posts/{id}/comments`             | Required | Add a comment                  |
| GET    | `/posts/{id}/comments/{commentId}` | Required | Get a comment                  |
| PATCH  | `/posts/{id}/comments/{commentId}` | Required | Update a comment (author only) |
| DELETE | `/posts/{id}/comments/{commentId}` | Required | Delete a comment (author only) |

## License

Project is licensed under MIT license. See more in [LICENSE](LICENSE) file.
