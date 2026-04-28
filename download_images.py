import requests
import os

def download_images(urls_file, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(urls_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    for i, url in enumerate(urls, 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                ext = url.split('.')[-1].split('?')[0]
                filename = f"image_{i}.{ext}"
                filepath = os.path.join(output_folder, filename)
                with open(filepath, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Downloaded {filename}")
            else:
                print(f"Failed to download {url}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    urls_file = input("Enter path to urls.txt: ")
    output_folder = input("Enter output folder: ")
    download_images(urls_file, output_folder)
