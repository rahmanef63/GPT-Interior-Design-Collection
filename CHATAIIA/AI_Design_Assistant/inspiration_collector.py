# Inspiration Collector 
# Contoh sederhana untuk mengumpulkan inspirasi desain dari internet
import requests

def fetch_design_inspiration(keyword):
    # Gunakan API untuk mencari gambar atau artikel terkait desain
    # Misalnya, menggunakan Unsplash API atau API serupa
    response = requests.get(f"https://api.unsplash.com/search/photos?query={keyword}&client_id=YOUR_ACCESS_KEY")
    return response.json()

if __name__ == "__main__":
    keyword = "modern interior"
    inspirations = fetch_design_inspiration(keyword)
    print(inspirations)
