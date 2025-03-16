import numpy as np
import customtkinter as ctk

def get_matrix_from_entries(entries, rows, cols):
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            try:
                matrix[i, j] = float(entries[i][j].get())
            except ValueError:
                return " invalid entry please try again "
    return matrix

def matrix_inverse_solution (matrix_a_entries, matrix_a_rows, matrix_a_cols, matrix_b_entries, matrix_b_rows, matrix_b_cols):
    matrix_a = get_matrix_from_entries(matrix_a_entries, matrix_a_rows, matrix_a_cols)
    matrix_b = get_matrix_from_entries(matrix_b_entries, matrix_b_rows, matrix_b_cols)

    try:
        matrix_a_inv = np.linalg.inv(matrix_a)
        print (matrix_a_inv)
    except np.linalg.LinAlgError:
        print("Matrix inversion failed")
        exit()

    result_matrix = np.dot(matrix_a_inv, matrix_b)
    return result_matrix

def create_matrix_inputs(rows, cols, frame):
    matrix_entries = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = ctk.CTkEntry(frame, width=40)
            entry.grid(row=i, column=j, padx=2, pady=2)
            row_entries.append(entry)
        matrix_entries.append(row_entries)
    return matrix_entries

