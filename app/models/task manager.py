import json
import os
from datetime import datetime, timedelta
from plyer import notification

TASKS_FILE = 'tasks.json'
STATUSES = ['čekající', 'dokončený', 'neúspěšný']

def send_desktop_notifications(tasks):
    today = datetime.today().date()
    today_tasks = []
    overdue_tasks = []

    for task in tasks:
        deadline_str = task.get('deadline', '')
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            if deadline == today:
                today_tasks.append(task)
            elif deadline < today:
                overdue_tasks.append(task)
        except ValueError:
            continue

    if today_tasks:
        notification.notify(
            title="Úkoly pro dnešek",
            message=f"Máš {len(today_tasks)} úkol(ů), které mají termín dnes.",
            timeout=10
        )

    if overdue_tasks:
        notification.notify(
            title="Zmeškané úkoly",
            message=f"{len(overdue_tasks)} úkol(ů) je po termínu!",
            timeout=10
        )

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def generate_id(tasks):
    if tasks:
        return max(task['id'] for task in tasks) + 1
    return 1


def create_task(tasks):
    title = input("Zadej název úkolu: ")
    deadline = input("Zadej termín splnění (YYYY-MM-DD): ")
    new_task = {
        'id': generate_id(tasks),
        'title': title,
        'status': 'čekající',
        'deadline': deadline
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Úkol byl přidán.")



def list_tasks(tasks):
    if not tasks:
        print("Žádné úkoly.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['title']} – {task['status']} – termín: {task.get('deadline', 'neuveden')}")


def update_task(tasks):
    task_id = int(input("Zadej ID úkolu k úpravě: "))
    for task in tasks:
        if task['id'] == task_id:
            new_title = input("Zadej nový název úkolu: ")
            new_deadline = input("Zadej nový termín (YYYY-MM-DD): ")
            task['title'] = new_title
            task['deadline'] = new_deadline
            save_tasks(tasks)
            print("Úkol byl upraven.")
            return
    print("Úkol s tímto ID nebyl nalezen.")



def delete_task(tasks):
    task_id = int(input("Zadej ID úkolu ke smazání: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("🗑️ Úkol byl smazán.")
            return
    print("Úkol s tímto ID nebyl nalezen.")


def change_status(tasks):
    task_id = int(input("Zadej ID úkolu ke změně stavu: "))
    for task in tasks:
        if task['id'] == task_id:
            print("Vyber nový stav:")
            for i, status in enumerate(STATUSES, start=1):
                print(f"{i}. {status}")
            choice = int(input("Volba: "))
            if 1 <= choice <= len(STATUSES):
                task['status'] = STATUSES[choice - 1]
                save_tasks(tasks)
                print("Stav úkolu byl změněn.")
            else:
                print("Neplatná volba.")
            return
    print("Úkol s tímto ID nebyl nalezen.")

def list_upcoming_tasks(tasks):
    today = datetime.today().date()
    threshold = today + timedelta(days=7)
    found = False

    print("Úkoly s termínem do 7 dnů:\n")
    for task in tasks:
        deadline_str = task.get('deadline', '')
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            if today <= deadline <= threshold:
                print(f"[{task['id']}] {task['title']} – {task['status']} – termín: {deadline}")
                found = True
        except ValueError:
            continue  # pokud není platné datum, přeskočíme

    if not found:
        print("Žádné blížící se úkoly.")


def menu():
    tasks = load_tasks()
    send_desktop_notifications(tasks)  
    show_notifications(tasks) 
    while True:
        print("\n Správce úkolů")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Upravit úkol")
        print("4. Smazat úkol")
        print("5. Změnit stav úkolu")
        print("6. Zobrazit úkoly s blízkým termínem")
        print("7. Konec")


        choice = input("Zadej volbu: ")

        if choice == '1':
            create_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            change_status(tasks)
        elif choice == '6':
            list_upcoming_tasks(tasks)
        elif choice == '7':
            print("Ukončuji program.")
            break


if __name__ == "__main__":
    menu()

