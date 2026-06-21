import pandas as pd

# Load messages
df = pd.read_csv("../data/sample_messages.csv")

annotations = []

print("\nAI Data Annotation Tool")
print("-" * 40)

for _, row in df.iterrows():

    print(f"\nMessage ID: {row['id']}")
    print(f"Message: {row['message']}")

    intent = input(
        "Intent (Billing/Technical/Account/Other): "
    )

    sentiment = input(
        "Sentiment (Positive/Neutral/Negative): "
    )

    pii = input(
        "Contains PII? (Yes/No): "
    )

    annotations.append({
        "id": row["id"],
        "message": row["message"],
        "intent": intent,
        "sentiment": sentiment,
        "pii_flag": pii
    })

output_df = pd.DataFrame(annotations)

output_df.to_csv(
    "../outputs/labeled_data.csv",
    index=False
)

print("\nAnnotations saved successfully.")
