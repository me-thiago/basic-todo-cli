

tags_keypair = [
                {"name": "Moon", "value": "moon"},
                {"name": "Dio", "value": "dio"},
                {"name": "Personal", "value": "personal"},
                {"name": "Gin", "value": "gin"}
            ]


tags = ["moon", "dio", "personal", "gin"]

status = ['not started', 'on going', 'completed']
priority = ['high', 'medium', 'low']

priority_keypair = [
                {"name": "High", "value": "high"},
                {"name": "Medium", "value": "medium"},
                {"name": "Low", "value": "low"}
            ]

def new_tag(name, value):
    tags_keypair.append({name, value})
    tags.append(value)
    print(f'new tag added: {name}. Total tags: {len(tags_keypair)}')

projects = ["tasks"]