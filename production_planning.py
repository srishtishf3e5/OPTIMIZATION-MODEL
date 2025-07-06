import pulp
import matplotlib.pyplot as plt

def main():
    # Step 1: Define the problem - Maximize profit
    problem = pulp.LpProblem("Production_Planning", pulp.LpMaximize)

    # Step 2: Define decision variables - units produced
    x = pulp.LpVariable('Product_A_units', lowBound=0, cat='Continuous')
    y = pulp.LpVariable('Product_B_units', lowBound=0, cat='Continuous')

    # Step 3: Objective function - Maximize profit
    problem += 40*x + 50*y, "Total_Profit"

    # Step 4: Constraints
    problem += 2*x + 3*y <= 120, "Labor_Constraint"
    problem += 4*x + 2*y <= 100, "Material_Constraint"

    # Step 5: Solve the optimization problem
    problem.solve()

    # Step 6: Print the results
    print(f"Status: {pulp.LpStatus[problem.status]}")
    print(f"Optimal production of Product A: {pulp.value(x)} units")
    print(f"Optimal production of Product B: {pulp.value(y)} units")
    print(f"Maximum Profit: ${pulp.value(problem.objective)}")

    # Step 7: Visualize the results
    products = ['Product A', 'Product B']
    units = [pulp.value(x), pulp.value(y)]

    plt.bar(products, units, color=['blue', 'orange'])
    plt.ylabel('Units Produced')
    plt.title('Optimal Production Plan')
    plt.show()

if __name__ == "_main_":
    main()
