# ACC102 Board Game Complexity Explorer

## Project Overview

This project is an ACC102 Track 4 interactive data analysis tool that explores how board game complexity relates to user ratings and market popularity. The central question is whether more complex board games tend to receive higher ratings and stronger user engagement.

Rather than analysing complexity in isolation, the project evaluates its relationship with both perceived quality (rating) and market reach (ownership). The final output combines a Python-based analytical workflow with a Streamlit application, allowing users to explore the dataset dynamically instead of relying on static charts.

---

## Analytical Focus and Data Context

The analysis is built around two key relationships:

- the relationship between **complexity and rating**
- the relationship between **complexity and popularity**

This dual perspective is important because highly rated games are not always widely owned, and popular games are not necessarily complex. By analysing both dimensions together, the project provides a more realistic understanding of product performance.

The dataset is based on BoardGameGeek data obtained from Kaggle. It contains over 20,000 board games and includes variables such as complexity scores, user ratings, ownership counts, and gameplay characteristics. The data were originally collected in February 2021, last updated in May 2022, and accessed for this project in April 2026.

---

## Data Preparation and Cleaning

Before analysis, the notebook applies a structured data cleaning process to ensure consistency and reliability. Column names are standardised, missing values are examined, and rows with missing values in the core variables are removed. The `domains` column is dropped due to its high level of missing data, and duplicate entries are eliminated.

To improve robustness, the project also introduces additional treatments:

- a **trimmed mean (5%–95%)** to reduce the impact of extreme values  
- a **log transformation of popularity** to address heavy skewness  
- filtering to retain only key analytical variables  

After cleaning, the dataset is exported as `bgg_cleaned.csv`, which is directly used in the Streamlit application.

---

## Analytical Approach

The analysis combines descriptive exploration with relationship-based methods. Initial descriptive statistics provide an overview of the dataset, including medians, trimmed means, and grouped summaries. This step highlights the uneven distribution of board game popularity and user engagement.

The core analysis focuses on the relationship between complexity and rating. A scatter plot is used to visualise the distribution, and a correlation coefficient is calculated to quantify the strength of the relationship. The results show a moderate positive relationship, indicating that more complex games tend to receive higher ratings, although the effect is not strong enough to be predictive on its own.

The relationship between complexity and popularity is analysed separately. When popularity is measured using raw ownership counts, the correlation is extremely weak. Because ownership data is highly skewed, a log transformation is applied, which improves interpretability but still shows only a limited relationship. This confirms that popularity depends on many factors beyond complexity.

To improve interpretability further, games are grouped into complexity ranges. This grouped analysis shows that while higher complexity is associated with stronger ratings, popularity does not increase consistently. The conclusion is therefore more nuanced: complexity contributes to perceived quality, but does not guarantee market success.

---

## Streamlit Application

The Streamlit app transforms the analysis into an interactive product. Users can adjust filters such as complexity range, minimum rating, and minimum ownership, allowing them to explore different segments of the dataset based on their own preferences.

The app includes several key features:

- dynamic filtering through sidebar controls  
- real-time summary metrics (games, rating, complexity, ownership)  
- an interactive scatter plot  
- automatic statistical interpretation  
- a Top 10 popularity chart  
- an expandable data table  

The main visualisation is a scatter plot where:

- x-axis represents complexity  
- y-axis represents rating  
- bubble size represents popularity  
- colour represents complexity level  

A key enhancement in the updated version is the inclusion of an **OLS-based trendline**. This trendline provides a visual representation of the regression relationship, making it easier to identify the direction of the relationship. Together with the correlation coefficient calculated in real time, it strengthens the analytical credibility of the tool.

The app also generates an automatic interpretation of the correlation result, categorising the relationship as strong, moderate, or weak. This allows non-technical users to understand the meaning of the analysis without needing statistical knowledge.

---

## Key Insights

The project produces several important insights.

First, there is a moderate positive relationship between complexity and rating, suggesting that more complex games are often valued more highly by users. Second, the relationship between complexity and popularity is much weaker, indicating that complexity alone does not drive market adoption. Third, popularity is highly skewed, meaning that raw comparisons can be misleading and require transformation or careful interpretation.

Taken together, the findings suggest that the most practical strategy is not to maximise complexity, but to identify a balance. Moderate-to-high complexity games often achieve strong ratings while remaining accessible to a broader audience.

---

## How to Run the Project

To run the project locally, make sure the repository includes the notebook, the Streamlit application file, and the cleaned dataset. After installing the required packages, run the application using:

streamlit run app.py

The application will open in a browser window and can be used immediately.

## Requirements

The project relies on the following Python libraries:

- pandas  
- streamlit  
- plotly  
- numpy  
- matplotlib  
These can be installed using a requirements.txt file or directly via pip.

---

## Limitations and Future Improvements

Although the project provides useful insights, it has several limitations. The dataset is not real-time and may not reflect recent market trends. Popularity is approximated using ownership rather than actual sales or revenue, and the analysis focuses on correlation rather than causation.

Future improvements could include:

- adding more features such as game mechanics or genre  
- introducing formal regression outputs (e.g. coefficients and R²)  
- building a recommendation system  
- improving the user interface design  
- incorporating more recent data  

---

## Project Value

This project demonstrates a complete data workflow from problem definition to product development. By combining analysis with an interactive interface, it moves beyond a traditional notebook and becomes a practical tool for exploring user preferences and product performance.

---

## Demo

Add your Mediasite video link here.

---

## Reflection and AI Disclosure

A separate reflective report is submitted via LMO. AI tools were used to support language refinement and structure, while all analysis, logic, and outputs were independently reviewed and verified.
