# OPTIMIZATION-MODEl
COMPANY: CODETECH IT SOLUTIONS

NAME: SRISHTI SHARMA 

INTERN ID: CT04DN466

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION OF THE PROJECT:

📌 Project Overview Optimization techniques play a critical role in business decision-making, enabling organizations to utilize limited resources efficiently while maximizing profit or minimizing cost. This project demonstrates how a Linear Programming model can be formulated and solved using Python to determine the optimal production quantities of multiple products under resource constraints.

The use case for this project involves a manufacturing unit that produces two products, each requiring labor and raw materials in different proportions. With limited resources available, the goal is to identify the optimal production mix that maximizes total profit while adhering to the given constraints.

🎯 Objectives To gain practical experience in formulating optimization problems.

To understand and apply linear programming concepts using Python.

To implement and solve an LP model using the PuLP library.

To derive insights from the model solution for business decision-making.

To visualize the results for easier interpretation and communication.

🛠 Tools & Technologies Programming Language: Python

Optimization Library: PuLP

Visualization: Matplotlib

Development Environment: PyCharm / Jupyter Notebook

🧪 Methodology

Defining the Business Problem The company produces two products:
Each product generates a specific profit per unit.

Both require different amounts of labor hours and raw materials.

There is a limited supply of each resource.

The goal is to maximize total profit while staying within these resource limits.

Formulating the Linear Program Decision Variables:
x = units of Product A to produce

y = units of Product B to produce

Objective Function:

Maximize total profit: 40x + 50y

Constraints:

Labor constraint: 2x + 3y ≤ 120

Material constraint: 4x + 2y ≤ 100

Non-negativity: x ≥ 0, y ≥ 0

Implementing the Model in Python Using the PuLP library, the problem was modeled and solved in the following steps:
Define the LP problem and objective.

Create decision variables.

Add constraints to the model.

Solve the model using PuLP’s built-in solver.

The code was structured to be modular and clear, and results were printed directly, showing optimal production levels and maximum profit.

Evaluating and Visualizing Results After solving the model:
The optimal number of units for each product was identified.

The maximum achievable profit under the given constraints was calculated.

A bar chart was plotted using Matplotlib to visualize the production plan.

📈 Results & Conclusion The linear programming model successfully calculated the optimal number of units of Product A and Product B to produce in order to maximize profit while staying within labor and material constraints. The results clearly demonstrated how optimization techniques can be applied to real-world production planning scenarios.

This project provided a hands-on understanding of:

Linear programming and constraint modeling

The use of PuLP for optimization problems

Translating a business problem into a mathematical model

Interpreting and visualizing results for decision support

✅ Key Takeaways Optimization models offer powerful tools for solving resource allocation problems.

Even simple models can yield significant business value.

PuLP in Python provides an accessible yet robust framework for solving LP problems.

Visualization enhances communication of model insights to stakeholders.
