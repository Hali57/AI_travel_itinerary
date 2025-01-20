import json
import random
from datetime import datetime, timedelta

# Define our static lists
cities = {
    "Nairobi": {
        "activities": {
            "Morning": [
                "Visit Nairobi National Park",
                "Walk in Karura Forest"
            ],
            "Afternoon": [
                "Lunch at a local restaurant",
                "Visit David Sheldrick Wildlife Trust"
            ],
            "Evening": [
                "Experience Nairobi Nightlife at The Alchemist Bar",
                "Explore local art galleries"
            ]
        }
    },
    "Mombasa": {
        "activities": {
            "Morning": [
                "Visit Fort Jesus",
                "Explore Old Town"
            ],
            "Afternoon": [
                "Lunch at a seaside restaurant",
                "Take a guided historical tour"
            ],
            "Evening": [
                "Beach walk and Swahili dinner",
                "Visit a local music venue"
            ]
        }
    },
    "Kwale": {
        "activities": {
            "Morning": [
                "Relax at Diani Beach",
                "Morning yoga by the sea"
            ],
            "Afternoon": [
                "Local cultural market tour",
                "Visit a hidden coastal gem"
            ],
            "Evening": [
                "Sunset at the beach",
                "Enjoy a quiet seaside dinner"
            ]
        }
    }
}

budget_tags = ["Low", "Medium", "High"]

# Placeholder image URLs dictionary (you can later integrate with Unsplash API if needed)
image_urls = {
    "Nairobi": {
        "Nightlife": [
            "https://unsplash.com/photos/nairobi_nightlife1",
            "https://unsplash.com/photos/nairobi_nightlife2"
        ],
        "Default": [
            "https://unsplash.com/photos/nairobi_default1"
        ]
    },
    "Mombasa": {
        "Default": [
            "https://unsplash.com/photos/mombasa_default1"
        ]
    },
    "Kwale": {
        "Diani": [
            "https://unsplash.com/photos/diani1",
            "https://unsplash.com/photos/diani2"
        ],
        "Default": [
            "https://unsplash.com/photos/kwale_default1"
        ]
    }
}

def generate_itinerary(city, date):
    itinerary = []
    for time_slot in ["Morning", "Afternoon", "Evening"]:
        # Select a random activity for the time slot
        activity_list = cities[city]["activities"][time_slot]
        activity = random.choice(activity_list)
        
        # Randomly assign a duration and budget tag
        duration = f"{random.randint(1, 4)}h"
        budget = random.choice(budget_tags)
        
        # Select images: prioritize special image sets (e.g., Diani for Kwale, Nightlife for Nairobi Evening)
        if city == "Kwale" and time_slot == "Morning" and "Diani" in activity:
            images = image_urls[city]["Diani"]
        elif city == "Nairobi" and time_slot == "Evening" and "Nightlife" in activity:
            images = image_urls[city]["Nightlife"]
        else:
            images = image_urls[city].get("Default", [])
        
        itinerary.append({
            "time": time_slot,
            "activity": activity,
            "duration": duration,
            "budget": budget,
            "images": images
        })
    
    return {
        "city": city,
        "date": date.strftime("%Y-%m-%d"),
        "itinerary": itinerary,
        "preview": True
    }

def simulate_data(num_days=5):
    data = []
    # Let's simulate itineraries for the next 'num_days' for each city
    base_date = datetime.now()
    for city in cities:
        for i in range(num_days):
            day_date = base_date + timedelta(days=i)
            itinerary = generate_itinerary(city, day_date)
            data.append(itinerary)
    return data

if __name__ == "__main__":
    simulated_data = simulate_data(num_days=3)  # generate 3 days of itineraries per city
    # Save to JSON file
    with open("simulated_itineraries.json", "w") as outfile:
        json.dump(simulated_data, outfile, indent=2)
    
    print("Data simulation complete. Check simulated_itineraries.json")
