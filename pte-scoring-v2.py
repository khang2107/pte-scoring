def calculate_pte_score(original_sentence, my_sentence):
    """
    Calculate the PTE score for Write from Dictation task.

    Args:
        original_sentence (str): The original dictation sentence
        my_sentence (str): The user's written response

    Returns:
        tuple: (percentage score (0-100), missing words, extra words, perfect_score)
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
    orig_words_copy = original_words.copy()
    my_words_copy = my_words.copy()

    # Track which words are matched (by their original indices)
    matched_orig_indices = set()
    matched_my_indices = set()

    # First pass: Match exact words in the correct positions
    for i in range(min(len(orig_words_copy), len(my_words_copy))):
        if orig_words_copy[i] == my_words_copy[i]:
            matched_orig_indices.add(i)
            matched_my_indices.add(i)

    # Second pass: Match remaining words regardless of position
    # Create lists of unmatched words with their original indices
    unmatched_orig = [
        (i, word)
        for i, word in enumerate(orig_words_copy)
        if i not in matched_orig_indices
    ]
    unmatched_my = [
        (i, word) for i, word in enumerate(my_words_copy) if i not in matched_my_indices
    ]

    # For each unmatched original word, try to find a match in unmatched response words
    for orig_idx, orig_word in unmatched_orig:
        for my_idx, my_word in unmatched_my:
            if orig_word == my_word:
                matched_orig_indices.add(orig_idx)
                matched_my_indices.add(my_idx)
                # Remove this response word from consideration for future matches
                unmatched_my = [(i, w) for i, w in unmatched_my if i != my_idx]
                break

    # Count matched words
    matched_words = len(matched_orig_indices)

    # Find missing and extra words
    missing_words = [
        original_words[i]
        for i in range(len(original_words))
        if i not in matched_orig_indices
    ]
    extra_words = [
        my_words[i] for i in range(len(my_words)) if i not in matched_my_indices
    ]

    # Calculate the percentage score
    score = (matched_words / total_words) * 100

    # Special case handling for up to 3 incorrect words but high match rate
    perfect_score = False
    if (total_words - matched_words) <= 3 and matched_words >= total_words:
        score = 100.0
        perfect_score = True

    return round(score), missing_words, extra_words, perfect_score


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
            "response": "The toughest part parts of postgraduate the education is the funding.",
            "expected_score": 89,
        },
        {
            "original": "The chief economist has radical ideas for the economy.",
            "response": "The chief economist economists has had a radical idea for the economy.",
            "expected_score": 75,  # Example expected score, adjust as needed
        },
    ]

    for i, example in enumerate(examples, 1):
        score, missing, extra, perfect = calculate_pte_score(
            example["original"], example["response"]
        )
        print(f"Example {i}:")
        print(f"Original: {example['original']}")
        print(f"Response: {example['response']}")
        print(f"Calculated Score: {score}%")
        print(f"Expected Score: {example['expected_score']}%")
        print(f"Match: {'✓' if score == example['expected_score'] else '✗'}")
        print(f"Missing words: {missing}")
        print(f"Extra words: {extra}")
        print("-" * 50)


# Interactive scoring interface
def main():
    print("\n===== PTE Write from Dictation Scoring Calculator =====")
    print("-" * 60)
    print("Type 'q' at any prompt to quit the program")

    while True:
        print("\n" + "-" * 60)
        original = input("\nOriginal sentence: ")
        if original.lower() == "q":
            print(
                "\nThank you for using the PTE Scoring Calculator. Good luck with your exam!"
            )
            break

        my_response = input("Your response: ")
        if my_response.lower() == "q":
            print(
                "\nThank you for using the PTE Scoring Calculator. Good luck with your exam!"
            )
            break

        score, missing_words, extra_words, perfect_score = calculate_pte_score(
            original, my_response
        )

        print("\n" + "-" * 60)
        print(f"Original: {original}")
        print(f"Response: {my_response}")
        print("-" * 60)
        print(f"Your score: {score}%")

        # Detailed feedback about errors
        if perfect_score:
            print("Perfect! You got all the words correct or had minimal errors.")
        else:
            if missing_words:
                print(f"\nMissing words: {', '.join(missing_words)}")
                print(
                    f"These words were in the original but missing from your response."
                )

            if extra_words:
                print(f"\nExtra/incorrect words: {', '.join(extra_words)}")
                print(f"These words were in your response but not in the original.")

            # General feedback based on score
            print("\nFeedback:")
            if score >= 80:
                print("Great job! You got most of the words correct.")
            elif score >= 60:
                print("Good effort. Try to pay more attention to exact wording.")
            else:
                print(
                    "Keep practicing. Focus on listening carefully and spelling correctly."
                )


if __name__ == "__main__":
    # Run the interactive scoring interface
    main()
    # Uncomment to test the examples instead
    # test_examples()
