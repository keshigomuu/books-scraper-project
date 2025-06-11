import pandas as pd
import plotly.express as px
import streamlit as st
import subprocess
import os

@st.cache_data(show_spinner=False)
def run_scraper():
    subprocess.run(["scrapy", "crawl", "books", "-o", "cleaned_books.json"])

run_scraper()


df = pd.read_json("cleaned_books.json")

# Sidebar filter
st.sidebar.title("Book Filters")
categories = df["category"].dropna().unique()
selected_categories = st.sidebar.multiselect("Select Categories", categories, default=list(categories))

filtered_df = df[df["category"].isin(selected_categories)]

# Title
st.title("📚 Books to Scrape - Dashboard")

# Summary
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Books", len(filtered_df))
col2.metric("Unique Categories", filtered_df['category'].nunique())
col3.metric("Average Price (£)", f"{filtered_df['price'].mean():.2f}")

# Visual 1: Books per Category
st.subheader("Books per Category")
cat_counts = filtered_df['category'].value_counts().reset_index()
cat_counts.columns = ['category', 'count']
sort_order = st.radio("Sort by:", ["Descending", "Ascending"], horizontal=True)
cat_counts = cat_counts.sort_values(by='count', ascending=(sort_order == "Ascending"))
fig1 = px.bar(cat_counts, x='category', y='count', title="Number of Books per Category")
st.plotly_chart(fig1)

# Visual 2: Price Distribution
st.subheader("Average Price Trend by Category")

# Group by category and compute mean price
price_trend = filtered_df.groupby("category")["price"].mean().reset_index()

# Sort by category name for consistent line shape
price_trend = price_trend.sort_values("category")

# Create line plot with area fill
fig2 = px.line(price_trend, x="category", y="price", title="Average Price by Category")
fig2.update_traces(fill='tozeroy', line_color='blue', fillcolor='rgba(0, 0, 255, 0.2)', mode='lines+markers')

st.plotly_chart(fig2)


# Visual 3: Avg Rating
st.subheader("Average Rating per Category")
rating_df = filtered_df.groupby("category")["rating"].mean().reset_index()
fig3 = px.bar(rating_df, x="category", y="rating", title="Average Rating")
st.plotly_chart(fig3)

# Visual: Average Price vs Availability
st.subheader("Average Price by Availability")

# Group and average
availability_price = filtered_df.groupby("availability")["price"].mean().reset_index()

# Sort by availability
availability_price = availability_price.sort_values("availability")

fig = px.bar(
    availability_price,
    x="availability",
    y="price",
    title="Average Price by Availability",
    labels={"availability": "Availability (Number in stock)", "price": "Average Price"},
)
st.plotly_chart(fig)
