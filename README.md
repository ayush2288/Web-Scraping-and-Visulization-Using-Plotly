Here’s a GitHub-friendly **README.md** file format for your project, using markdown syntax (`#`, `*`, `**`) for proper rendering on GitHub.

---

# **Practical Automation and Data Handling**

### **Objective**
Complete two tasks:
1. Build a web scraping tool.
2. Automate a KPI dashboard for data visualization.

---

## **1. Web Scraping**

### **Features**
- Automates web scraping using Selenium.
- Extracts and processes data into CSV files.

### **Requirements**
- Python
- Selenium
- WebDriver (e.g., ChromeDriver)

### **Installation**
1. Ensure `web_scraper.py` is downloaded from this repository.
2. Install the required dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```
3. Run the script:
   ```bash
   python web_scraper.py
   ```

---

## **2. Data Visualization with Plotly**

### **Features**
- Generates visualizations for KPI analysis.
- Includes revenue, AOV, ROMS, and revenue distribution insights.

### **Requirements**
- Python
- Plotly
- Pandas

### **Installation**
1. Download `kpi_dashboard.py` from this repository.
2. Install the required dependencies:
   ```bash
   pip install plotly pandas
   ```
3. Run the script:
   ```bash
   python kpi_dashboard.py
   ```

---

## **Data Sources**
- **Scraped Data**: [Scraped data from Noon.com](https://docs.google.com/spreadsheets/d/1eAJN1HEAf4BFrYAx7BDOtcQ3t5t09Rna7wPDdjBX0uI/edit?usp=sharing)

---

### **Key Insights**

#### **1. Annual Revenue by Category**
- **Clothing**: Largest revenue contributor, rising from ~320k in 2020 to ~360k in 2023.
- **Home & Kitchen**: Second largest, increasing from ~270k in 2020 to ~320k in 2023.
- **Electronics**: Third largest, increasing from ~220k in 2020 to ~270k in 2023.
- Steady growth in total revenue from ~820.5k in 2020 to ~841.6k in 2023.
  ![Screenshot (998)](https://github.com/user-attachments/assets/b372f4d2-7707-497d-8474-c8af0436b8c2)

  

#### **2. Average Order Value (AOV) per Category**
- **Electronics**: Highest AOV, increasing from ~241 in 2020 to ~250 in 2023.
- **Home & Kitchen**: Second highest, ranging between ~225 and ~235.
- Slight increase in AOV across all categories, indicating higher customer spending.
  ![Screenshot (999)](https://github.com/user-attachments/assets/05167283-8e3f-4b13-a1ee-2a2ed4b63cd7)


#### **3. Return on Marketing Spend (ROMS) per Category**
- **Home & Kitchen**: Highest ROMS, reaching ~8.5 in 2023.
- **Sports**: Second highest, increasing to ~8 in 2023.
- Overall ROMS trend indicates more efficient marketing over time.
![Screenshot (1001)](https://github.com/user-attachments/assets/6a980a15-b690-4b30-9b8d-7f4fb68f9194)


#### **4. Revenue Distribution by Category**
- **Clothing**: Largest revenue contributor, accounting for 20.5% in 2022.
- **Home & Kitchen**: Second largest, with 20.2% share in 2022.
- Steady growth across all categories from 2020 to 2023.
![Screenshot (1002)](https://github.com/user-attachments/assets/2003f454-de81-46cd-8f7d-dbc930954398)

