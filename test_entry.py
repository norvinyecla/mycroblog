import unittest
import os
import json
from mycroblog import create_app, db 

class EntryTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.entry = { 'text': 'random entry' }
        
        with self.app.app_context():
            db.create_all()

    def test_entry_add(self):
        res = self.client().post('/entry', data=self.entry)
        self.assertEqual(res.status_code, 201)

    def test_entry_get_by_id(self):
        res = self.client().post('/entry', data=self.entry)
        self.assertEqual(res.status_code, 201)
        json_result = json.loads(res.data)
        result = self.client().get('/entries/{}'.format(json_result['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('random entry', str(res.data))


    def test_entry_delete(self):
        res = self.client().post('/entry', data=self.entry)
        self.assertEqual(res.status_code, 201)
        json_result = json.loads(res.data)
        
        self.client().delete('/entries/{}'.format(json_result['id']))
        result = self.client().get('/entries/{}'.format(json_result['id']))
        self.assertEqual(result.status_code,404)

    def test_get_all_entries(self):
        res = self.client().post('/entries', data=self.entry)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.status_code, 200)
        self.assertIn('random entry', str(res.data))

if __name__ == "__main__":
    unittest.main()