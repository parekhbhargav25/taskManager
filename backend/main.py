from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
taskidCounter = 1
tasks = [ ]

class Task(BaseModel):
    id: int
    title: str
    completed: bool=False  

@app.get("/")
def root ():
    return {"Message: Backend is running"}

@app.get("/health")
def healthCheck():
    return {"status" : "ok"}

@app.post("/tasks")
def createTask(task: Task):
    global taskidCounter
    task.id = taskidCounter
    taskidCounter +=1
    
    tasks.append(task)
    return task

@app.get("/tasks")
def getAllTasks():
    return tasks


@app.put("/tasks/{task_id}")
def updateTask (task_id: int, updatedTask: Task ):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updatedTask
            return updatedTask
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def deleteTask (task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "task deleted"}
    return {"error": "task not found"}

        
    

    