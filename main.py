from src.preprocess import load_and_prepare_data
from src.model import train_model
from src.predict import predict_winner
from utils.helpers import save_model

def choose_option(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    idx = int(input("Enter the number of your choice: ")) - 1
    return options[idx]

def main():
    print("Loading IPL data from local CSVs...")
    df = load_and_prepare_data()

    print("Training prediction model...")
    model, encoder = train_model(df)
    save_model(model, encoder)

    teams = [
        "Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore",
        "Kolkata Knight Riders", "Sunrisers Hyderabad", "Delhi Capitals",
        "Rajasthan Royals", "Punjab Kings", "Lucknow Super Giants", "Gujarat Titans"
    ]

    venues = [
        "Wankhede Stadium", "M. A. Chidambaram Stadium", "M. Chinnaswamy Stadium",
        "Arun Jaitley Stadium", "Eden Gardens", "Rajiv Gandhi Intl. Stadium",
        "Narendra Modi Stadium", "Sawai Mansingh Stadium",
        "IS Bindra Stadium", "BRSABV Ekana Stadium"
    ]

    toss_options = ["bat", "field"]

    print("\nPredict Your Match Outcome!")

 
    season = input("Enter the IPL Season Year (e.g., 2025): ").strip()

    team1 = choose_option("Select Team 1:", teams)
    team2 = choose_option("Select Team 2:", [t for t in teams if t != team1])
    venue = choose_option("Select Venue:", venues)
    toss_winner = choose_option("Select Toss Winner:", [team1, team2])
    toss_decision = choose_option("Select Toss Decision:", toss_options)

    print("\nMaking Prediction...")
    user_input = {
        "season": season,
        "venue": venue,
        "team1": team1,
        "team2": team2,
        "toss_winner": toss_winner,
        "toss_decision": toss_decision
    }

    predict_winner(user_input, model, encoder)

if __name__ == "__main__":
    main()
