# Bad Poets Society - Poem Generator

A computational creativity project that generates poetry using template-based and grammar-based approaches. This system creates various styles of poems including haikus, quatrains, free verse, couplets, and grammar-generated poetry.

## Project Overview

This poem generator is part of a Computational Creativity assignment exploring how computational systems can create artistic content. The generator uses templates and grammar rules to produce original poetry by combining words from curated word banks.


## Usage

### Basic Usage

Run the generator with the example script:

```bash
python poem_generator.py
```

This will generate sample poems in all available styles and save three examples to the `output/` directory.

### Using the Generator in Your Code

```python
from poem_generator import PoemGenerator

# Create a generator instance
generator = PoemGenerator(seed=42)  # Optional: set seed for reproducibility

# Generate different poem styles
haiku = generator.generate_haiku()
quatrain = generator.generate_quatrain()
free_verse = generator.generate_free_verse(num_lines=8)
couplet = generator.generate_couplet()
grammar_poem = generator.generate_grammar_poem(num_lines=6)

# Format and print
print(generator.format_poem(free_verse))

# Save to file
generator.save_poem(free_verse, "output/my_poem.txt")
```

### Available Poem Styles

- **Haiku**: 3-line poem (approximately 5-7-5 syllable pattern)
- **Quatrain**: 4-line stanza (supports rhyme schemes)
- **Free Verse**: Flexible number of lines with varied structures
- **Couplet**: 2-line stanza
- **Grammar**: Poems generated using recursive grammar rules

### Command-Line Interface

You can also use the generator interactively:

```python
from poem_generator import PoemGenerator

generator = PoemGenerator()

# Generate a specific style
poem = generator.generate_poem("free_verse", num_lines=10)
print(generator.format_poem(poem))
```

## How It Works

The poem generator uses two main approaches:

1. **Template-Based Generation**: Uses predefined sentence templates with placeholders (e.g., `{adj} {noun} {verb}`) that are filled with random words from curated word banks.

2. **Grammar-Based Generation**: Uses recursive grammar rules to build more complex sentence structures, allowing for nested phrases and varied syntax.

### Word Banks

The generator maintains word banks organized by part of speech:
- Nouns (e.g., moon, star, dream, heart)
- Verbs (e.g., dances, whispers, flows)
- Adjectives (e.g., bright, dark, gentle)
- Adverbs (e.g., slowly, softly, deeply)

### Stopping Criteria

- **Haiku**: Fixed at 3 lines
- **Quatrain**: Fixed at 4 lines
- **Free Verse**: Configurable number of lines (default: 6)
- **Couplet**: Fixed at 2 lines
- **Grammar**: Configurable number of lines (default: 5)

## Extending the Generator

You can extend the generator by:

1. **Adding more words** to the word banks in `PoemGenerator.__init__()`
2. **Creating new templates** in the `templates` dictionary
3. **Defining new grammar rules** in the `grammar_rules` dictionary
4. **Adding new poem styles** by creating new generation methods

Example:

```python
# Add new words
generator.nouns.extend(["cloud", "rain", "thunder"])
generator.adjectives.extend(["mysterious", "ethereal"])

# Add new template
generator.templates["sonnet"] = [
    "The {adj} {noun} {verb} in {noun}",
    # ... more lines
]
```

## Output

Generated poems are saved as plain text files in the `output/` directory. Each poem is formatted with one line per verse.

## Inspiring Set

The generator's word banks and templates are inspired by:
- Classic poetry themes (nature, emotions, time, dreams)
- Common poetic imagery (moon, stars, oceans, mountains)
- Traditional poetic structures (haiku, quatrain, couplet)

## Future Enhancements

Potential improvements:
- Syllable counting for stricter haiku generation
- Rhyme detection and enforcement
- Integration with NLP libraries (spaCy, NLTK) for more sophisticated grammar
- Machine learning approaches for style learning
- User-defined word banks and templates

## Notes

- The generator uses random selection, so each run produces different poems
- Set a seed for reproducibility: `PoemGenerator(seed=42)`
- The syllable counting in haikus is approximate and not strictly enforced
- Rhyme schemes in quatrains are conceptual (actual rhyming not implemented)



