def characterReplacement(s: str, k: int) -> int:
    max_freq_count = {}
    left = 0
    result = 0

    for right in range(len(s)):
        # Add the new character to the hashmap
        max_freq_count[s[right]] = 1 + max_freq_count.get(s[right], 0)

        # Check if window is invalid
        window_size = right - left + 1
        if window_size - max(max_freq_count.values()) > k:
            # Shrink from left
            max_freq_count[s[left]] -= 1
            left += 1

        # Update result with current valid window size
        result = max(result, right - left + 1)

    return result

print(characterReplacement("AAABABB", 1))