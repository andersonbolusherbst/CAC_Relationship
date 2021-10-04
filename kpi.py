import streamlit as st
import pandas as pd
import numpy as np 
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from millify import millify

st.set_page_config(
    page_title = 'Inversion Sample KPI Dashboard',
    page_icon = '✅',
    layout = 'wide'
)




st.markdown(" # Overview of Inversion Customer Aquisition Costs Relationship")
st.image("fb-customer-acquisition-cost.png")
subheader = "Marketing Activities and Lead Generation can become inefficient if we fail to distinguish between these two important factors:"  
st.markdown(f"<h1 style='text-align: center; color: black;'>{subheader}</h1>", unsafe_allow_html=True)

col1, col2,col3= st.columns(3)
subsub = "Customers attracted by MARKETING CONTENT (Newsletters, Promotions, Seminars etc)"
subsub2 = "Customers who show an ACTIVE INTEREST in purchasing a product (Request a quote, Fill out an CRM form)"

with col1:
    st.markdown(f"<h2 style='text-align: left; color: black;'>{subsub}</h2>", unsafe_allow_html=True)
    
with col2:
    pass
with col3: 
    st.markdown(f"<h2 style='text-align: right; color: black;'>{subsub2}</h2>", unsafe_allow_html=True)
    

st.image("MQL-vs-SQL.jpeg")
     

conclusion = "Are you spending time and money on the wrong section of your customer base?" 
conclusion2 = "By focussing on SQL lead generation, you can decreases you CAC which will increase your profit per customer"  
st.markdown(f"<h3 style='text-align: left; color: black;'>{conclusion}</h3>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: left; color: black;'>{conclusion2}</h3>", unsafe_allow_html=True)
st.write("")
st.write("")

# col4, col5, col6 , col7, col8,col9,col10 = st.columns(7)

# with col4:
#     pass
# with col5:
#     pass
# with col6:
#     pass
# with col8:
#     pass
# with col9:
#     pass
# with col10:
#     pass
# with col7 :
#     #stage1 = st.button("Next")
#     pass


st.write("---")

st.image("CAC COSTS.png")
    
st.subheader("Consider all of the costs related to Customer Aquisition. An example can be seen above")

st.write("---")

WHY = "Why is CAC important?"
CALCULATION = "CAC Margin Calculation"
Method = "Method for CAC Calculation"

st.markdown(f"<h1 style='text-align: center; color: black;'>{WHY}</h1>", unsafe_allow_html=True)
st.subheader(" ✔︎ Enables your business to asses which segments of your customer base are most efficient and profitable")
st.subheader(" ✔︎ Helps to drive profit margins as you scale")
st.subheader(" ✔︎ Powerful metric to calculate the resulting ROI from an Investor standpoint")
st.subheader("")
st.markdown(f"<h1 style='text-align: center; color: black;'>{Method}</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: left; color: black;'>{CALCULATION}</h2>", unsafe_allow_html=True)

st.image("CACMArgin.png")

st.markdown(" ## Gross Profit after CAC")
st.image("GPAfterCAC.png")
                            
st.write("---")                               

HOW = "How can CAC be Decreased?"
st.markdown(f"<h1 style='text-align: center; color: black;'>{HOW}</h1>", unsafe_allow_html=True)
st.subheader(" ✔︎ Focus on top performing acquisition channels")
st.subheader(" ✔︎ Assess sales process")
st.subheader(" ✔︎ Focus efforts on SQL leads")
st.subheader(" ✔︎ Build the Brand")
st.subheader(" ✔︎ Improve Sales Funnel")

st.write("---")

st.markdown(" # Inversion Process ")
st.write("Inversion aims to decrease CAC through its powerful Brand Process and an emphasis on brand creation and strength")
    
Relationship = "As CAC Margin ⬇︎ Gross Profit after CAC will ⬆︎. See for yourself below!"
st.markdown(f"<h2 style='text-align: left; color: black;'>{Relationship}</h2>", unsafe_allow_html=True)

CAC_selection = st.slider('CAC % Decrease: ',
                                min_value= 0,
                                max_value= 10)
RevenueperCustomer = 50000
CACMARGIN = CAC_selection/RevenueperCustomer  
GPAFTERCAC = 1-CACMARGIN 
Write = "Gross Profit After Customer Aquisition Cost Decrease = "

