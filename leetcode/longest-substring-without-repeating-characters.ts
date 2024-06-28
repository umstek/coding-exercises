function lengthOfLongestSubstring(s: string): number {
  let maxLen = 0;
  let start = 0;
  let chars = new Map();
  for (let i = 0; i < s.length; i += 1) {
    const c = s.charAt(i);
    if (chars.has(c)) {
      maxLen = Math.max(i - start, maxLen);
      for (let o = start; o < chars.get(c); o++) {
        chars.delete(s.charAt(o))
      }
      start = chars.get(c) + 1;
      chars.set(c, i);
    } else {
      chars.set(c, i);
    }
  }
  maxLen = Math.max(s.length - start, maxLen);

  return maxLen;
}

