# Candidate Screener 
def screen_candidate(candidate_info, job_requirements):
    # Fungsi untuk menyaring kandidat berdasarkan persyaratan pekerjaan
    # Bisa berupa pemeriksaan resume, keterampilan, pengalaman, dll.
    is_qualified = all(req in candidate_info['skills'] for req in job_requirements)
    return is_qualified

if __name__ == "__main__":
    candidate_info = {'name': 'Alice', 'skills': ['CAD', '3D Modeling', 'Communication']}
    job_requirements = ['CAD', '3D Modeling']
    result = screen_candidate(candidate_info, job_requirements)
    print(f"Candidate {candidate_info['name']} Qualified: {result}")