col11,col12 = st.columns(2)

with col11:
    st.markdown(f"<h2 style='text-align: left; color: green;'>{Write}</h2>", unsafe_allow_html=True) 
with col12:
    st.markdown(f"<h2 style='text-align: left; color: green;'>{GPAFTERCAC}</h2>", unsafe_allow_html=True)
st.write("")
st.write("")
st.image("Return on Inversion.png")
st.write("")
st.write("")
InversionCost = 42000
IncrementalGain = GPAFTERCAC
ReturnONInversion = IncrementalGain/InversionCost
WriteUP = "Return on Paying for Inversions Service = "

col13,col14 = st.columns(2)
with col13: 
    st.markdown(f"<h2 style='text-align: left; color: green;'>{WriteUP}</h2>", unsafe_allow_html=True)

with col14: 
    st.markdown(f"<h2 style='text-align: left; color: green;'>{ReturnONInversion}</h2>", unsafe_allow_html=True)    
    







# CAC, 
# Count of SQLs, 
# SQL conversion rate (website traffic/number of CRM lead forms completed - this is Bitrix for September) , 
# SQL to deals rate ( called Sales Win Rate) , 
# count of sales, 
# ARPC, 
# Retun on marketing (Marketing costs ( This is all costs related to acquiring customers)/Revenue)
# # kpi 1 

# col1, col2, col3,col4 = st.columns(4)
# st.write("")
# st.write("")
# col5, col6, col7, col8= st.columns(4)
# st.write("")
# st.write("")

# header = "Return on Inversion"
# st.markdown(f"<h1 style='text-align: center; color: black;'>{header}</h1>", unsafe_allow_html=True)
# subheader = "Here we would use a model to 'sum' the impact of the above metrics to illustrate their overall impact on Driveaway SA"
# subheader2 = "The figures used here are simply placeholders"
# st.markdown(f"<h3 style='text-align: center; color: black;'>{subheader}</h3>", unsafe_allow_html=True)
# st.markdown(f"<h3 style='text-align: center; color: black;'>{subheader2}</h3>", unsafe_allow_html=True)
# g = 87
# st.markdown(f"<h1 style='text-align: center; color: black;'>{g}</h1>", unsafe_allow_html=True)
# g1 = "⬆︎21.7%"
# st.markdown(f"<h2 style='text-align: center; color: green;'>{g1}</h2>", unsafe_allow_html=True)  

# col1.metric("CAC - Customer Aquisition Cost", "R1561.60", "0%")
# col2.metric("SQL Count", "40", "0%")
# col3.metric("SQL Conversion Rate", "3.3%", "0%")
# col4.metric("SQl to Deal Rate", "12.5%", "0%")
# col5.metric("Deals Count", "5", "0%")
# col6.metric("ARPC - Average Revenue per Customer ",millify(44326, precision=2), "0%")
# col7.metric("Return on Marketing", "65.79%", "0%")
# col8.metric("Cost of Aquisition Margin", "34.21%", "0%")

# st.header("**KPI Notes**")
# st.subheader("CAC ---> Average monthly cost was pulled from the period July 2020-2021. It was adjusted for the deal period 1 Sept - 20 Sept. ")
# st.subheader("Average revenue per customer needs to be updated with more accurate inputs")


# st.markdown("<hr/>",unsafe_allow_html=True)


# st.markdown("## Driveaway SA Sales KPI's: OPTIONAL FUTURE LAYOUT")

# st.image("Marketing_to_Sales_Funnel.jpeg")
# st.write("This dashboard will be linked with the data from either Google Analytics or a consolidated database encompasing all of the data needed for month to month KPI calculation")
# st.write("This dashboard will try to illustrate the Marketing and Sales funnels shown above")

# # kpi 1 

# kpi01, kpi02, kpi12, = st.columns(3)
# st.text("")
# st.text("")
# kpi03, kpi04, kpi05, kpi13 = st.columns(4)
# st.text("")
# st.text("")
# kpi06, kpi07, kpi08, kpi14 = st.columns(4)
# st.text("")
# st.text("")
# kpi09, kpi10, kpi11, kpi15 = st.columns(4)



