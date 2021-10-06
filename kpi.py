import streamlit as st
import pandas as pd
import numpy as np 


st.set_page_config(
    page_title = 'Inversion Sample KPI Dashboard',
    page_icon = '✅',
    layout = 'wide'
)




st.markdown(" # Overview of Inversion Customer Aquisition Costs Relationship")
st.image("fb-customer-acquisition-cost.png")
subheader = "If Marketing Activities and Lead Generation tactics are not well thought out, they can drive up the Cost of Customer Acquisition (CAC) and erode your profit margin. Are you spending money and time unnecessarily on the wrong people? It's important to distinguish between:"  
st.markdown(f"<h2 style='text-align: center; color: black;'>{subheader}</h1>", unsafe_allow_html=True)
st.write("")
st.write("")

col1, col2,col3= st.columns(3)
subsub = "Customers attracted by MARKETING CONTENT (Newsletters, Promotions, Seminars etc)"
mqlsql = "Marketing Qualified Leads  VS  Sales Qualified Leads"
subsub2 = "Customers who show an ACTIVE INTEREST in purchasing a product (Request a quote, Fill out an CRM form)"

with col1:
    st.markdown(f"<h4 style='text-align: left; color: black;'>{subsub}</h2>", unsafe_allow_html=True)
    
with col2:
     st.image("MQL-vs-SQL.jpeg")
with col3: 
    st.markdown(f"<h4 style='text-align: right; color: black;'>{subsub2}</h2>", unsafe_allow_html=True)
    

     

conclusion = "It's easy to be unaware that you are spending time and money on people interested in your marketing content and not enough on people who are actively interested in purchasing your product or service. Sometimes we are interested in a businesses product, and will sign up for the newsletter but we may never intend (or could never afford) to buy the product." 
conclusion2 = "By focusing on SQL lead generation, and allocating your resources to SQLs, you can decreases your CAC which will increase your profit per customer"  
st.markdown(f"<h4 style='text-align: left; color: black;'>{conclusion}</h4>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: left; color: black;'>{conclusion2}</h4>", unsafe_allow_html=True)
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

st.subheader("Consider all of the costs related to Customer Aquisition. An example can be seen above")

st.image("CAC COSTS.png")

st.subheader("Now consider the effect of these costs being allocated to people only interested in marketing content. Sales people may waste time following up on the wrong opportunities")
    

st.write("---")

WHY = "Why is CAC important?"
CALCULATION = "CAC Margin Calculation"
Method = "Method for CAC Calculation"

#st.markdown(f"<h1 style='text-align: center; color: black;'>{WHY}</h1>", unsafe_allow_html=True)
#st.subheader(" ✔︎ Enables your business to asses which segments of your customer base are most efficient and profitable")
#st.subheader(" ✔︎ Helps to drive profit margins as you scale")
#st.subheader(" ✔︎ Powerful metric to calculate the resulting ROI from an Investor standpoint")
#st.subheader("")
#st.markdown(f"<h1 style='text-align: center; color: black;'>{Method}</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: left; color: black;'>{CALCULATION}</h2>", unsafe_allow_html=True)

st.subheader("_CAC formula = Total Costs to Aqcuire Customers / Number of Customers_")
st.subheader("_CAC Margin formula = Total Costs to Aqcuire Customers / Revenue_")
st.subheader("_Gross Profit After CAC Margin = 1 - CAC Margin_")
st.subheader("The relationship of Customer Acquisition Cost with Profit can best be illustrated with the CAC margin. You can explore the effects of changes in CAC after the next section")

st.image("MockCAC.png")
                            
st.write("---")                               

HOW = "How can CAC be Decreased?"
st.markdown(f"<h1 style='text-align: center; color: black;'>{HOW}</h1>", unsafe_allow_html=True)
st.subheader(" ✔︎ Focus on top performing acquisition channels")
st.subheader(" ✔︎ Assess sales process")
st.subheader(" ✔︎ Focus efforts on SQL leads")
st.subheader(" ✔︎ Build the Brand")
st.subheader(" ✔︎ Improve Sales Funnel")
st.subheader(" ✔︎ Increase Organic Traffic")


st.write("---")
CAC_selection = st.slider('CAC % Decrease: ',
                                min_value= 0,
                                max_value= 10)
RevenueperCustomer = 500000
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
WriteUP = "Return on Paying for Inversion's Service = "

col13,col14 = st.columns(2)
with col13: 
    st.markdown(f"<h2 style='text-align: left; color: green;'>{WriteUP}</h2>", unsafe_allow_html=True)

with col14: 
    st.markdown(f"<h2 style='text-align: left; color: green;'>{ReturnONInversion}</h2>", unsafe_allow_html=True)  

#### KPI Slider Section      
st.write("----")
st.markdown("<h1 style='text-align: center; color: black;'>Inversion Process</h1>", unsafe_allow_html=True)
st.subheader("Inversion aims to decrease CAC through its powerful Brand Process and an emphasis on brand creation and strength. By having a strong brand, customers with active interest in your product will come to you. Meaning that investing in your brand now brings you cheap, even free Sales Qualified customers in the long run")
    
Relationship = "As CAC Margin ⬇︎ Gross Profit after CAC will ⬆︎. See for yourself below!"
st.markdown(f"<h3 style='text-align: center; color: black;'>{Relationship}</h3>", unsafe_allow_html=True)

st.subheader("Lets put these ratios into action!")
st.write("Below is the output of our different ratios before manipulating the CAC Margin thanks to Inversions processes")

TCA = 160000
NumCust = 11
Rev = 500000
InversionCost = 42000

CAC = TCA/NumCust
CACMAR = TCA/Rev

GPACAC = 1-CACMAR

InversionCost = 42000
IncrementalGain = 340000 - (Rev * GPACAC)
ROI = IncrementalGain/InversionCost


st.write("Customer Aquisition Cost: ", CAC)
st.write("Customer Aquisition Cost MARGIN", CACMAR)
st.write("Gross Profit after CAC Margin", GPACAC)
#st.write("Initial Return on Inversion", ROI, )
    
        
st.title("Return on Inversion")
st.subheader("Adjust CAC Margin here")
CAC_selection = st.slider('CAC % Scenario: ',
                                min_value= -0.05,
                                max_value= 0.05, value = 0.0, step = 0.01)
st.write("Chosen CAC MARGIN:", CAC_selection)

NewCACMAR = CACMAR*(1+CAC_selection)
NewGPACAC = 1-NewCACMAR
NewIncrementalGain = 340000 - (Rev * NewGPACAC)
NewROI = NewIncrementalGain/InversionCost

st.write("Customer Aquisition Cost: ", CAC)
st.write("NEW Customer Aquisition Cost MARGIN", NewCACMAR)
st.write("NEW Gross Profit after CAC Margin Change", NewGPACAC)
st.write("Return on Inversion after CAC Change", NewROI)
    
st.write("---") 











