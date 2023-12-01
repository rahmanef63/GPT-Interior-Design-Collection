# Budget Analyzer 
def analyze_budget(budget, expenses):
    # Fungsi ini akan menganalisis dan mengelola anggaran
    remaining_budget = budget - sum(expenses)
    return remaining_budget

if __name__ == "__main__":
    budget = 5000  # Anggaran proyek
    expenses = [2000, 1500, 800]  # Biaya yang sudah dikeluarkan
    remaining_budget = analyze_budget(budget, expenses)
    print(f"Remaining Budget: {remaining_budget}")
