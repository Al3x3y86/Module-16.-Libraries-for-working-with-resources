from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Список пользователей
users = []


# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int


# GET запрос для получения всех пользователей
@app.get("/users")
def get_users():
    return users


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
def add_user(username: str, age: int):
    user_id = 1 if not users else users[-1].id + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


# PUT запрос для обновления пользователя
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
