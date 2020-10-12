#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


school_data = pd.read_csv("/Users/Jorda/Desktop/Pandas Homework/Resources/schools_complete.csv")
student_data = pd.read_csv("/Users/Jorda/Desktop/Pandas Homework/Resources/students_complete.csv")


# In[3]:


school_data


# In[5]:


total_schools = len(school_data)


# In[9]:


total_students = school_data["size"].sum()


# In[10]:


total_budget = school_data["budget"].sum()


# In[11]:


student_data


# In[55]:


average_math = round(student_data["math_score"].mean(), 2)


# In[56]:


average_reading = round(student_data["reading_score"].mean(), 2)


# In[57]:


passed_maths = len(student_data.loc[student_data['math_score'] >= 70])


# In[58]:


percent_passed_math = (passed_maths/total_students)* 100


# In[59]:


passed_reading = len(student_data.loc[student_data['reading_score'] >=70])


# In[60]:


percent_passed_reading = (passed_reading/total_students)* 100


# In[61]:


passed_math_list = student_data.loc[student_data['math_score'] >= 70]


# In[62]:


passed_math_and_reading = len(passed_math_list.loc[student_data['reading_score'] >=70])


# In[63]:


percent_passed_overall = (passed_math_and_reading/total_students)* 100


# In[64]:


len(student_data.loc[student_data['math_score'] >= 70].loc[student_data['reading_score'] >=70])


# In[65]:


(x/total_students)* 100


# In[67]:


pd.DataFrame({"Total Schools":[total_schools], "Total Students":[total_students], "Total Budget":[total_budget], 
              "Average Math Score":[average_math], "Average Reading Score":[average_reading], "% Passing Math":[percent_passed_math],
              "% Passing Reading":[percent_passed_reading], "% Overall Passing":[percent_passed_overall]})


# In[87]:


school_sum1 = school_data.rename(columns={"type":"School Type", "size":"Total Students", "budget":"Total School Budget"})


# In[89]:


del school_sum1['School ID']


# In[91]:


school_sum1


# In[101]:


per_student_budget = school_sum1["Total School Budget"]/school_sum1["Total Students"]
school_sum1["per_student_budget"] = per_student_budget


# In[102]:


school_sum1


# In[106]:


huang_math = student_data.loc[student_data["school_name"] == "Huang High School"]


# In[107]:


huang_math


# In[108]:


huang_avg_math = huang_math["math_score"].mean()


# In[109]:


huang_avg_math


# In[111]:


figueroa_math = student_data.loc[student_data["school_name"] == "Figueroa High School"]


# In[112]:


figueroa_avg_math = figueroa_math["math_score"].mean()


# In[113]:


shelton_math = student_data.loc[student_data["school_name"] == "Shelton High School"]


# In[114]:


shelton_avg_math = shelton_math["math_score"].mean()


# In[115]:


hernandez_math = student_data.loc[student_data["school_name"] == "Hernandez High School"]


# In[116]:


hernandez_avg_math = hernandez_math["math_score"].mean()


# In[117]:


griffin_math = student_data.loc[student_data["school_name"] == "Griffin High School"]


# In[118]:


griffin_avg_math = griffin_math["math_score"].mean()


# In[119]:


wilson_math = student_data.loc[student_data["school_name"] == "Wilson High School"]


# In[120]:


wilson_avg_math = wilson_math["math_score"].mean()


# In[121]:


cabrera_math = student_data.loc[student_data["school_name"] == "Cabrera High School"]


# In[122]:


cabrera_avg_math = cabrera_math["math_score"].mean()


# In[123]:


bailey_math = student_data.loc[student_data["school_name"] == "Bailey High School"]


# In[124]:


bailey_avg_math = bailey_math["math_score"].mean()


# In[125]:


holden_math = student_data.loc[student_data["school_name"] == "Holden High School"]


# In[126]:


holden_avg_math = holden_math["math_score"].mean()


# In[127]:


pena_math = student_data.loc[student_data["school_name"] == "Pena High School"]


# In[204]:


pena_avg_math = pena_math["math_score"].mean()


# In[205]:


wright_math = student_data.loc[student_data["school_name"] == "Wright High School"]


# In[206]:


wright_avg_math = wright_math["math_score"].mean()


# In[207]:


rodriguez_math = student_data.loc[student_data["school_name"] == "Rodriguez High School"]


# In[208]:


rodriguez_avg_math = rodriguez_math["math_score"].mean()


# In[209]:


johnson_math = student_data.loc[student_data["school_name"] == "Johnson High School"]


# In[210]:


johnson_avg_math = johnson_math["math_score"].mean()


# In[211]:


ford_math = student_data.loc[student_data["school_name"] == "Ford High School"]


# In[212]:


ford_avg_math = ford_math["math_score"].mean()


# In[213]:


thomas_math = student_data.loc[student_data["school_name"] == "Thomas High School"]


# In[214]:


thomas_avg_math = thomas_math["math_score"].mean()


# # Short Cut Math Averages

# In[215]:


school_data["school_name"].values


# In[216]:


School_Names = list(school_data["school_name"].values)


# In[217]:


[ [s, student_data.loc[student_data["school_name"] == s]["math_score"].mean() ] for s in School_Names ]


# In[218]:


avg_maths_scores = [student_data.loc[student_data["school_name"] == s]["math_score"].mean() for s in School_Names]


