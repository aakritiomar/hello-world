#!/usr/bin/env python3
"""
Example usage of the StringSearcher class for practical scenarios.
"""

from string_search import StringSearcher


def example_basic_search():
    """Basic string searching example."""
    text = """
    Python is a powerful programming language. Python is easy to learn and 
    Python has extensive libraries. Many developers choose Python for their projects
    because Python offers great flexibility and Python community support is excellent.
    """
    
    pattern = "Python"
    searcher = StringSearcher()
    
    # Find all occurrences
    positions = searcher.find_builtin(text, pattern)
    
    print(f"Found '{pattern}' at positions: {positions}")
    print(f"Total occurrences: {len(positions)}")
    
    # Show context around each match
    for pos in positions:
        start = max(0, pos - 10)
        end = min(len(text), pos + len(pattern) + 10)
        context = text[start:end].replace('\n', ' ').strip()
        print(f"Position {pos}: ...{context}...")


def example_case_insensitive_search():
    """Case-insensitive searching example."""
    text = "Hello World! This is a HELLO message with hello variations."
    pattern = "hello"
    searcher = StringSearcher()
    
    # Case-sensitive search
    positions_sensitive = searcher.find_builtin(text, pattern)
    print(f"Case-sensitive search for '{pattern}': {positions_sensitive}")
    
    # Case-insensitive search using regex
    positions_insensitive = searcher.find_regex(text, pattern, case_sensitive=False)
    print(f"Case-insensitive search for '{pattern}': {positions_insensitive}")


def example_multiple_patterns():
    """Search for multiple patterns efficiently."""
    text = """
    The quick brown fox jumps over the lazy dog. The fox is quick and 
    the dog is lazy. A quick fox and a lazy dog make an interesting story.
    """
    
    patterns = ["fox", "dog", "quick", "lazy"]
    searcher = StringSearcher()
    
    print("Multiple pattern search results:")
    for pattern in patterns:
        positions = searcher.find_builtin(text, pattern)
        print(f"'{pattern}': {len(positions)} occurrences at positions {positions}")


def example_long_text_search():
    """Example with very long text (simulating file content)."""
    # Simulate reading a large file
    with open("string_search.py", "r") as file:
        long_text = file.read()
    
    pattern = "def"
    searcher = StringSearcher()
    
    # Compare different algorithms
    algorithms = {
        "Built-in": searcher.find_builtin,
        "KMP": searcher.find_kmp,
        "Boyer-Moore": searcher.find_boyer_moore
    }
    
    print(f"Searching for '{pattern}' in file with {len(long_text)} characters:")
    
    for name, func in algorithms.items():
        positions = func(long_text, pattern)
        print(f"{name}: Found {len(positions)} occurrences")


def example_word_boundaries():
    """Find whole words using regex."""
    text = "The cat catches cats. A cat is different from cats."
    pattern = "cat"
    searcher = StringSearcher()
    
    # Find all occurrences of "cat" (including within "cats")
    all_positions = searcher.find_builtin(text, pattern)
    print(f"All '{pattern}' occurrences: {all_positions}")
    
    # Find only whole word "cat" using regex
    import re
    whole_word_positions = []
    for match in re.finditer(r'\b' + re.escape(pattern) + r'\b', text):
        whole_word_positions.append(match.start())
    
    print(f"Whole word '{pattern}' occurrences: {whole_word_positions}")


if __name__ == "__main__":
    print("=== Basic Search Example ===")
    example_basic_search()
    print("\n=== Case-Insensitive Search Example ===")
    example_case_insensitive_search()
    print("\n=== Multiple Patterns Example ===")
    example_multiple_patterns()
    print("\n=== Long Text Search Example ===")
    example_long_text_search()
    print("\n=== Word Boundaries Example ===")
    example_word_boundaries()