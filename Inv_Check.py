import streamlit as st
import pandas as pd
import base64
import io, os
# arr=[41.53,41.53,46.61,46.61,46.61,46.61,52.54,55.93,58.47,58.47,58.47,58.47,79.66,93.22,95.77,105.08,105.08,105.08,116.94,121.19,121.19,121.19,128.81,131.36,132.2,134.75,134.75,134.75,134.75,134.75,134.75,134.75,134.75,143.22,147.46,151.69,151.69,151.69,154.24,155.08,155.08,155.08,155.08,155.08,155.08,155.08,159.32,160.17,163.56,164.41,164.41,164.41,165.25,165.25,168.64,168.64,168.64,168.64,168.64,168.64,171.18,171.19,172.88,172.88,174.58,179.66,189.83,189.83,194.07,197.46,202.54,203.39,211.02,222.03,230.51,230.51,237.29,239.83,242.38,242.38,247.46,264.4,266.11,269.5,270.34,270.34,270.34,270.34,276.28,277.97,277.97,277.97,278.81,286.44,286.44,291.52,303.39,304.24,304.24,306.77,309.32,310.16,328.82,328.82,331.36,332.2,333.05,333.9,333.9,337.28,337.28,339.83,354.24,354.24,354.24,359.33,373.73,373.73,379.66,384.75,387.29,405.08,405.08,405.1,405.93,412.72,417.81,438.14,438.14,442.38,458.46,467.86,468.64,472.88,504.23,505.92,505.92,522.05,522.88,527.12,533.91,539,541.53,548.3,561.02,568.64,581.36,584.75,633.05,643.22,643.23,646.6,649.15,663.58,674.56,676.28,700.86,709.32,709.32,715.25,723.72,728.82,809.3,833.91,848.31,855.08,942.39,1000.01,1004.23,1024.57,1058.5,1062.71,1074.58,1103,1121.21,1192.37,1266.96,1328.78,1566.11,1603.38,1639.87,1665.22,1673.71,1722.05,1747.46,1829.66,1848.31,1863.53,1955.09,1993.21,1998.27,2036.48,2059.35,2183.94,2198.3,2277.97,2322.88,2369.5,2411.06,2444.94,2649.17,2810.13,2861.07,3057.58,3372.02,3561.83,3672.91,3871.21,3963.57,4229.66,4619.58,5029.58,5068.74,5227.91,5396.55,6022.03,10469.48,11126.3,13539.25,14827.02,16057.37,17595.45,18820.19,22513.14,24226.87,28080.21,61930.53
# ]


st.title("Rohit Bhai the Great....!")

# try:
    # arr=list(map(int,input("Enter Total Amount: ").split()))
    # aa=st.text_area("Enter Total Amount: ")
    # arr=list(map(int,aa.split(" ")))

        
# except:
    # arr=list(map(float,input("Enter Total Amount: ").split()))
    # ab=st.text_area("Enter Total Amount: ")
    # arr1=list(map(float,ab.split(" ")))


    
arr=''
aa=st.text_input("Enter Total Amount: ")

if aa:
    try:
        arr=list(map(int,aa.split(" ")))
    except:
        arr=list(map(float,aa.split(" ")))
else:
    pass


aa=[]
a=0


for i in arr:
    a=a+i
    if a>39800:
        break
    else:
        aa.append(i)
    # arr.remove(i)
    # aa=[j for j in arr if j not in aa]

# print(aa)

# for i in aa:
#     with open("Inv_Check.txt","a") as f:
#         f.write(str(i)+"\n")

towrite = io.BytesIO()
ab=pd.DataFrame(aa,columns=["Amount"],index=range(1,len(aa)+1))
ab.to_csv(towrite,encoding="utf-8",index=False,header=True)
towrite.seek(0)
b64 = base64.b64encode(towrite.read()).decode()
linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="AmtData.csv">Download file</a>'
st.markdown(linko, unsafe_allow_html=True)


raw_text=st.button("Raw Text")
if raw_text:
    for i in aa:
        st.text(i)
else:
    st.warning("")


