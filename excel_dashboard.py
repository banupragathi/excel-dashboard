import pandas as pd
import os
import streamlit as st

# Function to load Excel files
def load_excel_files(folder_path):
    excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]
    return excel_files

# Function to display sheets
def display_sheets(file_path):
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    return sheet_names

# Streamlit dashboard
st.title('📊 Excel Sheets Dashboard with Charts')

folder_path = 'excel_data'
if not os.path.exists(folder_path):
    st.error('❌ "excel_data" folder not found. Please add it next to this file.')
else:
    excel_files = load_excel_files(folder_path)
    selected_file = st.selectbox('Select an Excel file:', excel_files)

    if selected_file:
        file_path = os.path.join(folder_path, selected_file)
        sheets = display_sheets(file_path)
        selected_sheet = st.selectbox('Select a sheet to display:', sheets)

        if selected_sheet:
            df = pd.read_excel(file_path, sheet_name=selected_sheet)
            st.subheader('📄 Table Preview')
            st.write(df)

            numeric_cols = df.select_dtypes(include='number').columns.tolist()
            if numeric_cols:
                st.subheader("📈 Visualize a Chart")
                chart_type = st.selectbox("Choose chart type:", ["Bar Chart", "Line Chart", "Area Chart"])
                x_axis = st.selectbox("X-axis column:", df.columns)
                y_axis = st.selectbox("Y-axis column (numeric only):", numeric_cols)

                if chart_type == "Bar Chart":
                    st.bar_chart(df.set_index(x_axis)[y_axis])
                elif chart_type == "Line Chart":
                    st.line_chart(df.set_index(x_axis)[y_axis])
                elif chart_type == "Area Chart":
                    st.area_chart(df.set_index(x_axis)[y_axis])
            else:
                st.info("This sheet has no numeric columns to plot.")


