from ai_service import summarise, sentiment

print("=== Voice AI Pipeline ===")

transcript = input("\nPaste call transcript:\n")

summary = summarise(transcript)
score = sentiment(transcript)

print("\n--- SUMMARY ---")
print(summary)

print("\n--- SENTIMENT SCORE ---")
print(score)

if score > 0:
    print("Positive conversation")
elif score < 0:
    print("Negative conversation")
else:
    print("Neutral conversation")