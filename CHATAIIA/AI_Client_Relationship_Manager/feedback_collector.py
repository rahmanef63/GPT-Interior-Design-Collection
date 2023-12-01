# Feedback Collector 
def collect_client_feedback(client_info):
    # Fungsi untuk mengumpulkan dan menganalisis feedback klien
    # Bisa berupa survei, wawancara, dll.
    feedback = "Feedback dari klien"
    print(f"Collected feedback from {client_info['name']}: {feedback}")
    return feedback

if __name__ == "__main__":
    client_info = {'name': 'Jane Doe', 'email': 'janedoe@example.com'}
    feedback = collect_client_feedback(client_info)
