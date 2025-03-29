># Headings
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
that's how to give heading in Markdown

# Text
Normal
> Special Text

<!-- Tip : 1 add double return to exit special text -->

# Line breaks

This is line number one \
This is line number two
<!-- Tip : 2 you can either use double return or \ for line break1 -->

# Concatenation

> ## Hello Mate! :)

# Text Formatting styles

**Bold**
<!-- double asterisk or underscores for bolding __bold__-->
*Italic*   
<!-- single asterisk or underscores for italisation _italic_ -->
***bold+italic***
<!-- triple asterisk or underscores for both italic and bold  ___italic+bold___-->

# Lists

- Bullet One
- Bullet Two
- Bullet Three
    - Sub Bullet 
        - Sub Sub Bullet
<!-- Tabular space + space + hypen\hash for sub sub bullet -->
- Bullet Four
    - Sub Bullet b
<!-- Tabular space + hyphen\hash adds sub bullet -->
- Bullet Five
<!-- for bullet add hyphen\hash -->

> Numbering

1. First
2. Second
3. Third 
<!-- just simply add number + full stop -->
<!-- similar sub listing as bullets -->
1. Four
1. Five
<!--Tip: 3 Automically syncs so just dw about numbering -->

# Line\Page Breaks

First Line

---
<!-- --- (three hyphens) or ___(three underscores) or ***(three asterisk) for line break  -->

Second Line

# Hyperlinks

<https://www.freecodecamp.org/news/how-to-use-markdown-in-vscode/>
<!-- use <> lesser and greater for links -->

[Learn Markdown from freeCodeCamp](https://www.freecodecamp.org/news/how-to-use-markdown-in-vscode/)
<!-- square brackets + roundbrackets for text embedded links -->

[freeCodeCamp]:https://www.freecodecamp.org/email-sign-up/
<!-- []+:+link for making link keys -->

That's a [link][freeCodeCamp]
<!-- that's how to use keys -->

# Images

![image](mc.png)
<!-- !+[]+() for opening link by image -->

# Adding Code or Code Block

Taking input in python: `input()`
<!-- single ticks in start and end -->

```python
def myfunction():
    return 
```
<!-- use triple ticks in start and end for block of code -->
<!-- Tip : 4 you can also add language name for formatting according to that language -->

# Tables

| **Item**       | **Category**    | **Quantity** | **Price (USD)** |
|-----------------|-----------------|--------------|-----------------|
| Apples         | Fruits          | 12           | 3.50            |
| Notebook       | Stationery      | 5            | 7.00            |
| Backpack       | Accessories     | 1            | 20.00           |
| Sneakers       | Footwear        | 2 pairs      | 40.00           |
<!-- straight slash + text + straight slash -->
<!-- striaght slash + few hyphens + straight slash -->


<!-- for aligning text to right add colon in start of hyphens -->
<!-- for aligning text to left add colon in end of hyphens -->
<!-- for middle aligning add colon to both sides -->
<!-- for instance -->
<!-- | **Item**       | **Category**    | **Quantity** | **Price (USD)** |
|-----------------|-----------------:|--------------|-----------------|
| Apples         | Fruits          | 12           | 3.50            |
| Notebook       | Stationery      | 5            | 7.00            |
| Backpack       | Accessories     | 1            | 20.00           |
| Sneakers       | Footwear        | 2 pairs      | 40.00           | -->

# Contents

[Headings](#headings)\
[Text](#text)\
[Line breaks](#line-breaks)
<!-- square brackets + round brackets -->
