#%%
import matplotlib.pyplot as plt
import pandas as pd 
#%%
df = pd.read_csv('GDPlist.csv')
#%%
df['Country']= df['Country'].map(lambda x:x.lstrip('�'))
df
#%%
#Biểu đồ để hiển thị giá trị cụ thể và so sánh GDP các nước Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.
df_vn = df[df['Country'] =='Vietnam']
df_indo = df[df['Country'] =='Indonesia']
df_cam = df[df['Country'] =='Cambodia']
df_thai = df[df['Country'] =='Thailand']
df_ma = df[df['Country'] =='Malaysia']

#%%
fig, ax = plt.subplots(3, 2)
ax[0][0].plot(df_vn['GDP (millions of US$)'], marker = '*')
ax[0][0].set_ylabel('GDP (millions of US$)')
ax[0][0].set_title('Viet Nam')

ax[1][0].plot(df_indo['GDP (millions of US$)'], marker = '*')
ax[1][0].set_ylabel('GDP (millions of US$)')
ax[1][0].set_title('Indonesia')

ax[2][0].plot(df_cam['GDP (millions of US$)'], marker = '*')
ax[2][0].set_ylabel('GDP (millions of US$)')
ax[2][0].set_title('Cambodia')
ax[2][0].set_xlabel('GDP')

ax[0][1].plot(df_thai['GDP (millions of US$)'], marker = '*')
ax[0][1].set_title('Thailand')

ax[1][1].plot(df_ma['GDP (millions of US$)'], marker = '*')
ax[1][1].set_title('Malaysia')
ax[2][1].set_xlabel('GDP')

plt.show()

# %%
