from fastapi import FastAPI

app = FastAPI()

# Изначальный словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}


# GET запрос для получения всех пользователей
@app.get("/users")
def get_users():
    return users


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
def add_user(username: str, age: int):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} is registered"}


# PUT запрос для обновления пользователя
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        return {"message": "User not found"}, 404
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} has been updated"}


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id not in users:
        return {"message": "User not found"}, 404
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}
