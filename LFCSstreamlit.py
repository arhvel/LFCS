# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 18:28:34 2021

@author: adeyem01
"""


from LFCS import LFCS1P
import streamlit as st
import pandas as pd
import base64

from io import BytesIO

ResultDataFrame = pd.DataFrame()

filename = None

st.write("""
         
         # This is the l-Length Contiguous Frequent Subsequence (i.e., LCFS) Explorer.
         ## It mines and output a user-defined length of contiguous patterns.
         ### This data mining explorer  avails:
         1. Provision of unique patterns repetitive frequencies.
         2. Provision of unique patterns relative and absolute support.
         3. Provision of unique patterns Super-sequence indexes.
         4. Exploration and sorting of identified patterns
         
         
         """)


explorer = LFCS1P('Explorer1')
st.write('### A LFCS instance is running.')
    
st.write(' ### Step 2: Do upload a two-columned csv file i.e. Index and Sequences')
uploaded_file = st.file_uploader("Upload your csv file")


if uploaded_file is not None:
    st.text('Loading data...')
    explorer.Data(uploaded_file)
    uploadname = uploaded_file.name
    st.write('Loading data...done!')
    
    
    st.write('Enter the pattern length to be mined below:')
    maxlength = st.number_input(label="pattern length?", min_value=1, value=3, format="%.i") 
    
    if st.checkbox(label='Do you want to shift the start position for mining'):
        st.write('#### Please, ensure the start position is not longer than the maximum lenght of the sequences')   
        startpos = st.number_input(label="Enter Start Postion?", min_value=2, value=2, format="%.i")
        name = str(maxlength) + '-LFC patterns mined from Start Position ' + str(startpos) + ' obtained from ' + uploadname
        filename = name
        namee = str(maxlength) + '_'+str(startpos)+'-LFCS_' + uploadname
        
        ResultDataFrame = pd.DataFrame()
        layout = st.expander('Generated Patterns Panel', expanded=True)
            
        with layout:
            st.write('### Step 3:')
            if st.button(label='Run LFCS'):
                LFCSitems, LFCSitemsAppearances = explorer.i_lfcs(maxlength,startpos)
                
                st.write("Mining Completed! Processing unique patterns.")

        
                # ### Secondary Operation
                frame = pd.DataFrame(LFCSitems, columns = ['Patterns','SuperSequences','Absolute Support', 'Relative Support %'])
                frame1 = pd.DataFrame(LFCSitemsAppearances, columns=['Patterns','SuperSequences','Appearance'])
                frame['Appearance'] = frame1['Appearance'].copy()
                
                arrangement  = frame['SuperSequences']

                rearranged =[]
                for app in arrangement:
                    converted = [item for t in app for item in t]
                    converted.sort()
                    rearranged.append(str(converted))


                frame['SuperSequences'] = pd.DataFrame(rearranged,columns = ['Supersequences']) 
               
                #print last twenty uniqe consecutive items
                st.write("Processing your Data Frame of uniqe contiguous items....")
                     
                SortedCrosstab = frame.copy()
                        
                SortedCrosstab = SortedCrosstab.sort_values('Absolute Support', ascending=False)
                
                SortedCrosstab = SortedCrosstab.reset_index(drop=True)
                ResultDataFrame = SortedCrosstab.copy()
                st.write("Analysis Completed ...")
                    
                st.write("Styling your output to fit the container below")
                #styled = SortedCrosstab.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
                #st.dataframe(styled.set_properties(**{'text-align': 'center'}).hide_index())
                st.dataframe(SortedCrosstab)
                    
                st.write('### Step 4:')
                st.write('#### Click the link below to download ' + filename)

                csv = ResultDataFrame.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()
                download = f'<a href="data:file/csv;base64,{b64}" download={namee}>Download csv file</a>'
                st.markdown(download,unsafe_allow_html=True)
                


    else:    
        name = str(maxlength) + '-LFC patterns obtained from ' + uploadname
        filename = name
        namee = str(maxlength) + '-LFCS_' + uploadname
            
        ResultDataFrame = pd.DataFrame()
        layout = st.expander('Generated Patterns Panel', expanded=True)
        
        with layout:
            st.write('### Step 3:')
            if st.button(label='Run LFCS'):
                LFCSitems, LFCSitemsAppearances = explorer.lfcs(maxlength)
                
                st.write("Mining Completed! Processing unique patterns.")

        
                # ### Secondary Operation
                frame = pd.DataFrame(LFCSitems, columns = ['Patterns','SuperSequences','Absolute Support', 'Relative Support %'])
                frame1 = pd.DataFrame(LFCSitemsAppearances, columns=['Patterns','SuperSequences','Appearance'])
                frame['Appearance'] = frame1['Appearance'].copy()

                arrangement  = frame['SuperSequences']

                rearranged =[]
                for app in arrangement:
                    converted = [item for t in app for item in t]
                    converted.sort()
                    rearranged.append(str(converted))


                frame['SuperSequences'] = pd.DataFrame(rearranged,columns = ['Supersequences']) 
               
                #print last twenty uniqe consecutive items
                st.write("Processing your Data Frame of uniqe contiguous items....")
                     
                SortedCrosstab = frame.copy()
                        
                SortedCrosstab = SortedCrosstab.sort_values('Absolute Support', ascending=False)
                
                SortedCrosstab = SortedCrosstab.reset_index(drop=True)
                ResultDataFrame = SortedCrosstab.copy()
                st.write("Analysis Completed ...")
                    
                st.write("Styling your output to fit the container below")
                #styled = SortedCrosstab.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
                #st.dataframe(styled.set_properties(**{'text-align': 'center'}).hide_index())
                st.dataframe(SortedCrosstab)
                    
                st.write('### Step 4:')
                st.write('#### Click the link below to download ' + filename)
                csv = ResultDataFrame.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()
                download = f'<a href="data:file/csv;base64,{b64}" download={namee}>Download csv file</a>'
                st.markdown(download,unsafe_allow_html=True)

else:
    st.warning("Please upload your csv file")


            

