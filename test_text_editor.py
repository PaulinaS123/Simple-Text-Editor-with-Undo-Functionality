# test_text_editor.py
import unittest
from text_editor import TextEditor


class TestTextEditor(unittest.TestCase):

    def test_normal_add_and_undo(self):
        editor = TextEditor()
        editor.add_char("A")
        editor.add_char("B")
        editor.undo()
        self.assertEqual(editor.text, "A")
        editor.undo()
        self.assertEqual(editor.text, "")

    def test_normal_delete_and_undo(self):
        editor = TextEditor()
        editor.add_char("X")
        editor.add_char("Y")
        editor.delete_char()
        self.assertEqual(editor.text, "X")
        editor.undo()
        self.assertEqual(editor.text, "XY")

    def test_mix_operations(self):
        editor = TextEditor()
        editor.add_char("1")
        editor.add_char("2")
        editor.delete_char()
        editor.add_char("3")
        editor.undo()
        self.assertEqual(editor.text, "1")
        editor.undo()
        self.assertEqual(editor.text, "12")

    # Edge Cases

    def test_undo_empty_stack(self):
        editor = TextEditor()
        editor.undo()
        self.assertEqual(editor.text, "")

    def test_delete_empty_text(self):
        editor = TextEditor()
        editor.delete_char()
        self.assertEqual(editor.text, "")

    def test_special_characters(self):
        editor = TextEditor()
        editor.add_char("!")
        editor.add_char("@")
        editor.delete_char()
        editor.undo()
        self.assertEqual(editor.text, "!@")


if __name__ == "__main__":
    unittest.main()
