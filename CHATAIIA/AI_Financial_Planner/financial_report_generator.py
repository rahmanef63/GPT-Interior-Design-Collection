# Financial Report Generator 
def generate_financial_report(revenues, expenses):
    # Fungsi ini akan membuat laporan keuangan
    net_profit = sum(revenues) - sum(expenses)
    return {"Net Profit": net_profit, "Revenues": sum(revenues), "Expenses": sum(expenses)}

if __name__ == "__main__":
    revenues = [5000, 7000, 6000]  # Pendapatan
    expenses = [2000, 3000, 1500]  # Pengeluaran
    report = generate_financial_report(revenues, expenses)
    print(report)
