"""
Simple script to generate poems and save them to the output directory.
Run this script to generate sample poems for your assignment.
"""

from poem_generator import PoemGenerator
import os

def main():
    """Generate multiple poems in different styles."""
    
    # Ensure output directory exists (handle path whether running from src/ or root)
    output_dir = "output" if os.path.exists("output") or not os.path.exists("src") else "../output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create generator
    generator = PoemGenerator(seed=42)
    
    print("Generating poems...")
    print("=" * 50)
    
    poems_to_generate = [
        ("haiku", "haiku_1", {}),
        ("haiku", "haiku_2", {}),
        ("quatrain", "quatrain_1", {}),
        ("free_verse", "free_verse_1", {"num_lines": 8}),
        ("free_verse", "free_verse_2", {"num_lines": 6}),
        ("couplet", "couplet_1", {}),
        ("grammar", "grammar_poem_1", {"num_lines": 7}),
    ]
    
    generated_poems = []
    
    for style, filename, kwargs in poems_to_generate:
        print(f"\nGenerating {style}...")
        poem = generator.generate_poem(style, **kwargs)
        
        # Save to file
        filepath = os.path.join(output_dir, f"{filename}.txt")
        generator.save_poem(poem, filepath)
        
        # Store for display
        generated_poems.append((style, filename, poem))
        
        print(f"Saved to {filepath}")
    
    # Display all generated poems
    print("\n" + "=" * 50)
    print("GENERATED POEMS")
    print("=" * 50)
    
    for style, filename, poem in generated_poems:
        print(f"\n{filename.upper().replace('_', ' ')} ({style}):")
        print("-" * 40)
        print(generator.format_poem(poem))
        print()
    
    print(f"\nAll poems saved to {output_dir}/ directory!")
    print(f"Total poems generated: {len(generated_poems)}")
    
    # Save a combined file with all poems
    combined_path = os.path.join(output_dir, "all_poems.txt")
    with open(combined_path, 'w', encoding='utf-8') as f:
        f.write("Bad Poets Society - Generated Poems Collection\n")
        f.write("=" * 50 + "\n\n")
        
        for style, filename, poem in generated_poems:
            f.write(f"{filename.upper().replace('_', ' ')} ({style})\n")
            f.write("-" * 40 + "\n")
            f.write(generator.format_poem(poem))
            f.write("\n\n")
    
    print(f"Combined collection saved to {combined_path}")

if __name__ == "__main__":
    main()

