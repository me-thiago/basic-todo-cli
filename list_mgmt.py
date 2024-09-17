lists = ["main"]


def create_list(name):
    lists.append(name)
    print(f'new list created: \n name: {name} \n position: {len(lists)}')

def delete_list(pos):
    print(f'deleting list {lists[int(pos)]} from the database. \n Now you have {len(lists)} lists available')

def view_lists():
    i = 0
    if len(lists)==0:
        print("no list available")
        return

    print(f'there are {len(lists)} lists:')
    for list in lists:
        print(f"  {i}. ({list.priority}): {list.description}")
        i = i+1

