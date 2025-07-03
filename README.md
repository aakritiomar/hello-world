# Efficient String Searching Algorithms

This project provides multiple efficient algorithms for searching strings within long paragraphs or documents.

## Files

- `string_search.py` - Main implementation with multiple string searching algorithms
- `example_usage.py` - Practical examples showing how to use the search algorithms
- `README.md` - This file

## Algorithms Implemented

1. **Built-in Python Methods** - Fastest for general use cases
2. **Knuth-Morris-Pratt (KMP)** - O(n+m) guaranteed performance
3. **Boyer-Moore** - Efficient for longer patterns
4. **Rabin-Karp** - Good for multiple pattern searches
5. **Regular Expressions** - Complex pattern matching

## Quick Start

```python
from string_search import StringSearcher

# Create searcher instance
searcher = StringSearcher()

# Search for a pattern in text
text = "Your long paragraph here..."
pattern = "search_term"

# Find all occurrences
positions = searcher.find_builtin(text, pattern)
print(f"Found at positions: {positions}")
```

## Performance Comparison

Based on benchmarks with 100K character text:

1. **Regex**: ~0.09 ms (fastest)
2. **Built-in**: ~0.10 ms 
3. **Boyer-Moore**: ~4.6 ms
4. **KMP**: ~6.3 ms
5. **Rabin-Karp**: ~15.8 ms

## When to Use Each Algorithm

- **Built-in methods**: General purpose (recommended)
- **KMP**: When you need guaranteed O(n+m) performance
- **Boyer-Moore**: For longer patterns or when pattern is longer than average
- **Rabin-Karp**: When searching for multiple patterns simultaneously
- **Regex**: For complex pattern matching or case-insensitive searches

## Running the Examples

```bash
# Run the main demo with performance benchmarks
python3 string_search.py

# Run practical usage examples
python3 example_usage.py
```

## Features

- Case-sensitive and case-insensitive searching
- Multiple pattern search
- Word boundary detection
- Performance benchmarking
- Context display around matches
- All algorithms return the same results for verification
