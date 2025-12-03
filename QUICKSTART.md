# Quick Start Guide

## Getting Started in 3 Steps

### 1. Generate Your First Poem

From the project root directory (`csr/`), run:

```bash
python src/poem_generator.py
```

This will generate sample poems in all styles and save 3 examples to the `output/` directory.

### 2. Generate Multiple Poems

To generate a collection of poems:

```bash
python src/generate_poems.py
```

This creates 7 different poems and saves them all to `output/`, plus a combined file.

### 3. Use in Your Own Code

```python
from src.poem_generator import PoemGenerator

# Create generator
generator = PoemGenerator()

# Generate a poem
poem = generator.generate_poem("free_verse", num_lines=10)

# Print it
print(generator.format_poem(poem))

# Save it
generator.save_poem(poem, "output/my_poem.txt")
```

## Available Styles

- `"haiku"` - 3-line haiku
- `"quatrain"` - 4-line stanza
- `"free_verse"` - Flexible length (default 6 lines)
- `"couplet"` - 2-line stanza
- `"grammar"` - Grammar-generated poem (default 5 lines)

## Examples

```python
# Haiku
haiku = generator.generate_haiku()

# Free verse with 12 lines
long_poem = generator.generate_free_verse(num_lines=12)

# Quatrain with specific rhyme scheme
quatrain = generator.generate_quatrain(rhyme_scheme="ABAB")

# Grammar poem
grammar_poem = generator.generate_grammar_poem(num_lines=8)
```

## Customization

### Add More Words

```python
generator = PoemGenerator()
generator.nouns.extend(["cloud", "rain", "thunder"])
generator.adjectives.extend(["mysterious", "ethereal"])
```

### Reproducible Results

```python
# Use a seed for the same results
generator = PoemGenerator(seed=42)
poem1 = generator.generate_poem("haiku")
poem2 = generator.generate_poem("haiku")  # Different poem

# Reset with same seed for same results
generator = PoemGenerator(seed=42)
poem3 = generator.generate_poem("haiku")  # Same as poem1
```

## Next Steps

1. Read the full [README.md](README.md) for detailed documentation
2. Check out the [logbook template](docs/logbook_template.md) for documenting your process
3. Generate poems and use Generative AI tools to present them
4. Extend the generator with your own templates and word banks

## Need Help?

- Check `src/poem_generator.py` for the full implementation
- See `output/` directory for example generated poems
- Review `data/word_banks_example.json` for word bank ideas

