# text_editor.py

class TextOperation:
    def __init__(self, op_type, char=None):
        self.op_type = op_type  # 'add' or 'delete'
        self.char = char        # character involved


class TextEditor:
    def __init__(self):
        self.text = ""
        self.stack = []

    def add_char(self, char):
        self.text += char
        self.stack.append(TextOperation("add", char))
        print("Current Text:", self.text)

    def delete_char(self):
        if self.text:
            deleted = self.text[-1]
            self.text = self.text[:-1]
            self.stack.append(TextOperation("delete", deleted))
        print("Current Text:", self.text)

    def undo(self):
        if not self.stack:
            print("Nothing to undo")
            return
        last_op = self.stack.pop()
        if last_op.op_type == "add":
            self.text = self.text[:-1]
        elif last_op.op_type == "delete":
            self.text += last_op.char
        print("Current Text after Undo:", self.text)
