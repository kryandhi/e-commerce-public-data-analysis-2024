import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg  
import urllib
import seaborn as sns
import streamlit as st
from func import DataAnalyzer
from func import BrazilMapPlotter
from babel.numbers import format_currency
import numpy as np

# Set the style for seaborn
sns.set(style='whitegrid')  # Use 'whitegrid' for a cleaner look

# Dataset
datetime_cols = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
all_df = pd.read_csv("all_data.csv")
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

for col in datetime_cols:
    all_df[col] = pd.to_datetime(all_df[col])

min_date = all_df["order_approved_at"].min()
max_date = all_df["order_approved_at"].max()

# Geolocation Dataset
geolocation = pd.read_csv('geolocation.csv')
data = geolocation.drop_duplicates(subset='customer_unique_id')

for col in datetime_cols:
    all_df[col] = pd.to_datetime(all_df[col])

min_date = all_df["order_approved_at"].min()
max_date = all_df["order_approved_at"].max()

# Sidebar
with st.sidebar:
    # Title with logo
    st.image("foto.png", width=150)  # Replace with the path to your logo
    st.title("Komang Ryandhi Suandita")

    # Date Range
    start_date, end_date = st.date_input(
        label="Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# Main
main_df = all_df[(all_df["order_approved_at"] >= str(start_date)) & 
                 (all_df["order_approved_at"] <= str(end_date))]

function = DataAnalyzer(main_df)
map_plot = BrazilMapPlotter(data, plt, mpimg, urllib, st)

daily_orders_df = function.create_daily_orders_df()
sum_spend_df = function.create_sum_spend_df()
sum_order_items_df = function.create_sum_order_items_df()
review_score, common_score = function.review_score_df()
state, most_common_state = function.create_bystate_df()
order_status, common_status = function.create_order_status()


# Title
st.header("E-Commerce Public Dataset Dashboard")

# Daily Orders
st.subheader("Daily Orders")

col1, col2 = st.columns(2)

with col1:
    total_order = daily_orders_df["order_count"].sum()
    st.markdown(f"Total Orders: **{total_order}**")

with col2:
    total_revenue = format_currency(daily_orders_df["revenue"].sum(), "IDR", locale="id_ID")
    st.markdown(f"Total Revenue: **{total_revenue}**")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    daily_orders_df["order_approved_at"],
    daily_orders_df["order_count"],
    marker="o",
    linewidth=2,
    color="skyblue"  # Use a solid color for this plot
)
ax.tick_params(axis="x", rotation=45)
ax.tick_params(axis="y", labelsize=15)
st.pyplot(fig)

with st.expander("See Explanation"):
        st.write('Dari grafik yang divisualisasikan, terlihat fluktuasi penjualan harian yang signifikan, kemungkinan disebabkan oleh faktor musiman. Total penjualan mencapai Rp19.657.996,94 dengan 95.795 pesanan.')



# Order Items
st.subheader("Order Items")
col1, col2 = st.columns(2)

with col1:
    total_items = sum_order_items_df["products"].sum()
    st.markdown(f"Total Items: **{total_items}**")

with col2:
    avg_items = sum_order_items_df["products"].mean()
    st.markdown(f"Average Items: **{avg_items:.2f}**")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))

# Create a color map based on the number of products sold
colors = plt.cm.viridis(np.linspace(0, 1, 5))  # Using 'viridis' colormap for better visibility

