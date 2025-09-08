from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str


users_db: dict[int, dict] = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
}


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user:
        return user
    return {"error": "User not found"}


@app.get("/users", response_model=list[User])
def list_users():
    return list(users_db.values())


@app.post("/users", response_model=User)
def create_user(user: User):
    users_db[user.id] = user.dict()
    return user
