# Copilot-as-a-Python-coding-partner
How I Used AI to Automate a Repetitive, Error-Prone Task

The Challenge

I needed to change the font and position of two words per page in a 435-page PDF. Each page had similar content. Let’s call the two words "Apples" and "Oranges.”

What made it tricky:

* The two words were repeated multiple times on every page. Only some occurrences needed to be replaced.  In this long PDF, the sentence "Buy Bob's apples" needed to be replaced each page. The word "apples" was used in other phrases on different lines and did not need to be replaced there.

* In "Buy Bob's apples," the font used for the word "apples" differed from the font used for the words "Buy Bob's.” This also was the case for "Bob's oranges are great too!"

* Several lines moved whenever the two words were replaced. 

Trying to edit this large PDF manually, one word at a time, twice per page would have taken a while and it could induce errors. When you multitask for a living, you need solutions that reduce error because distractions happen.


#My Method

To get this done I used Copilot to write and refine a Python script through prompt engineering. I worked iteratively describing what I wanted in plain language letting Copilot generate the code.

Each time I encountered a challenge, like aligning text, simulating bold, adjusting spacing, or Copilot code errors, I simply described the issue in a prompt. Copilot responded with updated code, explanations, and suggestions. 

Here are some of the tasks the script had to perform:

* Quickly test different font styles and placements.
* Fine-tune the horizontal offset for natural-looking spacing.
* Switch between fonts and styling strategies without rewriting everything.
* Programmatically determine which was the correct "Apple" that needed a font change.

This process took some time. But it gave me a deeper understanding of Python, how to run scripts locally, and how a PDF is rendered.

#My Tools  
* Python 3.9+ (Locally on my Mac OSX laptop)
* PyMuPDF (fitz): for PDF manipulation
* Lucida Calligraphy Bold.otf: font


#What I Learned 
* PyMuPDF gives you control over text placement and styling.
* Custom fonts can be embedded and used precisely.
* While free open source libraries like PyMuPDF are powerful, they can't do everything. More complicated edits require a paid Adobe API. 
* AI or LLM are not perfect. Although they code well, I spent a lot of time fixing mistakes. But it got done!
* Coding this way is fun and productive.

Disclaimer: I used the AI Copilot to generate a draft of this post and to perform the tasks I described. I ended up using it’s text as a draft and rewrote most of it.