# In[219]:


[i for i in range(5)]


# In[220]:


school_sum1["Average Math Score"] = avg_maths_scores


# In[221]:


school_sum1


# In[222]:


avg_read_scores = [student_data.loc[student_data["school_name"] == s]["reading_score"].mean() for s in School_Names]


# In[223]:


school_sum1["Average Reading Score"] = avg_read_scores


# In[224]:


school_sum1


# In[225]:


percent_passing_math = [
( len(student_data.loc[student_data["school_name"] == School_Names[s]].loc[student_data["math_score"] >= 70]) / school_data["size"][s] ) * 100
    
   for s in range(len(School_Names)) 
]


# In[226]:


percent_passing_reading = [
( len(student_data.loc[student_data["school_name"] == School_Names[s]].loc[student_data["reading_score"] >= 70]) / school_data["size"][s] ) * 100
    
   for s in range(len(School_Names)) 
]


# In[227]:


percent_overall_passing = [
( len(student_data.loc[student_data["school_name"] == School_Names[s]].loc[student_data["reading_score"] >= 70].loc[student_data["math_score"] >= 70]) / school_data["size"][s] ) * 100
    
   for s in range(len(School_Names)) 
]


# In[228]:


school_sum1["Percent Passing Math"] = percent_passing_math
school_sum1["Percent Passing Reading"] = percent_passing_reading
school_sum1["Percent Overall Passing"] = percent_overall_passing


# In[234]:


school_sum1


# In[240]:


Top_Five_Performing = school_sum1.sort_values(by = ["Percent Overall Passing"], ascending=False).head()


# In[241]:


Bottom_Five_Performing = school_sum1.sort_values(by = ["Percent Overall Passing"], ascending=False).tail()


# In[251]:


pd.DataFrame(student_data.groupby(["school_name", "grade"])["math_score"].mean())


# In[252]:


pd.DataFrame(student_data.groupby(["school_name", "grade"])["reading_score"].mean())


# In[261]:


bin1 = school_sum1.loc[school_sum1["per_student_budget"]<584][["Average Math Score", "Average Reading Score", "Percent Passing Math", "Percent Passing Reading", "Percent Overall Passing"]].mean()


# In[263]:


bin2 = school_sum1.loc[school_sum1["per_student_budget"]<=629].loc[school_sum1["per_student_budget"]>=585][["Average Math Score", "Average Reading Score", "Percent Passing Math", "Percent Passing Reading", "Percent Overall Passing"]].mean()


# In[265]:


bin3 = school_sum1.loc[school_sum1["per_student_budget"]<=644].loc[school_sum1["per_student_budget"]>=630][["Average Math Score", "Average Reading Score", "Percent Passing Math", "Percent Passing Reading", "Percent Overall Passing"]].mean()


# In[266]:


bin4 = school_sum1.loc[school_sum1["per_student_budget"]<=675].loc[school_sum1["per_student_budget"]>=645][["Average Math Score", "Average Reading Score", "Percent Passing Math", "Percent Passing Reading", "Percent Overall Passing"]].mean()


# In[267]:


bin4


# In[291]:


School_Spending_Breakdown = pd.DataFrame({"<584":bin1, "585-629":bin2, "630-644":bin3, "645-675":bin4}).transpose()


# In[292]:


School_Spending_Breakdown


# In[277]:


sizebin1 = school_sum1.loc[school_sum1["Total Students"]<1000][["Average Math Score", "Average Reading Score", "Percent Passing Math", "Percent Passing Reading", "Percent Overall Passing"]].mean()


# In[282]:


sizebin2 = school_sum1.loc[school_sum1["Total Students"]<=2000].loc[school_sum1["Total Students"]>=1000][["Average Math Score", "Average Reading Score", "Percent Passing Math", "Percent Passing Reading", "Percent Overall Passing"]].mean()


# In[283]:


sizebin3 = school_sum1.loc[school_sum1["Total Students"]<=5000].loc[school_sum1["Total Students"]>=2000][["Average Math Score", "Average Reading Score", "Percent Passing Math", "Percent Passing Reading", "Percent Overall Passing"]].mean()


# In[289]:


School_Size_Breakdown = pd.DataFrame({"Small (<1000)":sizebin1, "Medium (1000-2000)":sizebin2, "Large (2000-5000)":sizebin3}).transpose()


# In[293]:


School_Size_Breakdown


# In[290]:


School_Type_Breakdown = school_sum1.groupby("School Type")[["Average Math Score", "Average Reading Score", "Percent Passing Math", "Percent Passing Reading", "Percent Overall Passing"]].mean()


# In[294]:


School_Type_Breakdown


# # Discription of Trends

# One trend we can see from this data is that out of the bottom five lowest performing schools, by percent overall passing, three of those schools also ranked in the top five for highest student population. You could make an arguement that schools with a higher number of studentrs trend in being lower performing schools. A reason for this trend may be due to the fact that it may be more difficult to manage higher populations of students given the amount of resources that schoool has access to. 
# 
# Another trend we make from this data is that out of the top five performing schools, by percent overall passing, three of those schools ranked in the top five for lowest student population. You could make conclusions that schools with lower student populations maybe resources can be spread more effectively upon students, thus causing more success. We can also see that when we seperated the shcools based on either district or charter type, we saw that charter schools had over 30% higher overall passing students. 
