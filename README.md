# IPL-Winner-Prediction

This ML project predictS the winner of an IPL match based on match context such as the teams, venue, toss details, and more.

The system is trained on real IPL match data and enables users to interactively select match conditions to receive winner predictions with a confidence score.

## Working

1. **Data Source**  
   Uses two datasets:
   - `matches.csv`: match-level summaries from past IPL seasons
   - `deliveries.csv`: ball-by-ball data used to compute team-level stats 

2. **Model Training**  
   A `RandomForestClassifier` is trained to predict which team wins

3. **Interactive Prediction**  
   A CLI lets the user choose:
   - Any season (past or future)
   - Team 1 and Team 2
   - Venue
   - Toss winner and toss decision  
   
   The system then predicts the winner




