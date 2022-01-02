"""
You have data for a variety of professions,
and you want to increase the salaries of just the data scientists by 10 percent every other year.
starting in the year 2024.

First, you create a NumPy array with each row holding the expected yearly salaries of one professional
(data scientist, product manager, designer, or software engineer).

Each column gives the respective future years’ salaries in 2025, 2026, and 2027.
The resulting NumPy array has four rows and three columns.

You have funds available to reinforce the most important professionals in the company.
You believe in the future of data science, so you decide to reward the hidden heroes of your company:
 the data scientists.

You need to update the NumPy array so that only the data scientists’
salaries increase by 10 percent every other year (non-cumulatively), starting from the year 2025.
"""


# Working with NumPy Arrays: Slicing, Broadcasting, and Array Types
def selective_increase(employees):
    employees[0, ::2] = employees[0, ::2] * 1.1


if __name__ == "__main__":
    ## Dependencies
    import numpy as np

    ## Data: yearly salary in ($1000) [2025, 2026, 2027]
    dataScientist = [130, 132, 137]
    productManager = [127, 140, 145]
    designer = [118, 118, 127]
    softwareEngineer = [129, 131, 137]
    employees = np.array([dataScientist,
                          productManager,
                          designer,
                          softwareEngineer])

    ## One-liner
    selective_increase(employees)

    ## Result
    print(employees)
    '''
    expected result looks like 
    [[143 132 150]
     [127 140 145]
     [118 118 127]
     [129 131 137]]
    '''
