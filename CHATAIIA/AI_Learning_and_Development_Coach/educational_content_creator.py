# Educational Content Creator 
def create_educational_content(topic, format):
    # Fungsi untuk membuat konten pendidikan
    # Bisa termasuk pembuatan video, tutorial, quiz, dll.
    content = f"Created {format} on {topic}"
    return content

if __name__ == "__main__":
    topic = 'Advanced CAD Techniques'
    format = 'Video Tutorial'
    content = create_educational_content(topic, format)
    print(content)
