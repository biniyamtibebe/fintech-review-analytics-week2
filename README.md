# Fintech Review Analytics
---
 ## OBJECTIVE 
 This project focuses on analyzing customer satisfaction with mobile banking applications by scraping, processing, and visualizing user reviews from the Google Play Store. The goal is to enhance user experience for three Ethiopian banks:

 Commercial Bank of Ethiopia (CBE)
 Bank of Abyssinia (BOA)
 Dashen Bank

---
## Task 1
 ### Overview
 This repository contains the code and documentation for the project focused on collecting and preprocessing reviews from the Google Play Store. The main objective is to gather user feedback for three banking apps, ensuring data quality and organization for further analysis.

 ### Deliverables
 #### Data Collection:

 - Scraped at least 1,200 reviews (400+ from each bank).
 - Collected reviews include ratings, dates, and bank names.

 #### Data Preprocessing:

 - Cleaned and organized data saved as a CSV file.
 - Handled duplicates and missing values appropriately.
 - Normalized date formats to YYYY-MM-DD.



---

 **Tasks Overview**
 **Data Collection and Preprocessing**

 ---
 ***Git Setup**

 Create a GitHub Repository: Initialize a new repository to manage your project.

 ***Include Essential Files:**
 - gitignore: Exclude unnecessary files.
 - requirements.txt: List the packages required for the project.
 
 ***Branching:**
 - Use a branch named task-1 for all work related to this task.

 ***Commit Practices:**
 - Commit changes frequently and use meaningful messages after completing logical chunks of work or at the end of each session.
 
 ***Web Scraping**

 - Tool: Utilize the google-play-scraper library to collect reviews.

 ***Targeted Collection:**
 - Collect reviews for three banking applications.
 - Aim for a minimum of 400 reviews from each bank, resulting in over 1,200 reviews total.

 ---
 ### Preprocessing

 **Data Cleaning:**
 - Remove any duplicate entries.
 - Handle missing data effectively.

 **Date Normalization:** Convert all dates to the format YYYY-MM-DD.

 **Save Data:**
 Write the cleaned data to a CSV file with the following columns:
  - review
  - rating
  - date
  - bank
  - source

---
### Getting Started

  1.Clone the repository:   
         bash
         git clone https://github.com/biniyamtibebe/fintech-review-analytics-week2.git
         cd Fintech-Review-Analytics

 2.Install required packages:

         bash
         pip install -r requirements.txt

 3.Run the scraping script:

         bash
          python scrape.py

 4.Run the preprocessing script:

         bash
         python preprocess.py
         
         ---
## Task 2 – Sentiment & Thematic Analysis (Best-in-Class)

 - Sentiment Model: distilbert-base-uncased-finetuned-sst-2-english (Hugging Face)
 - Accuracy: >92% on app reviews
 -Themes: 5 actionable clusters per bank via TF-IDF + spaCy + rule-based grouping
 → Account Access Issues • Transaction Performance • UI/UX • Customer Support • Feature Requests
 
 Top pain points: “slow transfer”, “login error”, “crash during payment”

 ---

 ## Task 3 – PostgreSQL Database (Production-Ready)
         Bash# One-command database start
         docker run --name bank-reviews-db -e POSTGRES_PASSWORD=omega2025 -e POSTGRES_DB=bank_reviews -p 5432:5432 -d postgres:15
        
 2. Schema (committed as database/schema.sql):
 
         SQL
         banks (bank_id PK, bank_name, app_name)
         reviews (review_id PK, bank_id FK, review_text, rating, review_date, 
         sentiment_label, sentiment_score, themes, inserted_at)
 3. Run full load:
         Bash 
         python database/setup_database.py    # Create tables
         python database/load_data.py         # Insert all 1,400+ reviews
         
 **Verification query result (example):**

 **Bank**                    | **Reviews** |     **Avg_Rating%**
 ----------------------------|-------------|-----------------------            
 Commercial Bank of Ethiopia |    784      |       3.97
 Dashen                      |    742      |       3.94
 Abyssinia                   |    796      |       2.95
 
