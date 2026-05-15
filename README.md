# Göksu Arslan DSA210 Project

**1. Motivation**

The main motivation of this project is to analyze how different traffic-related factors influence travel duration and to evaluate the accuracy of estimated travel times using real-life driving data. In addition, the project aims to predict travel duration using basic machine learning models and data science techniques.
   
**2. Data Collection**

The dataset used in this project was collected manually from real-life driving experiences between April 1 and April 14. The trips were made by the author, family members, and friends under different traffic conditions and routes.

For each trip, several variables were recorded, including:
* Departure and arrival times
* Actual travel duration
* Estimated travel duration from Google Maps
* Distance
* Number of traffic lights
* Traffic level

The dataset consists of 127 observations, where each row represents a single trip and each column corresponds to a specific variable.

The collected data is suitable for exploratory data analysis, statistical testing, and machine learning applications related to travel duration prediction.

**3. Project Outline**

The project analysis followed several stages including:
  1. Data preprocessing & Exploratory Data Analysis (EDA)
  3. Hypothesis testing
  4. Machine learning modeling

**4. Exploratory Data Analysis**

Initially, the dataset was cleaned and transformed into a suitable format for analysis.

Time-related variables were converted into datetime format and travel durations were standardized into minutes. Additional variables such as delay and rush hour indicators were also created.

* Delay: difference between estimated and actual duration
* Rush hour: binary variable representing peak traffic hours
  
After preprocessing, several visualization and analysis techniques were applied to better understand the dataset. The EDA process included:
* Histogram analysis
* Scatter plots
* Boxplots
* Correlation analysis
* Traffic-level based comparisons

Histograms were used to examine the distributions of actual travel duration and delay values. Scatter plots were created to analyze relationships between variables such as distance and travel duration. Boxplots were used to compare travel duration across different traffic levels and rush hour conditions. Correlation analysis was also performed to investigate the relationships between numerical variables.

Several statistical hypothesis tests were conducted to validate the observed relationships within the dataset. The following tests were applied on specified topics:
* Independent T-Test. Rush hour vs non-rush hour effects
* ANOVA Test: Traffic level differences
* Paired T-Test: Estimated vs actual travel durations
* Pearson Correlation Test: Correlation between distance and travel duration
* One-Sample T-Test: Delay behavior

**5. Machine Learning and Model Evaluation**

Several machine learning models were implemented to predict actual travel duration. The following models were applied:
* Linear Regression
* Random Forest Regressor
* K-Nearest Neighbors (KNN)
* Decision Tree Regressor

The models were trained using variables such as:
* Distance
* Traffic level
* Estimated duration
* Number of traffic lights
* Rush hour information
  
Model performances were evaluated using:
* MAE
* RMSE
* R² score

A comparison table of model perfomance:

<img width="660" height="173" alt="image" src="https://github.com/user-attachments/assets/75280b15-bd6d-4cd6-abdc-53f01a476072" />

**6. Findings**

The analysis revealed several important findings regarding travel duration and traffic behavior.
* Actual travel duration showed a right-skewed distribution, meaning that most trips were relatively short while a few trips lasted significantly longer.
* Delay values were generally centered around zero, indicating that estimated travel times were usually close to actual travel durations.
* A strong positive correlation (≈ 0.89) was observed between distance and actual travel duration.
* Estimated travel duration and actual travel duration showed a very strong relationship (≈ 0.97), demonstrating the reliability of Google Maps estimations.
* Traffic level significantly affected travel duration, while rush hour alone did not show a statistically significant impact.
* Trips under medium and high traffic conditions had noticeably longer and more variable travel durations compared to low traffic conditions.
* The number of traffic lights showed only a weak relationship with travel duration.
* Delay analysis showed slight overestimation during low traffic conditions and slight underestimation during medium and high traffic conditions.

Machine learning results also showed strong predictive performance:
* Linear Regression achieved the best overall performance with an R² score of 0.914.
* Random Forest produced a very similar performance with an R² score of 0.909.
* KNN also generated strong prediction results with an R² value close to 0.90.
* Decision Tree showed the weakest performance with an R² score of 0.784.

Overall, the results demonstrate that travel duration can be predicted successfully using simple transportation-related variables.

**7. Limitations and Future Work**

One of the main limitations of this study is the relatively small dataset size collected over a limited time period. Since the data was self-collected, it may also reflect specific driving habits and geographic conditions.

Additionally, the project focused on a limited number of variables. Factors such as weather conditions, accidents, road quality, and real-time traffic incidents were not included in the analysis.

For future work:
* The dataset can be expanded over longer periods
* Additional transportation variables can be integrated
* A real-time travel duration prediction dashboard can be developed



