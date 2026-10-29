from datetime import date

assignment1 = {
    "duedate": date(2026, 10, 1),
    "class": "maths",
    "topic": "sets",
    "priority": "high"
}
assignment2 = {
    "duedate": date(2026, 10, 5),
    "class": "programming",
    "topic": "loops",
    "priority": "medium"
}
assignment3 = {
    "duedate": date(2026, 10, 25),
    "class": "maths",
    "topic": "functions",
    "priority": "low"
}

tasks = [assignment1, assignment2, assignment3]

def show_tasks(tasks):
    for task in tasks:
        print(f"Class: {task['class']}, Topic: {task['topic']}, Due Date: {task['duedate']}, Priority: {task['priority']}")

def add_task(tasks, duedate, class_name, topic, priority):
    new_task = {
        "duedate": duedate,
        "class": class_name,
        "topic": topic,
        "priority": priority

    }
    tasks.append(new_task)
    

show_tasks(tasks)
add_task(tasks, date(2026, 10, 15), "computing","algorithms", "high")
show_tasks(tasks)

