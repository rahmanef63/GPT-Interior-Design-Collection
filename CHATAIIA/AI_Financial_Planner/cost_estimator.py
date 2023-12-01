# Cost Estimator 
def estimate_project_cost(material_costs, labor_costs):
    # Fungsi ini akan membuat estimasi biaya proyek berdasarkan biaya material dan tenaga kerja
    total_cost = sum(material_costs) + sum(labor_costs)
    return total_cost

if __name__ == "__main__":
    material_costs = [500, 200, 300]  # Contoh biaya material
    labor_costs = [1000, 1500]  # Contoh biaya tenaga kerja
    total_cost = estimate_project_cost(material_costs, labor_costs)
    print(f"Total Estimated Cost: {total_cost}")
