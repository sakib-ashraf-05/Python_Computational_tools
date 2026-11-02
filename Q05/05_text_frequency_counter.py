from collections import Counter
import string


def count_word_frequency(text: str) -> Counter:
    """Counts the frequency of each word in the text string.

    Performs case-insensitive counting and strips punctuation.
    """
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return Counter(words)


def count_character_frequency(text: str, ignore_spaces: bool = True) -> Counter:
    """Counts the frequency of each character in the text string."""
    if ignore_spaces:
        text = text.replace(" ", "")
    return Counter(text)


def main():
    print("=== Text Frequency Analyzer ===\n")
    sample_text = input("Enter a text string to analyze: ").strip()

    if not sample_text:
        print("No text provided. Exiting.")
        return

    # Word Frequency Analysis
    word_counts = count_word_frequency(sample_text)
    print("\n--- Word Frequencies ---")
    for word, frequency in word_counts.most_common():
        print(f"'{word}': {frequency}")

    # Character Frequency Analysis
    char_counts = count_character_frequency(sample_text, ignore_spaces=True)
    print("\n--- Character Frequencies (excluding spaces) ---")
    for char, frequency in char_counts.most_common():
        print(f"'{char}': {frequency}")


if __name__ == "__main__":
    main()