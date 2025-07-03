#!/usr/bin/env python3
"""
Efficient String Searching Algorithms

This module provides multiple implementations for efficiently searching
a pattern string within a long text paragraph.
"""

import time
import re
from typing import List, Optional


class StringSearcher:
    """A collection of efficient string searching algorithms."""
    
    @staticmethod
    def find_builtin(text: str, pattern: str) -> List[int]:
        """
        Use Python's built-in string methods (most efficient for general use).
        
        Args:
            text: The text to search in
            pattern: The pattern to find
            
        Returns:
            List of starting indices where pattern is found
        """
        positions = []
        start = 0
        while True:
            pos = text.find(pattern, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        return positions
    
    @staticmethod
    def find_regex(text: str, pattern: str, case_sensitive: bool = True) -> List[int]:
        """
        Use regular expressions for pattern matching.
        
        Args:
            text: The text to search in
            pattern: The pattern to find
            case_sensitive: Whether to perform case-sensitive search
            
        Returns:
            List of starting indices where pattern is found
        """
        flags = 0 if case_sensitive else re.IGNORECASE
        positions = []
        for match in re.finditer(re.escape(pattern), text, flags):
            positions.append(match.start())
        return positions
    
    @staticmethod
    def find_kmp(text: str, pattern: str) -> List[int]:
        """
        Knuth-Morris-Pratt algorithm implementation.
        Time complexity: O(n + m) where n = len(text), m = len(pattern)
        
        Args:
            text: The text to search in
            pattern: The pattern to find
            
        Returns:
            List of starting indices where pattern is found
        """
        if not pattern:
            return []
        
        # Build the partial match table (failure function)
        def build_partial_match_table(pattern: str) -> List[int]:
            table = [0] * len(pattern)
            j = 0
            
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = table[j - 1]
                
                if pattern[i] == pattern[j]:
                    j += 1
                
                table[i] = j
            
            return table
        
        partial_match_table = build_partial_match_table(pattern)
        positions = []
        j = 0  # Index for pattern
        
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = partial_match_table[j - 1]
            
            if text[i] == pattern[j]:
                j += 1
            
            if j == len(pattern):
                positions.append(i - j + 1)
                j = partial_match_table[j - 1]
        
        return positions
    
    @staticmethod
    def find_boyer_moore(text: str, pattern: str) -> List[int]:
        """
        Boyer-Moore algorithm implementation (simplified version).
        Very efficient for longer patterns.
        
        Args:
            text: The text to search in
            pattern: The pattern to find
            
        Returns:
            List of starting indices where pattern is found
        """
        if not pattern:
            return []
        
        # Build bad character table
        def build_bad_char_table(pattern: str) -> dict:
            table = {}
            for i in range(len(pattern)):
                table[pattern[i]] = i
            return table
        
        bad_char_table = build_bad_char_table(pattern)
        positions = []
        i = 0
        
        while i <= len(text) - len(pattern):
            j = len(pattern) - 1
            
            # Check pattern from right to left
            while j >= 0 and pattern[j] == text[i + j]:
                j -= 1
            
            if j < 0:
                # Pattern found
                positions.append(i)
                i += 1
            else:
                # Calculate shift using bad character rule
                bad_char = text[i + j]
                shift = j - bad_char_table.get(bad_char, -1)
                i += max(1, shift)
        
        return positions
    
    @staticmethod
    def find_rabin_karp(text: str, pattern: str, prime: int = 101) -> List[int]:
        """
        Rabin-Karp algorithm using rolling hash.
        Good for searching multiple patterns.
        
        Args:
            text: The text to search in
            pattern: The pattern to find
            prime: Prime number for hash calculation
            
        Returns:
            List of starting indices where pattern is found
        """
        if not pattern:
            return []
        
        n = len(text)
        m = len(pattern)
        positions = []
        
        # Calculate hash values
        pattern_hash = 0
        text_hash = 0
        h = 1
        
        # Calculate h = pow(256, m-1) % prime
        for i in range(m - 1):
            h = (h * 256) % prime
        
        # Calculate initial hash values
        for i in range(m):
            pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
            text_hash = (256 * text_hash + ord(text[i])) % prime
        
        # Slide the pattern over text
        for i in range(n - m + 1):
            # Check if hash values match
            if pattern_hash == text_hash:
                # Verify character by character
                if text[i:i + m] == pattern:
                    positions.append(i)
            
            # Calculate hash value for next window
            if i < n - m:
                text_hash = (256 * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
                if text_hash < 0:
                    text_hash += prime
        
        return positions


def benchmark_algorithms(text: str, pattern: str, iterations: int = 1000) -> dict:
    """
    Benchmark different string searching algorithms.
    
    Args:
        text: The text to search in
        pattern: The pattern to find
        iterations: Number of iterations for timing
        
    Returns:
        Dictionary with algorithm names and their execution times
    """
    algorithms = {
        'Built-in': StringSearcher.find_builtin,
        'KMP': StringSearcher.find_kmp,
        'Boyer-Moore': StringSearcher.find_boyer_moore,
        'Rabin-Karp': StringSearcher.find_rabin_karp,
        'Regex': StringSearcher.find_regex
    }
    
    results = {}
    
    for name, func in algorithms.items():
        start_time = time.time()
        for _ in range(iterations):
            positions = func(text, pattern)
        end_time = time.time()
        
        results[name] = {
            'time': (end_time - start_time) / iterations,
            'positions_found': len(positions)
        }
    
    return results


def main():
    """Demonstrate string searching with example text."""
    
    # Example long paragraph
    long_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor 
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore 
    eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
    in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis 
    unde omnis iste natus error sit voluptate accusantium doloremque laudantium, 
    totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi 
    architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia 
    voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores 
    eos qui ratione voluptatem sequi nesciunt. Lorem ipsum dolor sit amet, consectetur 
    adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    """ * 100  # Make it longer for better benchmarking
    
    search_pattern = "dolor"
    
    print(f"Searching for '{search_pattern}' in text of {len(long_text):,} characters")
    print("=" * 60)
    
    # Test all algorithms
    searcher = StringSearcher()
    
    print("Algorithm Results:")
    print("-" * 40)
    
    # Built-in method
    positions = searcher.find_builtin(long_text, search_pattern)
    print(f"Built-in method: Found {len(positions)} occurrences")
    print(f"First 5 positions: {positions[:5]}")
    
    # KMP algorithm
    positions_kmp = searcher.find_kmp(long_text, search_pattern)
    print(f"KMP algorithm: Found {len(positions_kmp)} occurrences")
    
    # Boyer-Moore algorithm
    positions_bm = searcher.find_boyer_moore(long_text, search_pattern)
    print(f"Boyer-Moore algorithm: Found {len(positions_bm)} occurrences")
    
    # Rabin-Karp algorithm
    positions_rk = searcher.find_rabin_karp(long_text, search_pattern)
    print(f"Rabin-Karp algorithm: Found {len(positions_rk)} occurrences")
    
    # Regex method
    positions_regex = searcher.find_regex(long_text, search_pattern)
    print(f"Regex method: Found {len(positions_regex)} occurrences")
    
    # Verify all algorithms return the same results
    all_same = (positions == positions_kmp == positions_bm == 
                positions_rk == positions_regex)
    print(f"\nAll algorithms agree: {all_same}")
    
    # Performance benchmark
    print("\n" + "=" * 60)
    print("Performance Benchmark (average time per search):")
    print("-" * 60)
    
    benchmark_results = benchmark_algorithms(long_text, search_pattern, iterations=100)
    
    # Sort by execution time
    sorted_results = sorted(benchmark_results.items(), key=lambda x: x[1]['time'])
    
    for name, data in sorted_results:
        print(f"{name:12}: {data['time']*1000:.4f} ms")
    
    print("\nRecommendations:")
    print("- Use built-in methods for general purpose searching (fastest)")
    print("- Use KMP for guaranteed O(n+m) performance")
    print("- Use Boyer-Moore for longer patterns")
    print("- Use Rabin-Karp when searching for multiple patterns")
    print("- Use Regex for complex pattern matching")


if __name__ == "__main__":
    main()