print("pangram" if len(set(input().strip().lower()) & set("abcdefghijklmnopqrstuvwxyz")) == 26 else "not pangram")
