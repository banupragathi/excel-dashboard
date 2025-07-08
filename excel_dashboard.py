import os
import pandas as pd
import streamlit as st

st.title('📁 Excel Dashboard - Built-in Data Files')

# Folder where Excel files are stored
folder_path = 'excel_data'

# Check if folder exists
if os.path.exists(folder_path):
    excel_files = [f for f in os.listdir(folder_path) if f.endswith(('.xlsx', '.xls'))]

    if excel_files:
        selected_file = st.selectbox('📄 Select an Excel file:', excel_files)

        if selected_file:
            file_path = os.path.join(folder_path, selected_file)
            try:
                xls = pd.ExcelFile(file_path)
                sheet_names = xls.sheet_names

                selected_sheet = st.selectbox('📑 Select a sheet:', sheet_names)

                if selected_sheet:
                    df = pd.read_excel(xls, sheet_name=selected_sheet)
                    st.success(f'Showing: {selected_file} > {selected_sheet}')
                    st.dataframe(df)
            except Exception as e:
                st.error(f"❌ Error reading the file: {e}")
    else:
        st.warning('No Excel files found in the "excel_data" folder.')
else:
    st.error('❌ "excel_data" folder not found. Please add it next to this file.')

