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

def properties_to_params(properties):
    return ', '.join([f"{prop_type} {prop_name}" for prop_name, prop_type in properties])

def extract_property_names(properties):
    return [prop_name for prop_name, _ in properties]
def property_names_to_string(property_names):
    return ', '.join(property_names)

def create_file_from_template(entity_name, properties, template_type, file_type, output_path):
    entity_name_lower = entity_name.lower()
    properties_str = properties_to_params(properties)
    property_names = extract_property_names(properties)
    property_names_str = property_names_to_string(property_names)

    folder_name = 'aspnet_personnal_api' if template_type == 'school' else 'aspnet_recyos_api'
    template_path = f"{folder_name}/{file_type}_template.txt"
    template = read_template(template_path)

    content = template.replace("[EntityName]", entity_name)
    content = content.replace("[EntityNameLower]", entity_name_lower)
    content = content.replace("[Properties]", properties_str)  # Replace with actual properties
    content = content.replace("[PropertyNames]", property_names_str)  # Replace with property names

    with open(output_path, "w") as file:
        file.write(content)


def main():
    template_type = get_template_type()
    entity_name = get_user_input()
    properties = get_entity_properties()

    if (template_type == 'school'):
        create_file_from_template(entity_name, properties, template_type, "repository",f"Repositories/Implementation/{entity_name}Repository.cs")
        create_file_from_template(entity_name, properties, template_type, "repository_interface",f"Repositories/Interface/I{entity_name}Repository.cs")
        create_file_from_template(entity_name, properties, template_type, "service", f"Services/Implementation/{entity_name}Service.cs")
        create_file_from_template(entity_name, properties, template_type, "service_interface",f"Services/Interface/I{entity_name}Service.cs")
        create_file_from_template(entity_name, properties, template_type, "controller", f"Controllers/{entity_name}Controller.cs")
    else:
        create_file_from_template(entity_name, properties, template_type, "repository",f"ORM/EFCore/Repository/{entity_name}Repository.cs")
        create_file_from_template(entity_name, properties, template_type, "repository_interface",f"ORM/Interfaces/I{entity_name}Repository.cs")
        create_file_from_template(entity_name, properties, template_type, "service", f"ORM/Service/{entity_name}Service.cs")
        create_file_from_template(entity_name, properties, template_type, "service_interface",f"ORM/Interfaces/I{entity_name}Service.cs")
        create_file_from_template(entity_name, properties, template_type, "controller", f"Controllers/{entity_name}Controller.cs")

if __name__ == "__main__":
    main()