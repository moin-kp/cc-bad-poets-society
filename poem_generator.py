"""
Bad Poets Society - Poem Generator
A template and grammar-based poem generator that creates various styles of poetry.
"""

import random
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class PoemLine:
    """Represents a single line of poetry."""
    text: str
    rhyme_sound: Optional[str] = None


class PoemGenerator:
    """
    A flexible poem generator using templates and grammars.
    Supports multiple poem structures and styles.
    """
    
    def __init__(self, seed: Optional[int] = None):
        """Initialize the generator with optional random seed."""
        if seed is not None:
            random.seed(seed)
        
        # Word banks organized by category
        self.nouns = [
            "moon", "star", "night", "day", "dream", "heart", "soul", "wind",
            "ocean", "river", "mountain", "tree", "flower", "bird", "song",
            "light", "shadow", "time", "memory", "hope", "fear", "love", "pain"
        ]
        
        self.verbs = [
            "dances", "whispers", "sings", "flows", "shines", "fades", "awakens",
            "sleeps", "dreams", "cries", "laughs", "flies", "falls", "rises",
            "burns", "freezes", "melts", "grows", "withers", "blooms"
        ]
        
        self.adjectives = [
            "bright", "dark", "gentle", "wild", "ancient", "young", "silent",
            "loud", "deep", "shallow", "warm", "cold", "soft", "hard", "empty",
            "full", "broken", "whole", "lost", "found", "free", "bound"
        ]
        
        self.adverbs = [
            "slowly", "quickly", "softly", "loudly", "gently", "wildly",
            "silently", "brightly", "darkly", "deeply", "lightly"
        ]
        
        # Template structures for different poem types
        self.templates = {
            "haiku": [
                "{adj} {noun} {verb}",
                "{adj} {noun} in {noun}",
                "{adj} {noun} {verb} {adv}"
            ],
            "quatrain": [
                "The {adj} {noun} {verb} in the {noun}",
                "Where {adj} {noun} {verb} and {verb}",
                "The {adj} {noun} {verb} {adv}",
                "And {adj} {noun} {verb} in {noun}"
            ],
            "free_verse": [
                "{adj} {noun}",
                "{noun} {verb} {adv}",
                "In the {adj} {noun}",
                "The {noun} {verb}",
                "{adj} and {adj}, the {noun} {verb}",
                "When {noun} meets {noun}",
                "{noun} of {adj} {noun}"
            ],
            "couplet": [
                "The {adj} {noun} {verb} in {noun}",
                "And {adj} {noun} {verb} {adv}"
            ]
        }
        
        # Grammar rules for more complex structures
        self.grammar_rules = {
            "noun_phrase": [
                "{adj} {noun}",
                "the {adj} {noun}",
                "{adj} {noun} of {noun}",
                "{noun} and {noun}"
            ],
            "verb_phrase": [
                "{verb} {adv}",
                "{verb} in {noun}",
                "{verb} with {adj} {noun}",
                "{verb} like {adj} {noun}"
            ],
            "sentence": [
                "{noun_phrase} {verb_phrase}",
                "In {noun_phrase}, {verb_phrase}",
                "When {noun_phrase}, {verb_phrase}",
                "{noun_phrase} that {verb_phrase}"
            ]
        }
    
    def _expand_template(self, template: str) -> str:
        """Expand a template string by replacing placeholders with random words."""
        result = template
        
        # Replace placeholders
        result = result.replace("{noun}", random.choice(self.nouns))
        result = result.replace("{verb}", random.choice(self.verbs))
        result = result.replace("{adj}", random.choice(self.adjectives))
        result = result.replace("{adv}", random.choice(self.adverbs))
        
        # Handle recursive replacements (e.g., {noun} in {noun})
        while "{" in result:
            result = result.replace("{noun}", random.choice(self.nouns))
            result = result.replace("{verb}", random.choice(self.verbs))
            result = result.replace("{adj}", random.choice(self.adjectives))
            result = result.replace("{adv}", random.choice(self.adverbs))
        
        return result.capitalize()
    
    def _expand_grammar(self, rule_type: str) -> str:
        """Expand a grammar rule recursively."""
        if rule_type not in self.grammar_rules:
            return ""
        
        template = random.choice(self.grammar_rules[rule_type])
        result = template
        
        # Recursively expand nested rules
        while "{" in result:
            for key in self.grammar_rules.keys():
                placeholder = "{" + key + "}"
                if placeholder in result:
                    result = result.replace(placeholder, self._expand_grammar(key))
            
            # Replace basic placeholders
            result = result.replace("{noun}", random.choice(self.nouns))
            result = result.replace("{verb}", random.choice(self.verbs))
            result = result.replace("{adj}", random.choice(self.adjectives))
            result = result.replace("{adv}", random.choice(self.adverbs))
        
        return result.capitalize()
    
    def generate_haiku(self) -> List[str]:
        """
        Generate a haiku (3 lines: 5-7-5 syllables approximately).
        Note: This is a simplified version that doesn't strictly enforce syllable counts.
        """
        lines = []
        templates = self.templates["haiku"]
        
        # First line (short)
        lines.append(self._expand_template(templates[0]))
        
        # Second line (longer)
        lines.append(self._expand_template(templates[1]))
        
        # Third line (short)
        lines.append(self._expand_template(templates[2]))
        
        return lines
    
    def generate_quatrain(self, rhyme_scheme: str = "ABAB") -> List[str]:
        """
        Generate a quatrain (4-line stanza).
        
        Args:
            rhyme_scheme: Rhyme scheme pattern (e.g., "ABAB", "ABBA", "AABB")
        """
        lines = []
        templates = self.templates["quatrain"]
        
        for i in range(4):
            lines.append(self._expand_template(templates[i % len(templates)]))
        
        return lines
    
    def generate_free_verse(self, num_lines: int = 6) -> List[str]:
        """
        Generate free verse poetry.
        
        Args:
            num_lines: Number of lines in the poem
        """
        lines = []
        templates = self.templates["free_verse"]
        
        for _ in range(num_lines):
            template = random.choice(templates)
            lines.append(self._expand_template(template))
        
        return lines
    
    def generate_couplet(self) -> List[str]:
        """Generate a couplet (2-line stanza)."""
        lines = []
        templates = self.templates["couplet"]
        
        for template in templates:
            lines.append(self._expand_template(template))
        
        return lines
    
    def generate_grammar_poem(self, num_lines: int = 5) -> List[str]:
        """Generate a poem using grammar rules."""
        lines = []
        
        for _ in range(num_lines):
            lines.append(self._expand_grammar("sentence"))
        
        return lines
    
    def generate_poem(self, style: str = "free_verse", **kwargs) -> List[str]:
        """
        Generate a poem in the specified style.
        
        Args:
            style: One of "haiku", "quatrain", "free_verse", "couplet", "grammar"
            **kwargs: Additional arguments for specific styles
                - num_lines: For free_verse and grammar styles
                - rhyme_scheme: For quatrain style
        
        Returns:
            List of poem lines
        """
        style = style.lower()
        
        if style == "haiku":
            return self.generate_haiku()
        elif style == "quatrain":
            rhyme_scheme = kwargs.get("rhyme_scheme", "ABAB")
            return self.generate_quatrain(rhyme_scheme)
        elif style == "free_verse":
            num_lines = kwargs.get("num_lines", 6)
            return self.generate_free_verse(num_lines)
        elif style == "couplet":
            return self.generate_couplet()
        elif style == "grammar":
            num_lines = kwargs.get("num_lines", 5)
            return self.generate_grammar_poem(num_lines)
        else:
            raise ValueError(f"Unknown style: {style}. Choose from: haiku, quatrain, free_verse, couplet, grammar")
    
    def format_poem(self, lines: List[str]) -> str:
        """Format poem lines into a single string."""
        return "\n".join(lines)
    
    def save_poem(self, lines: List[str], filename: str):
        """Save a poem to a file."""
        import os
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.format_poem(lines))
            f.write("\n")


def main():
    """Example usage of the poem generator."""
    import os
    generator = PoemGenerator(seed=42)
    
    print("=" * 50)
    print("Bad Poets Society - Poem Generator")
    print("=" * 50)
    print()
    
    # Generate different styles
    styles = ["haiku", "quatrain", "free_verse", "couplet", "grammar"]
    
    for style in styles:
        print(f"\n{style.upper().replace('_', ' ')}:")
        print("-" * 30)
        poem = generator.generate_poem(style, num_lines=6 if style in ["free_verse", "grammar"] else None)
        print(generator.format_poem(poem))
        print()
    
    # Save some poems (handle path whether running from src/ or root)
    print("\nSaving sample poems to output/ directory...")
    output_dir = "output" if os.path.exists("output") or not os.path.exists("src") else "../output"
    for i, style in enumerate(styles[:3], 1):
        poem = generator.generate_poem(style, num_lines=6 if style in ["free_verse", "grammar"] else None)
        generator.save_poem(poem, os.path.join(output_dir, f"poem_{i}_{style}.txt"))
    
    print("Done!")


if __name__ == "__main__":
    main()

