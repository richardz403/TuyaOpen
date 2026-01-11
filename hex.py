import re

def format_to_c_array(text, array_name="my_image_data", vals_per_line=12):
    # 1. Extract all hex values (removing existing 0x if present)
    raw_hexes = re.findall(r'\b(?:0x)?([0-9A-Fa-f]{2,4})\b', text)
    
    # 2. Start the C array declaration
    output = f"const uint8_t {array_name}[] = {{\n    "
    
    # 3. Add values with 0x, commas, and line breaks
    for i, val in enumerate(raw_hexes):
        output += f"0x{val.lower()}"
        
        # Add comma if not the last element
        if i < len(raw_hexes) - 1:
            output += ", "
        
        # Add a newline every 'vals_per_line' elements
        if (i + 1) % vals_per_line == 0 and i < len(raw_hexes) - 1:
            output += "\n    "
            
    output += "\n};"
    return output

# --- Usage ---
input_data = "AA BB CC DD 11 22 33 44 A1 B2 C3 D4" # Paste your hex table here
print(format_to_c_array(input_data))