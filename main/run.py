import customtkinter as ctk

import helpers

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Linear Algebra Project | Reverse Array")
root.geometry("500x600")


def run():
    #Create all fonts and labels for the use of the GUI
    project_label = ctk.CTkLabel(root,text= "Group 5: Joshua Torrez, Carter Tiesman, Nguyen Lam",text_color="grey")
    project_label.place(relwidth=1.37, relheight=1.97)

    sub_font = ctk.CTkFont(size = 10)

    equation_label = ctk.CTkLabel(root, text = "(A   )B = ")
    equation_label.place(x = 88, y = 348)

    equation_inv_label = ctk.CTkLabel(root, text = "-1",font=sub_font)
    equation_inv_label.place(x = 100, y = 340)

    #Create all the labels needed for our
    matrix_a_label = ctk.CTkLabel(root,text = "A =")
    matrix_a_label.place(x = 150, y = 45)
    matrix_a_frame = ctk.CTkFrame(root)
    matrix_a_frame.pack(pady=10)
    matrix_a_rows, matrix_a_cols = 3, 3
    matrix_a_entries = helpers.create_matrix_inputs(matrix_a_rows, matrix_a_cols, matrix_a_frame)

    matrix_a_label = ctk.CTkLabel(root, text="B =")
    matrix_a_label.place(x=150, y=165)
    matrix_b_frame = ctk.CTkFrame(root)
    matrix_b_frame.pack(pady=10)
    matrix_b_rows, matrix_b_cols = 3, 1
    matrix_b_entries = helpers.create_matrix_inputs(matrix_b_rows, matrix_b_cols, matrix_b_frame)

    def display_result(result_matrix):
        for widget in result_frame.winfo_children():
            widget.destroy()

        result_rows, result_cols = result_matrix.shape
        for i in range(result_rows):
            for j in range(result_cols):
                entry = ctk.CTkEntry(result_frame, width=40)
                entry.insert(0, str(result_matrix[i][j]))
                entry.configure(state="disabled")
                entry.grid(row=i, column=j, padx=2, pady=2)

    result_frame = ctk.CTkFrame(root)
    result_frame.pack(pady=10)
    result_label = ctk.CTkLabel(root, text="")
    result_label.pack()

    def button():
        result = helpers.matrix_inverse_solution(matrix_a_entries, matrix_a_rows, matrix_a_cols, matrix_b_entries,matrix_b_rows, matrix_b_cols)
        if isinstance(result, str):
            result_label.configure(text=result)
        else:
            display_result(result)
    inverse_button = ctk.CTkButton(root, text="solve", command=button)
    inverse_button.pack(pady=5)

run()
root.mainloop()
