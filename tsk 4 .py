class ContentBasedRecommendationSystem:
    def __init__(self):
        # Database of items with their attributes
        self.items = {
            'Movie1': ['Action', 'Adventure', 'Sci-Fi'],
            'Movie2': ['Drama', 'Romance'],
            'Movie3': ['Action', 'Comedy'],
            'Movie4': ['Drama', 'Thriller'],
            'Movie5': ['Comedy', 'Romance'],
            'Book1': ['Mystery', 'Thriller'],
            'Book2': ['Romance', 'Fiction'],
            'Book3': ['Science', 'Non-Fiction'],
            'Book4': ['Mystery', 'Crime'],
            'Book5': ['Fantasy', 'Adventure'],
            'Product1': ['Electronics', 'Gadgets'],
            'Product2': ['Clothing', 'Fashion'],
            'Product3': ['Home', 'Appliances'],
            'Product4': ['Health', 'Wellness'],
            'Product5': ['Toys', 'Games']
        }

    def display_available_items(self, item_type):
        if item_type in ['movie', 'book', 'product']:
            print(f"Available {item_type}s:")
            for item in self.items:
                if item_type in item.lower():
                    print(item)

            print("HERE ARE MY RECOMMENDATION OF MOVIES, BOOKS, AND PRODUCTS.")
            print("HERE ARE THE MOVIES:")
            print("JHON WICK, ZERO, RAONE, ANIMAL, JAWAN")
            print("HERE ARE THE BOOKS:")
            print("SEPTOLOGY, MELANCHOLY, MORGAN OG, THE ARCHIES, ADVENTURE TIME")
            print("HERE ARE THE PRODUCTS:")
            print("APPLE, SAMSUNG, MICROMAX, REDMI")

    def get_user_preferences(self):
        user_input = input("Enter the type of item you are interested in (Movie, Book, Product): ").lower()

        if user_input not in ['movie', 'book', 'product']:
            print("Invalid input. Please enter 'Movie', 'Book', or 'Product'.")
            return []

        self.display_available_items(user_input)

        user_input_name = input(f"Enter the name of a {user_input}: ")
        user_preferences = self.items.get(user_input_name, [])
        return user_preferences, user_input

    def recommend_items(self, user_preferences, item_type, num_recommendations=5):
        similarity_scores = {}
        for item, attributes in self.items.items():
            if item_type in item.lower():
                common_attributes = set(attributes) & set(user_preferences)
                similarity_score = len(common_attributes)
                similarity_scores[item] = similarity_score

        recommended_items = sorted(similarity_scores, key=similarity_scores.get, reverse=True)[:num_recommendations]

        return recommended_items

def main():
    recommendation_system = ContentBasedRecommendationSystem()

    user_preferences, item_type = recommendation_system.get_user_preferences()

    if user_preferences:
        recommended_items = recommendation_system.recommend_items(user_preferences, item_type, num_recommendations=7)

        print(f"Recommended {item_type}s:")
        for item in recommended_items:
            print(item)
    else:
        print("No recommendations found for the given input.")

if __name__ == "__main__":
    main()
