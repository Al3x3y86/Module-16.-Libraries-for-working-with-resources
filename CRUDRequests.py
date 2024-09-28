from fastapi import FastAPI, Path, HTTPException

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
def get_users():
    return users


@app.post("/user/{username}/{age}")
def add_user(
    username: str = Path(..., min_length=3, max_length=50, description="Имя пользователя, минимум 3 и максимум 50 символов"),
    age: int = Path(..., ge=1, le=120, description="Возраст пользователя, от 1 до 120")
):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} is registered"}


@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: str = Path(..., description="ID пользователя"),
    username: str = Path(..., min_length=3, max_length=50, description="Имя пользователя, минимум 3 и максимум 50 символов"),
    age: int = Path(..., ge=1, le=120, description="Возраст пользователя, от 1 до 120")
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} has been updated"}


@app.delete("/user/{user_id}")
def delete_user(user_id: str = Path(..., description="ID пользователя")):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}