# with kpi01:
#     header = "Alignment"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 111 
#     st.markdown(f"<h2 style='text-align: center; color: yellow;'>{number1}</h2>", unsafe_allow_html=True)

# with kpi02:
#     header = "Retention"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 222 
#     st.markdown(f"<h2 style='text-align: center; color: yellow;'>{number1}</h2>", unsafe_allow_html=True)

# with kpi03:
#     header = "CLTV - Customer Lifetime Value"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 555 
#     st.markdown(f"<h2 style='text-align: center; color: orange;'>{number1}</h2>", unsafe_allow_html=True)

# with kpi04:
#     header = "ARPC - Average Revenue Per Customer "
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 333 
#     st.markdown(f"<h2 style='text-align: center; color: orange;'>{number1}</h2>", unsafe_allow_html=True)

# with kpi05:
#     header = "Average Deal Size "
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h2 style='text-align: center; color: orange;'>{number1}</h2>", unsafe_allow_html=True)

# with kpi06:
#     header = "SQO Count"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h2 style='text-align: center; color: purple;'>{number1}</h2>", unsafe_allow_html=True)

# with kpi07:
#     header = "SQO Conversion Rate"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h2 style='text-align: center; color: purple;'>{number1}</h2>", unsafe_allow_html=True)

# with kpi08:
#     header = "SQO Time to Close"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h2 style='text-align: center; color: purple;'>{number1}</h2>", unsafe_allow_html=True)   

# with kpi09:
#     header = "MQL Count"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h2 style='text-align: center; color: blue;'>{number1}</h2>", unsafe_allow_html=True)  

# with kpi10:
#     header = "MQL Conversion Rate"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h2 style='text-align: center; color: blue;'>{number1}</h2>", unsafe_allow_html=True)  

# with kpi11:
#     header = "MQL Time to Count"
#     st.markdown(f"<h3 style='text-align: center; color: black;'>{header}</h3>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h2 style='text-align: center; color: blue;'>{number1}</h2>", unsafe_allow_html=True)

# with kpi12:
#     header = "CAC - Customer Aquisition Cost"
#     st.markdown(f"<h1 style='text-align: center; color: black;'>{header}</h1>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

# with kpi13:
#     header = "Customer Value"
#     st.markdown(f"<h1 style='text-align: center; color: black;'>{header}</h1>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h1 style='text-align: center; color: orange;'>{number1}</h1>", unsafe_allow_html=True)


# with kpi14:
#     header = "SQO"
#     st.markdown(f"<h1 style='text-align: center; color: black;'>{header}</h1>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h1 style='text-align: center; color: purple;'>{number1}</h1>", unsafe_allow_html=True)


# with kpi15:
#     header = "MQL"
#     st.markdown(f"<h1 style='text-align: center; color: black;'>{header}</h1>", unsafe_allow_html=True)
#     number1 = 444 
#     st.markdown(f"<h1 style='text-align: center; color: blue;'>{number1}</h1>", unsafe_allow_html=True) 

# header = "Sales"
# st.markdown(f"<h1 style='text-align: center; color: black;'>{header}</h1>", unsafe_allow_html=True)
# subheader = "Need to work out a model which sums this to provide metric for Sales"
# st.markdown(f"<h3 style='text-align: center; color: black;'>{subheader}</h3>", unsafe_allow_html=True)
# g = 87
# st.markdown(f"<h1 style='text-align: center; color: black;'>{g}</h1>", unsafe_allow_html=True)
# g1 = "⬆︎21.7%"
# st.markdown(f"<h2 style='text-align: center; color: green;'>{g1}</h2>", unsafe_allow_html=True)                     


# st.markdown("<hr/>",unsafe_allow_html=True)

# st.markdown("## Visulization Section")
# st.write("The idea behind this section would be to illustrate certain KPIs shown above. Examples of some of Driveaways features have been shown below as an example.")

# chart1, chart2 = st.columns(2)
# chart3, chart4 =st.columns(2)

# with chart1:
#     st.image("Deal Stage.png")

# with chart2:
#     st.image("Vehicle Make Breakdown.png")
# with chart3:
#     st.image("Average Purchase Price Over Time.png")

# with chart4:
#     st.image("Average Lease Amount Over Time.png")  

# st.markdown("<hr/>",unsafe_allow_html=True)





