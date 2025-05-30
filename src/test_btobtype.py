import unittest

from blocktoblocktype import block_to_block_type
from mdtoblocks import markdown_to_blocks

class BToBType(unittest.TestCase):
    def test_b_to_b_type(self):
        md = """
# This is a header

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

```This is a longgggg
multi line
code block```

>This is a quote
>This is also a quote

1. Ordered list item
2. Ordered list item again
"""
        blocks = markdown_to_blocks(md)

        for block in blocks:
            block_to_block_type(block)