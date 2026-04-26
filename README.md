# ACC102 Board Game Complexity Explorer

## Project Overview

This project is an ACC102 Track 4 interactive data analysis tool. It explores how board game complexity relates to user ratings and market popularity.

The central question is whether more complex board games tend to receive higher ratings and stronger user engagement. The project does not analyse complexity alone. It also considers rating and ownership, because a highly rated game is not always widely owned, and a popular game is not always complex.

The final product combines a Python notebook with a local Streamlit application. The notebook shows the full analytical workflow, while the Streamlit app allows users to explore the results interactively.

## Target Users

The intended users are:

- board game buyers
- casual players
- game designers

The tool helps these users compare games based on complexity, rating, and popularity. It also provides recommendations based on different user goals.

## Dataset

The dataset is based on BoardGameGeek data obtained from Kaggle. It contains over 20,000 board games and includes variables such as:

- game name
- year published
- player numbers
- playing time
- average rating
- average complexity
- owned users

The data were originally collected in February 2021, last updated in May 2022, and accessed for this project in April 2026.

After cleaning, the dataset is saved as `bgg_cleaned.csv`, which is used by the Streamlit app.

## Python Workflow

The notebook includes the following workflow:

1. Load and inspect the dataset
2. Standardise column names
3. Check missing values
4. Remove duplicate records
5. Drop columns with serious missingness
6. Select key analytical variables
7. Produce descriptive statistics
8. Apply 5%–95% trimmed mean treatment
9. Apply log transformation to popularity
10. Analyse relationships between complexity, rating, and owned users
11. Create charts and grouped summaries
12. Export the cleaned dataset for the Streamlit app

## Main Analysis

The analysis focuses on two main relationships:

1. Complexity and rating
2. Complexity and popularity

The project uses descriptive statistics, scatter plots, correlation analysis, grouped comparisons, and visualisations.

The main finding is that complexity has a moderate positive relationship with rating, but it does not automatically lead to mass popularity. This suggests that complexity may improve perceived quality among experienced players, but it can also reduce accessibility for casual users.

## Streamlit App Features

The Streamlit app includes:

- sidebar filters for complexity range, minimum rating, and minimum owned users
- real-time summary metrics
- an interactive complexity-rating scatter plot
- an OLS trendline
- automatic interpretation of the correlation result
- a recommendation section
- a Top 10 owned games bar chart
- an expandable filtered data table

The recommendation section allows users to choose one of four goals:

- Balanced Choice
- Highest Rated
- Most Popular
- Lower Complexity

The app then ranks games using rating, owned users, and complexity.

## Repository Structure

```text
ACC102-Board-Game-Complexity-Explorer/
├── app.py
├── Board Game.ipynb
├── bgg_cleaned.csv
├── BGG_Data_Set.csv
├── README.md
└── requirements.txt

```

## How to Run the App Locally

This project is designed to run as a local Streamlit app.

First, clone or download this repository. Then open Terminal or Command Prompt inside the project folder that contains `app.py`.

Install the required packages:


```bash
pip install -r requirements.txt
```

After installation, run the app with:

```bash
streamlit run app.py
```

The app will open locally in a browser window, usually at:

```text
http://localhost:8501
```

If the browser does not open automatically, copy the local URL shown in the terminal and paste it into your browser.

## Required Files

To run the app successfully, make sure these files are in the same repository folder:

- `app.py`
- `bgg_cleaned.csv`
- `requirements.txt`
  
`BGG_Data_Set.csv` is the original dataset used.

The file `bgg_cleaned.csv` must be in the same folder as `app.py`, because the app reads it directly using a relative file path.

## Demo Video

The demo video is submitted separately through Mediasite on LMO.

## Limitations and Future Improvements

This project has several limitations. BoardGameGeek users may not represent all board game consumers, because they are usually more interested in board games than average buyers. Also, owned users is only a proxy for popularity. It does not directly measure sales, revenue, or current market demand. The analysis shows association rather than causation.

Future improvements could include:

- adding game category, mechanics, or publisher information
- using more recent data
- adding price or sales data
- using user review text for sentiment analysis
- allowing users to customise recommendation weights

## Project Value

This project demonstrates a complete data workflow from problem definition to product development. It uses Python for cleaning, transformation, analysis, visualisation, and interactive product design. The Streamlit app adds user value by helping users move from data exploration to practical game recommendations.

## Reflection and AI Disclosure

A separate reflective report is submitted through LMO. The AI disclosure is included at the end of the reflective report.
