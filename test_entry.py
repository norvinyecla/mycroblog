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
        result1 = self.client().post('/entry', data=self.entry)
        self.assertEqual(result1.status_code, 201)
        json_result1 = json.loads(result1.data)

        result2 = self.client().get('/entry/{}'.format(json_result1['id']))
        json_result2 = json.loads(result2.data)
        self.assertIn(str(json_result1['text']), str(json_result2['text']))
        self.assertEqual(str(json_result1['id']), str(json_result2['id']))


    def test_entry_delete(self):
        res = self.client().post('/entry', data=self.entry)
        self.assertEqual(res.status_code, 201)
        json_result = json.loads(res.data)
        
        self.client().delete('/entry/{}'.format(json_result['id']))
        result2 = self.client().get('/entry/{}'.format(json_result['id']))
        self.assertEqual(result2.status_code, 404)


    def test_get_all_entries(self):
        res = self.client().post('/entry', data=self.entry)
        self.assertEqual(res.status_code, 201)
        self.assertIn('random entry', str(res.data))

        res = self.client().get('/entries')
        self.assertEqual(res.status_code, 200)
        self.assertIn('random entry', str(res.data))


if __name__ == "__main__":
    unittest.main()