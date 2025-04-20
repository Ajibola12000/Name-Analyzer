def analyze_name(name):
    print(f"\n🔍 Analyzing the name: '{name}'\n")
    
    # Basic Info
    print(f"📏 Length: {len(name)} characters (including space)")
    print(f"🔠 Uppercase: {name.upper()}")
    print(f"🔡 Lowercase: {name.lower()}")
    print(f"🔤 Title Case: {name.title()}")
    print(f"🔣 First Character: '{name[0]}'")
    print(f"🔚 Last Character: '{name[-1]}'")
    
    # Check for 'AI' (case-insensitive)
    print(f"🤖 Contains 'AI'? {'ai' in name.lower()}")
    
    # Split into words (if space exists)
    if ' ' in name:
        first, last = name.split()
        print(f"\n✂️ Split into: First Name = '{first}', Last Name = '{last}'")
        print(f"📏 First Name Length: {len(first)} letters")
        print(f"📏 Last Name Length: {len(last)} letters")
    
    # Count vowels
    vowels = sum(1 for char in name.lower() if char in 'aeiou')
    print(f"\n🎵 Number of vowels: {vowels}")
    
    # Count consonants
    consonants = sum(1 for char in name.lower() if char.isalpha() and char not in 'aeiou')
    print(f"🎶 Number of consonants: {consonants}")
    
    # Generate initials
    initials = '.'.join([word[0].upper() for word in name.split()]) + "."
    print(f"\n✒️ Initials: {initials}")
    
    # GitHub-style username suggestion
    username = name.lower().replace(' ', '-')
    print(f"\n💻 GitHub Username Suggestion: {username}")
    
    # Fun fact: Reverse the name
    reversed_name = name[::-1]
    print(f"\n🌀 Reversed Name: {reversed_name}")

if __name__ == "__main__":
    user_name = "Adegoke Ajibola"
    analyze_name(user_name)