# Plot Best Selling Products
sns.barplot(x="products", y="product_category_name_english", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Sales", fontsize=15)
ax[0].set_title("Best Selling Products", loc="center", fontsize=20)
ax[0].tick_params(axis='y', labelsize=15)
ax[0].tick_params(axis='x', labelsize=12)

# Plot Worst Selling Products
sns.barplot(x="products", y="product_category_name_english", data=sum_order_items_df.sort_values(by="products", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sales", fontsize=15)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Selling Products", loc="center", fontsize=20)
ax[1].tick_params(axis='y', labelsize=15)
ax[1].tick_params(axis='x', labelsize=12)

st.pyplot(fig)

with st.expander("See Explanation"):
        st.write('Grafik di atas menunjukkan data penjualan produk secara keseluruhan. Terdapat total 114.810 item yang terjual dengan rata-rata 1617.04 item per transaksi. Kategori produk yang paling banyak terjual adalah bed_bath_table, diikuti oleh health_beauty, sports_leisure, furniture_decor, dan computers_accessories. Sebaliknya, kategori produk yang paling sedikit terjual adalah arts_and_craftmanship, la_cuisine, cds_dvds_musicals, fashion_children_clothes, dan security_and_services.')


# Review Score
st.subheader("Review Score")

# Convert start_date and end_date to datetime objects
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Convert 'review_creation_date' column to datetime if not already
all_df['review_creation_date'] = pd.to_datetime(all_df['review_creation_date'], format='ISO8601')

# Filter data based on the selected date range
review_data = all_df[
    (all_df['review_creation_date'] >= start_date) & 
    (all_df['review_creation_date'] <= end_date)
]

col1, col2 = st.columns(2)

with col1:
    total_reviews = review_data.shape[0]
    st.markdown(f"Total Reviews: **{total_reviews}**")

with col2:
    avg_review = review_data['review_score'].mean()
    st.markdown(f"Average Review Score: **{avg_review:.2f}**")

fig, ax = plt.subplots(figsize=(20, 10))

# Create a color map based on review scores
colors = plt.cm.viridis(np.linspace(0, 1, 5))  # Using 'viridis' colormap for better visibility

# Create a bar plot for review scores by month with color mapping
sns.countplot(x=review_data['review_creation_date'].dt.month,
              hue=review_data['review_score'],
              palette=colors)

plt.title("Customer Satisfaction", fontsize=20)
plt.xlabel("Month")
plt.ylabel("Count of Reviews")
plt.legend(title="Review Score", loc='upper right', bbox_to_anchor=(1.2, 1))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(range(0, 12), months)

st.pyplot(fig)

with st.expander("See Explanation"):
        st.write('Terdapat total 113.997 ulasan produk dengan rata-rata skor 4,08. Grafik menunjukkan jumlah ulasan per bulan dan distribusi skor ulasan. Secara keseluruhan, produk memiliki reputasi yang baik dengan mayoritas ulasan memberikan skor tinggi.')


# Order Approved
st.subheader("Orders Approved")

all_df = all_df[(all_df['order_approved_at'] >= start_date) & (all_df['order_approved_at'] <= end_date)]

monthly_order = all_df.resample(rule='M', on='order_approved_at').agg({
    "order_id": "size",
})
monthly_order.index = monthly_order.index.strftime('%B')
monthly_order = monthly_order.reset_index()
monthly_order.rename(columns={
    "order_id": "order_count",
}, inplace=True)
monthly_order = monthly_order.sort_values('order_count').drop_duplicates('order_approved_at', keep='last')
month_mapping = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

monthly_order["month_numeric"] = monthly_order["order_approved_at"].map(month_mapping)
monthly_order = monthly_order.sort_values("month_numeric")
monthly_order = monthly_order.drop("month_numeric", axis=1)

col1, col2 = st.columns(2)

with col1:
    # Calculate total orders and average orders per month
    total_orders = all_df.shape[0]
    st.markdown(f"Total Orders Approved: **{total_orders}**")

with col2:
    # Average orders per month
    avg_orders_per_month = all_df.resample(rule='M', on='order_approved_at').size().mean()
    st.markdown(f"Average Orders per Month: **{avg_orders_per_month:.2f}**")

fig, ax = plt.subplots(figsize=(20, 10))

# Create the plot
ax.plot(
    monthly_order["order_approved_at"],
    monthly_order["order_count"],
    marker='o',
    linewidth=2,
    color="skyblue"  # Use a solid color for this plot
)

# Set title and labels
ax.set_title("Number of Orders Approved per Month", loc="center", fontsize=20)
ax.tick_params(axis="x", labelsize=10, rotation=45)
ax.tick_params(axis="y", labelsize=10)

# Use st.pyplot and pass the figure
st.pyplot(fig)

with st.expander("See Explanation"):
        st.write('Dari grafik yang divisualisasikan, terlihat adanya penurunan yang cukup drastis pada jumlah pesanan di bulan September, diikuti dengan lonjakan signifikan pada bulan November. Hal ini menunjukkan fluktuasi yang cukup tajam dalam pola pesanan selama periode tersebut.')


# Customer Demographic
st.subheader("Customer Demographic")
tab1, tab2, tab3 = st.tabs(["State", "Order Status", "Geolocation"])

with tab1:
    most_common_state = state.customer_state.value_counts().index[0]
    st.markdown(f"Most Common State: **{most_common_state}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=state.customer_state.value_counts().index,
                y=state.customer_count.values, 
                data=state,
                palette=["#068DA9" if score == most_common_state else "#D3D3D3" for score in state.customer_state.value_counts().index]
                    )

    plt.title("Number customers from State", fontsize=15)
    plt.xlabel("State")
    plt.ylabel("Number of Customers")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab2:
    common_status_ = order_status.value_counts().index[0]
    st.markdown(f"Most Common Order Status: **{common_status_}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=order_status.index,
                y=order_status.values,
                order=order_status.index,
                palette=["#068DA9" if score == common_status else "#D3D3D3" for score in order_status.index]
                )
    
    plt.title("Order Status", fontsize=15)
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab3:
    
    
    map_plot.plot() 


    with st.expander("See Explanation"):
        st.write('Berdasarkan grafik yang telah dibuat, mayoritas pelanggan terkonsentrasi di wilayah tenggara dan selatan. Selain itu, terdapat jumlah pelanggan yang lebih tinggi di kota-kota besar yang berperan sebagai ibu kota, seperti São Paulo, Rio de Janeiro, dan Porto Alegre.')



st.caption('Copyright (C) Komang Ryandhi Suandita 2024')
