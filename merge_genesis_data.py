
import os
import json
import shutil
import sys

def merge_and_process_files(date_str):
    # Define paths
    speed_json_path = os.path.join('genesis-init-speed', f'{date_str}.json')
    memory_json_path = os.path.join('genesis-init-memory', f'{date_str}.json')
    result_json_path = os.path.join('genesis-data', f'{date_str}.json')

    speed_html_path = os.path.join('genesis-init-speed', f'{date_str}.html')
    new_speed_html_path = os.path.join('genesis-data', f'{date_str}.speed.json')

    memory_html_path = os.path.join('genesis-init-memory', f'{date_str}.html')
    new_memory_html_path = os.path.join('genesis-data', f'{date_str}.memory.json')

    metadata_json_path = os.path.join('genesis-init-speed', f'{date_str}.metadata.json')
    new_metadata_json_path = os.path.join('genesis-data', f'{date_str}.metadata.json')

    # Ensure the input files exist
    if not os.path.exists(speed_json_path):
        print(f"Speed JSON file not found: {speed_json_path}")
        return
    if not os.path.exists(memory_json_path):
        print(f"Memory JSON file not found: {memory_json_path}")
        return

    # Read the speed data
    with open(speed_json_path, 'r') as speed_file:
        speed_data = json.load(speed_file)

    # Read the memory data
    with open(memory_json_path, 'r') as memory_file:
        memory_data = json.load(memory_file)

    # Merge the data
    merged_data = {
        'speed': speed_data,
        'memory': memory_data
    }

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(result_json_path), exist_ok=True)

    # Save the merged data
    with open(result_json_path, 'w') as result_file:
        json.dump(merged_data, result_file, indent=4)

    # Move and rename HTML files
    if os.path.exists(speed_html_path):
        shutil.move(speed_html_path, new_speed_html_path)
    else:
        print(f"Speed HTML file not found: {speed_html_path}")

    if os.path.exists(memory_html_path):
        shutil.move(memory_html_path, new_memory_html_path)
    else:
        print(f"Memory HTML file not found: {memory_html_path}")

    # Copy metadata JSON file
    if os.path.exists(metadata_json_path):
        shutil.copy(metadata_json_path, new_metadata_json_path)
    else:
        print(f"Metadata JSON file not found: {metadata_json_path}")

    print(f"Processed files for date {date_str}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_and_process.py <date>")
        print("Example: python merge_and_process.py 20230101")
    else:
        date_str = sys.argv[1]
        merge_and_process_files(date_str)