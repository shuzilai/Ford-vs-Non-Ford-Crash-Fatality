# Ford vs. Non-Ford Crash Fatality Analysis

**Claim:** Ford vehicles are often involved in the most fatal crashes. This analysis tests that claim using NHTSA crash data from 2016–2024.

## Summary
- **Main Question:** Is there a statistically significant relationship between driving a Ford and fatal accidents?
- **Data:** 57,207 crash records from the NHTSA Fatality Analysis Reporting System (FARS).
- **Method:** Data cleaning (removing unnecessary/missing fields) and logistic regression with predictors including vehicle occupants, licensing, injuries, vehicle age, gender, time of day, and Ford vs. non-Ford.
  
## Key Insights
- Ford fatality rate: 0.000051%
- Non-Ford fatality rate: 0.00002837%
- Logistic regression coefficient for FORD? = 0.59 (odds ratio ≈ 1.80) — suggests higher odds of fatal crashes for Ford vehicles, but **not statistically significant** (p = 0.235).
- Only time of day was significant: higher fatality odds at night.

## Limitations
- Many predictors not statistically significant.
- Omitted factors (vehicle type, speed, driver impairment) could influence results.
- Possible reverse causality (e.g., reputation or insurance effects on Ford ownership).

## Conclusion
We fail to reject the null hypothesis — there’s no statistically significant evidence that driving a Ford leads to higher fatal accident rates. However, omitted variables and reverse causality may still influence the outcome.

## Tools Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Microsoft Excel

## Author
Shu Zi Lai — Graduate Student in Business Analytics
