import os
from dotenv import load_dotenv
from groq import Groq  # Switched from OpenAI to Groq

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_story(theme, genre):
    print("\n✍️ The AI is writing your story... please wait...\n")

    try:
        prompt = f"Write a {genre} story based on the theme: {theme}. Make it engaging and creative."

        # Groq uses the same 'chat.completions.create' syntax!
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # A very powerful free model
            messages=[
                {"role": "system", "content": "You are a creative storyteller."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )

        story = response.choices[0].message.content.strip()
        return story
    except Exception as e:
        print(f"Error generating story: {e}")
        return "Sorry, I couldn't generate a story at the moment."

# ... (Keep the rest of your user input and file saving logic the same)

# Main function to run the story generator
print("Welcome to the AI Story Generator!")
user_theme = input(
    "Enter a theme for your story (e.g., love, adventure, mystery): ")
user_genre = input(
    "Enter a genre for your story (e.g., fantasy, sci-fi, horror): ")

generated_story = generate_story(user_theme, user_genre)
print("\n📖 Here is your generated story:\n")
print(generated_story)

# 3. Save the generated story to a text file
with open("generated_story.txt", "w", encoding="utf-8") as file:
    file.write(generated_story)
print("\n✅ Your story has been saved to 'generated_story.txt'")
