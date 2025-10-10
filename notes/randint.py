my_list = [1, 2, 3, "apple", 5, "banana"]
element_to_find = "apple"

# Check if the element is in the list
found_true_or_false = element_to_find in my_list

print(f"Is '{element_to_find}' in the list? {found_true_or_false}")

element_to_find_not_present = "grape"
found_true_or_false_not_present = element_to_find_not_present in my_list

print(f"Is '{element_to_find_not_present}' in the list? {found_true_or_false_not_present}")