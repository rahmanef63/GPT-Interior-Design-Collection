# Client Communicator 
def manage_client_communication(client_info, message):
    # Fungsi untuk mengelola komunikasi dengan klien
    # Bisa mengirim email, pesan, dll.
    print(f"Sending message to {client_info['name']}: {message}")
    # Implementasi pengiriman pesan nyata
    pass

if __name__ == "__main__":
    client_info = {'name': 'John Doe', 'email': 'johndoe@example.com'}
    message = "Update proyek terbaru..."
    manage_client_communication(client_info, message)
