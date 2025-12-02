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
### 1.Review Volume & Average Rating

| Bank                            | Review Count | Avg. Rating |
| ------------------------------- | ------------ | ----------- |
| **Bank of Abyssinia**           | 796          | **2.95**    |
| **Commercial Bank of Ethiopia** | 784          | **3.97**    |
| **Dashen Bank**                 | 742          | **3.94**    |

**Insights**
- CBE and Dashen outperform BOA in both ratings and sentiment.
- BOA has the most reviews, but also the lowest overall rating, signaling higher user dissatisfaction.
- CBE holds the best rating (3.97), indicating relatively better user perception.

---
### 2. Sentiment Distribution Across Banks
**Sentiment Counts**
From the SQL output:
| Bank       | Positive | Neutral | Negative |
| ---------- | -------- | ------- | -------- |
| **CBE**    | 476      | 2       | 306      |
| **BOA**    | 336      | 2       | 458      |
| **Dashen** | 468      | 8       | 266      |

**Insights**
- BOA has the highest number of negative reviews (458) despite having strong positive mentions (336). The imbalance suggests broad and persistent dissatisfaction.
- CBE shows a positive-to-negative ratio of 476:306, better than BOA but still with considerable negative sentiment.
- Dashen Bank demonstrates the healthiest sentiment balance, with more positive (468) and fewer negative mentions (266).

This shows Dashen Bank users express the highest net positivity, while BOA faces the most frustration.

---
### 3. Review Text Examples (Highly Negative)
Several extremely negative reviews share common patterns:
- Severe app crashes (“literally crashes every month”)
- Poor performance or slow responses (“very slow”)
- Access issues (“I can't access it properly”)
- User frustration (“worst app on the planet”)
- Frequent complaints about **CBE** and **BOA** apps

The sentiment scores (near –0.9998) indicate these texts are among the strongest negative outliers, often containing emotionally charged language.

---

### 4. Thematic Analysis Across Banks
**Key Themes Identified**
From the heatmap:
| Theme                          | BOA | CBE | Dashen |
| ------------------------------ | --- | --- | ------ |
| **Other (general complaints)** | 336 | 354 | 294    |
| **Transaction Performance**    | 40  | 16  | 29     |
| **UI & UX**                    | 18  | 13  | 30     |
| **Account Access Issues**      | 13  | 12  | 23     |
| **Feature Requests**           | 7   | 6   | 14     |
| **Customer Support**           | 7   | 3   | 7      |

**Insights from the Theme Heatmap**

1️⃣ General complaints dominate across all banks

 - The largest category is "Other", indicating many              comments describe overall dissatisfaction, instability, or general  frustration without fitting into narrow categories.
 - CBE has the most “general complaints,” but BOA is close behind.

2️⃣ BOA leads in transaction-related complaints

 - BOA has the highest transaction-related issues (40).
 - Complaints often relate to:
    - Payment failures
    - Delayed transactions
    - App errors during transfers

3️⃣ Dashen leads in UI/UX and access issues
 - Dashen has noticeably more UI/UX-related complaints, indicating users care about visual design and navigation.
 - Dashen also has higher account access problems, signaling login/session stability concerns.

4️⃣ Feature requests are low overall

  - Users of all three apps rarely ask for new features—indicating users are more concerned with stability, speed, and reliability than new functionality.
  
  ---
### 5. Comparative Insights: Which App Performs Best?

**Best App overall: Dashen Bank**
 - Strong positive sentiment (468)
 - Lowest negative sentiment ratio
 - Good average rating (3.94)
 - Complaints mostly relate to UX/access—not fundamental functionality

**Most Polarizing App: Commercial Bank of Ethiopia**

 - Highest positive (476) but also high negative (306)
 - High review volume and strong ratings, but stability issues persist

**Most Problematic App: Bank of Abyssinia**
 - Lowest average rating (2.95)
 - Most negative reviews (458) overall
 - Largest number of transaction-related complaints
 - Strong user frustration in sample reviews

---
### 6. High-Level Conclusions

#### 1.Performance & Reliability
   All banks face severe user frustration over app reliability. Transaction-related issues are particularly prominent for BOA.

#### 2.User Interface (UI/UX)
   Dashen users complain more about UX issues—suggesting Dashen  should focus on improving interface consistency and usability.

#### 3.App Stability & Access
Frequent mentions across all banks highlight:
   - Login issues
   - Slow loading
   - App crashes

#### 4.Customer Support Mentions Low
  Users seem more focused on operational issues rather than support interactions.

#### 5.Sentiment strongly correlates with rating
  BOA’s frustration-heavy text reflects its low average rating.

  ---
### 7. Recommendations Per Bank
**Bank of Abyssinia (Most critical improvements needed)**
 - Prioritize app stability and crash reduction
 - Improve transaction reliability
 - Investigate major recurring negative triggers (“slow,” “worst app,” “can’t access”)
 - Consider redesigning core architecture

**Commercial Bank of Ethiopia**
 - Address crashes during payments
 - Improve error-handling messages
 - Conduct performance tuning for peak hours
 - Improve onboarding & login flow
 
**Dashen Bank**
 - Main focus: UI/UX redesign and navigation clarity
 - Fix login instability and account access issues
 - Strengthen design consistency and user flows

 --- 

### 📌 Final Summary
 - Dashen Bank performs best overall.
 - CBE is strong but suffers from reliability issues.
 - BOA requires urgent improvement in performance and stability.
 - Users across all banks experience frustration with access, performance, and speed, overshadowing feature-related requests.