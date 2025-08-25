import requests
import os

def download_file(url, save_path):
    try:
        # Send GET request to the URL link 
        response = requests.get(url)
        
        # Check if the request was successful (receive status code 200)
        if response.status_code == 200:
            # Write the content of the response to a local file
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded successfully: {save_path}")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

base_url = {"URL"}

save_dir = {"Directory to save the file"}# use forward slashes for Windows


for i in range(2, 412):
    url = f"{base_url}{i}
    save_path= f"{save_dir}"
    download_file(url, save_path)
