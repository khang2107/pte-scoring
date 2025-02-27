# PTE Write from Dictation Scoring Tool

A Python-based calculator that simulates the scoring system for the "Write from Dictation" task in Pearson Test of English (PTE) Academic exams.

## Overview

The "Write from Dictation" task is a crucial component of the PTE Academic exam's Listening section. In this task, test takers listen to a sentence and must type it exactly as they hear it. This tool helps you practice by comparing your written response against the original dictation and calculating a score that approximates the PTE scoring algorithm.

## Features

- **Accurate Scoring**: Implements a scoring system that closely resembles the actual PTE scoring mechanism
- **Word Matching**: Identifies correctly used words regardless of position
- **Detailed Feedback**: Provides information on missing and extra words
- **Perfect Score Recognition**: Awards 100% for responses with minimal errors but high word match rate
- **Interactive Interface**: Easy-to-use command-line interface for practicing

## How It Works

The scoring algorithm follows these steps:

1. **Text Preprocessing**: Both the original sentence and your response are tokenized, converted to lowercase, and stripped of punctuation
2. **Two-Pass Matching**:
    - First pass identifies words that match exactly in the correct positions
    - Second pass finds remaining words that match regardless of position
3. **Score Calculation**: Your score is the percentage of original words that you correctly included
4. **Special Case Handling**: If you've matched all words but added up to 3 extra words, you can still receive a perfect score

## Usage

Run the program and follow the interactive prompts:

```
python pte_scoring.py
```

### Example Interaction

```
===== PTE Write from Dictation Scoring Calculator =====
------------------------------------------------------------
Type 'q' at any prompt to quit the program

------------------------------------------------------------

Original sentence: The chief economist has radical ideas for the economy.
Your response: The chief economist has a radical idea for the economy.

------------------------------------------------------------
Original: The chief economist has radical ideas for the economy.
Response: The chief economist has a radical idea for the economy.
------------------------------------------------------------
Your score: 88%

Missing words: ideas

Extra/incorrect words: a, idea

Feedback:
Great job! You got most of the words correct.
```

## Testing with Examples

The tool includes a test function with several example sentences to demonstrate scoring behavior. To run the tests, uncomment the `test_examples()` line in the main function.

## Scoring Logic

- Each correct word from the original sentence is worth points
- Words are matched exactly (after converting to lowercase and removing punctuation)
- Word order is considered in the first matching pass but allowances are made in the second pass
- Extra or incorrect words do not directly reduce your score, but missing words do
- The final score is: (number of matched words / total words in original) × 100

## Installation

Clone this repository and run the Python script:

```bash
git clone https://github.com/yourusername/pte-dictation-scorer.git
cd pte-dictation-scorer
python pte_scoring.py
```

## Requirements

- Python 3.6 or higher
