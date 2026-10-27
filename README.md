# Full-stack Codex Template

Business-neutral repository skeleton extracted from an existing production-oriented full-stack project.

## Stack

- Frontend: Next.js 15, React 19, TypeScript, plain CSS, Docker.
- Backend: Python 3.12, Django 5.2, Django REST Framework, PostgreSQL, Redis, Celery, Gunicorn, Docker.
- Agent guidance: scoped `AGENTS.md` files plus reusable skills under `.agents/skills/`.

This template intentionally contains no product/domain rules. Add Django domain apps under `backend/apps/<domain>/` and frontend features under the existing App Router structure.

## Development

Backend:

```bash
cd backend
docker compose up --build
```

Frontend:

```bash
cd frontend
npm ci
npm run dev
```

Default URLs: frontend `http://localhost:3000`, backend `http://localhost:8000`.

## Note for GIT
* Please help apply GitFlow for this repository (https://danielkummer.github.io/git-flow-cheatsheet).
* Example:
  * Name for any features -> `feature/xxx-yyy`. Ex: `feature/implement-login-ui`
  * Name for any bugs -> `bugfix/xxx-yyy`. Ex: `bugfix/wrong-message-when-login`

* When creating a title for a pull request or a commit message, please ensure that both the title and message are meaningful, and include a description if necessary. Capitalize the first letter and avoid using special characters.
* Example:
  * Implement the authentication feature

## Author
* Name: Tuan Le
* Email: latuan.dev@gmail.com
