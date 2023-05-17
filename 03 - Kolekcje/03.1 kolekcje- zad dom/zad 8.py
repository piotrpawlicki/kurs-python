def list_item_counter(poem):
    poem_count = {}
    for word in poem:
        if word not in poem_count:
            poem_count[word] = 1
        else:
            poem_count[word] += 1
    return poem_count


names ={
    'Poland' : ['Zuzanna', 'Julia', 'Maja', 'Hanna', 'Lena', 'Alicja', 'Amelia', 'Victoria', 'Olivia', 'Nicole'],
    'Germany' : ["Sophie", "Marie", "Maria", "Emilia", "Hannah", "Mia", "Anna", "Johanna", "Lina", "Emma"],
    'Italy' : ["Sofia", "Giulia", "Aurora", "Alice", "Emma", "Giorgia", "Martina", "Ginevra", "Chiara", "Sara"],
    'France' : ["Emma", "Jade", "Louise", "Alice", "Chloe", "Leah", "Manon", "Lina", "Rose", "Camille"],
    'Spain': ["Maria", "Lucia", "Paula", "Martina", "Sofia", "Julia", "Carla", "Valeria", "Daniela", "Alba"],
    'UK': ["Olivia", "Amelia", "Isla", "Ava", "Emily", "Lily", "Sophia", "Grace", "Freya", "Charlotte"],
    'Netherlands' : ["Emma", "Tess", "Sophie", "Julia", "Anna", "Lieke", "Lotte", "Eva", "Sanne", "Noa"],
    'Sweden' : ["Alice", "Elsa", "Saga", "Ella", "Lilly", "Ebba", "Olivia", "Maja", "Agnes", "Alva"],
    'Denmark' : ["Sofia", "Ida", "Freja", "Ella", "Alma", "Emma", "Clara", "Josefine", "Anna", "Karla"],
    'Norway' : ["Emma", "Sophie", "Nora", "Emilie", "Thea", "Ingrid", "Maja", "Linnea", "Amalie", "Oda"]
}


list_of_names_temp = list(names.values())
list_of_names = []
for row in list_of_names_temp:
    list_of_names.extend(row)
result = list_item_counter(list_of_names)

for key, value in result.items():
    if value > 2 :
        print(key)