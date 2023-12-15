def get_template_type():
    while True:
        template_type = input("Choose the template type ('school' or 'work'): ").lower()
        if template_type in ['school', 'work']:
            return template_type
        print("Invalid input. Please enter 'school' or 'work'.")

def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_user_input():
    entity_name = input("Enter the entity name: ")
    # Add more inputs for properties if needed
    return entity_name

def get_entity_properties():
    properties = []
    while True:
        prop_name = input("Enter property name (or just hit enter to finish): ")
        if not prop_name:
            break
        prop_type = input(f"Enter type for '{prop_name}': ")
        properties.append((prop_name, prop_type))
    return properties

def create_file_from_template(entity_name, template_type, file_type, output_path):
    entity_name_lower = entity_name.lower()
    folder_name = 'aspnet_personnal_api' if template_type == 'school' else 'aspnet_recyos_api'
    template_path = f"{folder_name}/{file_type}_template.txt"
    template = read_template(template_path)
    content = template.replace("[EntityName]", entity_name)
    content = template.replace("[EntityNameLower]", entity_name_lower)
    with open(output_path, 'w') as file:
        file.write(content)

def main():
    template_type = get_template_type()
    entity_name = get_user_input()
    properties = get_entity_properties()

    create_file_from_template(entity_name, template_type, "repository", f"Repositories/Implementation/{entity_name}Repository.cs")
    create_file_from_template(entity_name, template_type, "repository_interface", f"Repositories/Interface/I{entity_name}Repository.cs")
    create_file_from_template(entity_name, template_type, "service", f"Services/Implementation/{entity_name}Service.cs")
    create_file_from_template(entity_name, template_type, "service_interface", f"Services/Interface/I{entity_name}Service.cs")
    create_file_from_template(entity_name, template_type, "controller", f"Controllers/{entity_name}Controller.cs")


if __name__ == "__main__":
    main()