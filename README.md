# Y

Social media backend REST API built with Django. Handles users, posts, likes, comments, and follows.

Contains:

- Django REST framework
- JWT auth
- PostgreSQL

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Copy `.env` and fill in your credentials:

```bash
cp src/.env.example src/.env
```

```bash
python3 src/manage.py makemigrations accounts posts
python3 src/manage.py migrate
python3 src/manage.py runserver
```

## API

All endpoints are prefixed with `/api/`. Authentication uses `Bearer <token>` headers.

| Method               | Endpoint                    | Auth | Description               |
| -------------------- | --------------------------- | ---- | ------------------------- |
| POST                 | `/auth/login`               | No   | Login                     |
| POST                 | `/auth/register`            | No   | Register                  |
| POST                 | `/auth/refresh`             | No   | Refresh token             |
| GET / PATCH          | `/users/me`                 | Yes  | Own profile               |
| GET                  | `/users/<username>`         | Yes  | User profile              |
| POST / DELETE        | `/users/<username>/follow`  | Yes  | Follow / unfollow         |
| GET / POST           | `/posts`                    | Yes  | Global feed / create post |
| GET                  | `/posts/feed`               | Yes  | Following-only feed       |
| GET / PATCH / DELETE | `/posts/<id>`               | Yes  | Post detail               |
| POST / DELETE        | `/posts/<id>/like`          | Yes  | Like / unlike             |
| GET / POST           | `/posts/<id>/comments`      | Yes  | Comments                  |
| GET / PATCH / DELETE | `/posts/<id>/comments/<id>` | Yes  | Comment detail            |

## License

Yyyyy, yyyyyy. Yyyyy Yyyyyy [LICENSE](LICENSE) yyyy.
