reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."]

keywords = ["good", "excellent", "bad", "poor", "average"]

def review_keywords(reviews, keywords):
    if len(reviews) > 0:
        word = reviews.find(keywords)
        if word > 0:
            return reviews.upper()
        else:
            print("No keywords were found. ")
    else:
        print("Please enter a review you would like to search. ")

    while True:
        review_input = input("Enter a review you would like to search ")
        word_input = input("Enter a word you would like to search for. ")

        result = review_keywords(review_input, word_input)
        print(result)

        continue_search = input("Would you like to search more review? (yes/no) ").lower()
        if continue_search != 'yes':
            break


def postive_negative(review):
    positive_count = 0
    negative_count = 0

    words = review.lower().split()
    
    # Count the number of positive and negative words in the review
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
            
    print(f"This is positive count {positive_count}. This is negative count {negative_count}")

    while True:
        review_input = input("Enter a review you would like to search ")
        positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
        negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
        result = postive_negative(review_input)
        print(result)

        continue_search = input("Would you like to search more review? (yes/no) ").lower()
        if continue_search != 'yes':
            break


# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

# def summary(review):

review_new = "I had a bad experience with this product. It didn't meet my expectations."

# words = review_new.split( )
# for word in words:
#     letters = word.split(' , ')
#     print(len(letters))

index = review_new.find[29] 
print(index)
        


# print(letters)