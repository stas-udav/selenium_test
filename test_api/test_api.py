#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
import time
import json
import pytest
import requests
import uuid

endpoint = "https://todo.pixegami.io/"

def create_task(payload):
    return requests.put(endpoint + "create-task", json=payload)

def update_task(payload):
    return requests.put(endpoint + "update-task", json=payload)

def get_task(task_id):
      return requests.get(endpoint + f"get-task/{task_id}")

def list_task(user_id):
    return requests.get(endpoint + f"list-tasks/{user_id}")  
def delete_task(task_id):
    return requests.delete(endpoint + f"delete-task/{task_id}")

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
        }

def test_get_endpoint():
    response_get = requests.get(endpoint)    
    endpoint_data = response_get.json()
    assert response_get.status_code == 200
    # print(endpoint_data)
    # print(response_get)

def test_create_task():
    payload = new_task_payload()
    create_task_response =  create_task(payload)   
    create_task_data = create_task_response.json()
    assert create_task_response.status_code == 200
    # print(create_task_data)
    # print(create_task_response)

    task_id = create_task_data["task"]["task_id"]
    get_create_task_response = get_task(task_id)
    assert get_create_task_response.status_code == 200
    get_task_data = get_create_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
    # print(get_task_data)
    # print(get_create_task_response)

def test_update_task():
    # first creating task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # updating task
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "New task",              
        "is_done": True
        }
    
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

def test_can_list_tasks():
    n = 3
    payload = new_task_payload()
    for _ in range(n):        
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # list task, check that N items is there
    user_id = payload["user_id"]
    list_task_response = list_task(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()
    tasks = data["tasks"]
    assert len(tasks) == 3

def test_can_delete_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200    
    task_id = create_task_response.json()["task"]["task_id"]
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # Get task and check if it not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
    
    

