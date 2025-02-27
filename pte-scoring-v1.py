def calculate_pte_score(original_sentence, my_sentence):
    """
    Calculate the PTE score for Write from Dictation task.

    Args:
        original_sentence (str): The original dictation sentence
        my_sentence (str): The user's written response

    Returns:
        float: Percentage score (0-100)
    """
    # Tokenize sentences to words, convert to lowercase, and remove punctuation
    original_words = [
        word.strip(".,?!:;()[]{}\"'-").lower() for word in original_sentence.split()
    ]
    my_words = [word.strip(".,?!:;()[]{}\"'-").lower() for word in my_sentence.split()]

    # Remove empty strings that might result from stripping punctuation
    original_words = [word for word in original_words if word]
    my_words = [word for word in my_words if word]

    # Count the total number of words in the original sentence
    total_words = len(original_words)

    # Create copies of word lists for processing
    orig_words_remaining = original_words.copy()
    my_words_remaining = my_words.copy()

    # Count matched words
    matched_words = 0

    # First pass: Match exact words in the correct positions
    for i in range(min(len(orig_words_remaining), len(my_words_remaining))):
        if i < len(orig_words_remaining) and i < len(my_words_remaining):
            if orig_words_remaining[i] == my_words_remaining[i]:
                matched_words += 1
                orig_words_remaining[i] = None
                my_words_remaining[i] = None

    # Clean up the remaining lists
    orig_words_remaining = [word for word in orig_words_remaining if word is not None]
    my_words_remaining = [word for word in my_words_remaining if word is not None]

    # Second pass: Match words regardless of position
    for my_word in my_words_remaining[:]:
        if my_word in orig_words_remaining:
            matched_words += 1
            orig_words_remaining.remove(my_word)
            my_words_remaining.remove(my_word)

    # Calculate the percentage score
    score = (matched_words / total_words) * 100

    # Special case handling for up to 3 incorrect words but high match rate
    # Based on examples 1 and 5, where duplicates and small additions still score 100%
    if (total_words - matched_words) <= 3 and matched_words >= total_words:
        score = 100.0

    return round(score)


# Test with provided examples
def test_examples():
    examples = [
        {
            "original": "Our group is meeting tomorrow in the library conference room.",
            "response": "Our group is meeting tomorrow in a the library library's conference room.",
            "expected_score": 100,
        },
        {
            "original": "An aerial photograph was promptly registered for thorough evaluation.",
            "response": "An area ariel photograph was evaluated for the valuation.",
            "expected_score": 44,
        },
        {
            "original": "An aerial photograph was promptly registered for thorough evaluation.",
            "response": "An aerial photograph was thorough thoroughly prompted for the evaluation.",
            "expected_score": 67,
        },
        {
            "original": "Undergraduates may pursue specific interests within certificate programs.",
            "response": "Undergraduates undergraduate may pursue different certificates within specific programs.",
            "expected_score": 63,
        },
        {
            "original": "She used to be an editor of the student newspaper.",
            "response": "She used to be an editor of a the student student's newspaper.",
            "expected_score": 100,
        },
        {
            "original": "The toughest part of postgraduate education is the funding.",
            "response": "The toughest part parts of the education is the funding.",
            "expected_score": 89,
        },
    ]

    for i, example in enumerate(examples, 1):
        score = calculate_pte_score(example["original"], example["response"])
        print(f"Example {i}:")
        print(f"Original: {example['original']}")
        print(f"Response: {example['response']}")
        print(f"Calculated Score: {score}%")
        print(f"Expected Score: {example['expected_score']}%")
        print(f"Match: {'✓' if score == example['expected_score'] else '✗'}")
        print("-" * 50)


# For individual testing
def main():
    print("PTE Write from Dictation Scoring Calculator")
    print("-" * 50)

    while True:
        original = input("Enter the original sentence (or 'q' to quit): ")
        if original.lower() == "q":
            break

        my_response = input("Enter your response: ")

        score = calculate_pte_score(original, my_response)
        print(f"Your score: {score}%")
        print("-" * 50)


if __name__ == "__main__":
    # Uncomment to test all examples
    test_examples()

    # Uncomment to use interactive mode
    # main()
