# Simple-Text-Editor-with-Undo-Functionality
### Student: Victoria Salomon
### AD 311 Intermediate Development
---
## Objective

Implement a simple text editor that allows adding characters, deleting the last character, and undoing the last operation using a stack.

## Project Structure

```bash
text-editor/
├── text_editor.py
├── test_text_editor.py
├── README.md
└── diagrams/ # Optional folder for flowcharts
```
## Features
- Add a character to the text
- Delete the last character
- Undo last operation (add or delete)
- Stack-based operation tracking
- Handles multiple consecutive undo operations

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/PaulinaS123/text-editor.git
cd text-editor
```
2. Run the program:
```bash
python text_editor.py
```
3. Run the unit tests:
```bash
 python -m unittest test_text_editor.py
```
## Test Cases

Normal Cases:

- Add multiple characters and undo last add
- Delete last character and undo
- Mix add/delete operations and undo sequence

Edge Cases:

- Undo when stack is empty
- Delete when text is empty
- Add/delete special characters

## Time & Space Complexity
```bash
| Operation       | Time Complexity | Space Complexity                     |
| --------------- | --------------- | ------------------------------------ |
| Add char        | O(1)            | O(1) per operation                   |
| Delete char     | O(1)            | O(1) per operation                   |
| Undo            | O(1)            | O(1) per operation                   |
| Overall storage | -               | O(n) for n operations (stack + text) |
```

