import streamlit as st 
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns

import joblib

with open("mlr.pkl", "rb") as file:
    model = joblib.load(file)

st.title( model)


# class mlapp():
#     pages = ["Data", "Viz_1"]
    
      
#     @staticmethod
#     def pageCreate(self):
        
#         pages.append("Viz_"+len(pages)-1)
#         Page = st.sidebar.radio("Navigation",pages)
#         return pages

#     @staticmethod
#     def navigations():
#         pages = ["Data", "Viz_1"]
#         Page = st.sidebar.radio("Navigation",pages)
#         if Page == pages[0]:

#             st.title("Do Data Analysis")
# # name = st.text_input("Enter your name: ")
# # st.write("you did it ",name)

# # st.checkbox("checkbox label")
# # st.button("Start")
# # import streamlit as st

# # import time
# # age = st.slider("Please select your age",1900, 2024, 2000)
# # year = 2024 - age
# # st.write(f"you are {year} years old.")
#             if data is not None:
#                 dat = pd.read_csv(data)
#                 df = pd.DataFrame(dat)
#                 indices = [i for i in range(1,df.shape[0]+1)]
#                 df.set_index(pd.Index(indices),inplace=True)
#                 head_l = [i for i in range(-15,df.shape[0],5)]
#     # head_l = [-5,-10,-15] + head_l
#                 t = st.selectbox('Select an option', head_l,index=3)
#                 if t < 0:

#                     peek = st.table(df.tail(-t))
#                 else:
#                     peek = st.table(df.head(t))
        
#             return st.write("Welcome home")




#     # df = pd.DataFrame(dat)
#     # fd = df

# ml = mlapp()
# # ml.pageCreate()
# if st.button("create a page")==True:
#     ml.pageCreate
#     # st.write(pages)
# ml.navigations()
# st.write()
# if Page == pages[1]:
#     if data:
#         st.title("Do Visualization")
#         graphs = st.checkbox("Graphs")
#         dat = pd.read_csv(data)
#         df = pd.DataFrame(dat)
        
       
#         a =0
#         global r
#         r = 1
#         c = 2
#         global g
#         g = 0
#         global xco
#         global yco
#         xco =0
#         yco =0
#         if graphs:
#             bar = st.checkbox("Bar Chart")
           
#             line = st.checkbox("Line Chart")
           

#             scatter = st.checkbox("Scatter Chart")
#             # area = st.checkbox("Area Chart")
           
#             hist = st.checkbox("histogram")
#         #    st.radio("Select the graph type",("bar Chart","line chart","histogram","area chart")) 
           
#             ng = st.slider("Please select how many graphs are you going to create",1,8,2)
#             # if a==0:
#             x_var = st.selectbox("Please select a variable as a x axis", df.columns, index = 1)
#             y_var = st.selectbox("Please select the variable as Y axis", df.columns, index = 2)
#             fig, ax = plt.subplots(nrows=2, ncols=c,figsize=(12,6))
            
        
            
#             # if bar or line or scatter or hist:
#             #     g +=1
#             #     if 2*r < g:
#             #         r+=1
#             #     fig, ax = plt.subplots(nrows=r, ncols=c,figsize=(12,6))
#             if hist:
                
                
#                 g +=1
                
#                 if g > 1 and yco < c-1:
#                     yco+=1
#                 elif g>1 and xco< r-1:
#                     xco+=1
                 
#                 #     fig, ax = plt.subplots(nrows=r, ncols=c,figsize=(12,6))
#                 bins = st.slider("Select the bin numbers",10, 30, 15)
#                 sns.histplot(df,x=x_var,bins=bins, ax=ax[xco, yco])
#                 ax[xco, yco].set_title(x_var + 'frequency')
#                 ax[xco, yco].set_xlabel(x_var)
#                 ax[xco, yco].set_ylabel('frequency')
#                 ax[xco, yco].grid(True)
#                 plt.tight_layout()
                
#             if bar:
                
#                 g +=1
#                 if g > 1 and yco < c-1:
#                     yco+=1
#                 elif g>1 and xco< r-1:
#                     xco+=1
                
#                 xx_var = df['country']
#                 sns.barplot(x='country', y=y_var, data=df.sort_values(by=y_var, ascending=False).iloc[:20,:], ax=ax[xco, yco])
#                 ax[xco, yco].set_title('country' +" vs "+y_var)
#                 plt.xticks(rotation=90)
#                 ax[xco, yco].set_xlabel('country')
#                 ax[xco, yco].set_ylabel(y_var)
#                 ax[xco, yco].grid(True)
#                 plt.tight_layout()
                
#             if scatter:
                
#                 g +=1
#                 if g > 1 and yco < c-1 and xco< r-1:
#                     yco+=1
#                 elif g>1 and xco< r-1:
#                     xco+=1
#                 #     r+=1
#                 #     fig, ax = plt.subplots(nrows=r, ncols=c,figsize=(12,6))
#                 sns.scatterplot(data=df, x = df[x_var],y=df[y_var], ax = ax[xco, yco])
#                 ax[xco, yco].set_title(x_var +" vs "+y_var)
#                 ax[xco, yco].set_xlabel(x_var)
#                 ax[xco, yco].set_ylabel(y_var)
#                 ax[xco, yco].grid(True)
#                 plt.tight_layout()
               
#             st.pyplot(fig)
#             st.write(xco, yco, g)
#             # else:
#             # st.caption("Click the visuals to view the charts")

#         # def histo(x,bins):
#         #     sns.histplot(df,x,bins,kde=True)

        
#         # st.button(f"r: {r}, g: {g}" )
        
        
#             # plt.xlabel()
#             # plt.ylabel()
#             # plt.title("histograam")
            
            

#         # fig, ax = plt.subplots(nrows=r, ncols=c,figsize=(12,6))
#         # x_var = st.selectbox("Please select a variable as a x axis", df.columns, index = 1)
#         # y_var = st.selectbox("Please select the variable as Y axis", df.columns, index = 2)
#         # sns.scatterplot(data=df, x = df[x_var],y=df[y_var], ax = ax[0])
#         # ax[0].set_title(x_var +" vs "+y_var)
#         # ax[0].set_xlabel(x_var)
#         # ax[0].set_ylabel(y_var)
#         # ax[0].grid(True)
#         # plt.tight_layout()

#         # xx_var = df['country']
        
#         # sns.barplot(x='country', y=y_var, data=df.sort_values(by=y_var, ascending=False).iloc[:20,:], ax=ax[1])
#         # ax[1].set_title('country' +" vs "+y_var)
#         # plt.xticks(rotation=90)
#         # ax[1].set_xlabel('country')
#         # ax[1].set_ylabel(y_var)
#         # ax[1].grid(True)
#         # plt.tight_layout()
#         # bins = st.slider("Select the bin numbers",10, 30, 15)
        
            
#         # plt.show()
        
#     # st.button("Peek Data", peek)
# # df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
# # my_data_element = st.line_chart(df)

# # for tick in range(10):
# #     # time.sleep(.5)
# #     add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
# #     my_data_element.add_rows(add_df)

# # st.button("Regenerate")