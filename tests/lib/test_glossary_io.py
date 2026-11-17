import unittest

from ...novel import glossary_csv_entry


class TestGlossaryCsvEntry(unittest.TestCase):
    def test_new_export_ignores_count_and_keeps_notes(self):
        parsed = glossary_csv_entry(
            ['source', 'translation', 'type', 'count', 'notes'],
            ['Sino', 'Сино', 'character', '42', 'A note'])
        self.assertEqual(('Sino', {
            'translation': 'Сино',
            'type': 'character',
            'notes': 'A note',
        }), parsed)
        self.assertNotIn('count', parsed[1])

    def test_legacy_four_column_export_keeps_notes(self):
        parsed = glossary_csv_entry(
            ['source', 'translation', 'type', 'notes'],
            ['Fino', 'Фино', 'character', 'Legacy note'])
        self.assertEqual('Legacy note', parsed[1]['notes'])
        self.assertNotIn('count', parsed[1])

    def test_positional_fallback_handles_five_and_four_columns(self):
        five = glossary_csv_entry(
            ['unknown'], ['A', 'B', 'object', '99', 'Five note'])
        four = glossary_csv_entry(
            ['unknown'], ['A', 'B', 'object', 'Four note'])
        self.assertEqual('Five note', five[1]['notes'])
        self.assertEqual('Four note', four[1]['notes'])


if __name__ == '__main__':
    unittest.main()
