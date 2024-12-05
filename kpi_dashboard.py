import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load the CSV file containing sales data
df = pd.read_csv("sales_data.csv")

# Convert the 'Date' column to datetime format and extract the year
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

# Calculate Average Order Value (AOV) by dividing total sales by quantity sold
df['AOV'] = df['TotalSales'] / df['QuantitySold']

# Group data by year and product category to analyze total sales and average AOV
grouped_data = df.groupby(['Year', 'Category']).agg({
    'TotalSales': 'sum',
    'AOV': 'mean'
}).reset_index()

# Calculate Return on Marketing Spend (ROMS) assuming a uniform marketing spend of 100,000 per year
marketing_spend_per_year = 100000
df['ROMS'] = df['TotalSales'] / marketing_spend_per_year

# Group ROMS data by year and category
roms_data = df.groupby(['Year', 'Category']).agg({'ROMS': 'sum'}).reset_index()

# Calculate total sales by product category for pie chart visualization
total_sales_by_category = df.groupby('Category')['TotalSales'].sum().reset_index()

# Create a bar chart for annual revenue by category
fig1 = px.bar(
    grouped_data, x='Year', y='TotalSales', color='Category',
    title='Annual Revenue by Category',
    labels={'Year': 'Year', 'TotalSales': 'Total Revenue', 'Category': 'Product Category'},
    barmode='stack', color_discrete_sequence=px.colors.qualitative.Set2
)

# Create a bar chart for AOV (Average Order Value) by category over the years
fig2 = go.Figure()
for category in grouped_data['Category'].unique():
    category_data = grouped_data[grouped_data['Category'] == category]
    fig2.add_trace(go.Bar(
        x=category_data['Year'], y=category_data['AOV'], name=category,
        marker=dict(color=px.colors.qualitative.Set2[grouped_data['Category'].unique().tolist().index(category)])
    ))

# Add a line showing the overall average AOV across all categories
overall_aov = grouped_data.groupby('Year')['AOV'].mean()
fig2.add_trace(go.Scatter(
    x=overall_aov.index, y=overall_aov, mode='lines+markers', name='Overall Average AOV',
    line=dict(color='black', dash='dash')
))
fig2.update_layout(
    title='Average Order Value (AOV) per Category',
    xaxis_title='Year',
    yaxis_title='Average Order Value (AOV)',
    barmode='group',
    legend_title='Product Category'
)

# Create a bar chart for ROMS (Return on Marketing Spend) by category
fig3 = px.bar(
    roms_data, x='Year', y='ROMS', color='Category',
    title='ROMS per Category',
    labels={'Year': 'Year', 'ROMS': 'Return on Marketing Spend', 'Category': 'Product Category'},
    barmode='stack', color_discrete_sequence=px.colors.qualitative.Set2
)

# Create a pie chart showing revenue distribution across categories
fig4 = px.pie(
    total_sales_by_category, values='TotalSales', names='Category',
    title='Revenue Distribution by Category',
    labels={'Category': 'Product Category', 'TotalSales': 'Total Revenue'},
    color='Category',
    color_discrete_sequence=px.colors.qualitative.Set2
)

# Combine all charts into one dropdown 
combined_fig = go.Figure()
combined_fig.add_traces(fig1.data)
combined_fig.add_traces(fig2.data)
combined_fig.add_traces(fig3.data)
combined_fig.add_traces(fig4.data)

# Create dropdown buttons to toggle between different visualizations
combined_fig.update_layout(
    updatemenus=[
        {
            "buttons": [
                {"label": "Annual Revenue by Category", "method": "update", "args": [{"visible": [True] * len(fig1.data) + [False] * (len(fig2.data) + len(fig3.data) + len(fig4.data))}, {"title": "Annual Revenue by Category"}]},
                {"label": "AOV per Category", "method": "update", "args": [{"visible": [False] * len(fig1.data) + [True] * len(fig2.data) + [False] * (len(fig3.data) + len(fig4.data))}, {"title": "Average Order Value (AOV) per Category"}]},
                {"label": "ROMS per Category", "method": "update", "args": [{"visible": [False] * (len(fig1.data) + len(fig2.data)) + [True] * len(fig3.data) + [False] * len(fig4.data)}, {"title": "ROMS per Category(The marketing data is not provided, so a marketing budget of 100000 is assumed as the annual marketing spend)"}]},
                {"label": "Revenue Distribution by Category", "method": "update", "args": [{"visible": [False] * (len(fig1.data) + len(fig2.data) + len(fig3.data)) + [True] * len(fig4.data)}, {"title": "Revenue Distribution by Category"}]},
            ],
            "direction": "down",
            "x": 0.16,
            "y": 1.19,
            "showactive": True,
        }
    ],
    title="Business Performance Dashboard",
    xaxis_title="Year",
    yaxis_title="Revenue",
    showlegend=True,
    legend_title_text="Product Category"
)

combined_fig.show()
