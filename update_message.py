import json

def update_message(button_num, new_text, file_path=None):
    """Helper function to update button messages"""
    try:
        with open('messages.json', 'r+') as f:
            messages = json.load(f)
            messages[str(button_num)] = {
                "text": new_text,
                "file": file_path
            }
            f.seek(0)
            json.dump(messages, f, indent=4)
            f.truncate()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error updating messages: {e}")

# Example usage:
# update_message(1, "New romantic message", "path/to/file.jpg")
