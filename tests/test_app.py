import tempfile,unittest
from pathlib import Path
from app import scan
class HygieneTests(unittest.TestCase):
 def test_private_key_marker_detected(self):
  with tempfile.TemporaryDirectory() as d:
   (Path(d)/"sample.txt").write_text("-----BEGIN PRIVATE KEY-----")
   self.assertEqual(scan(d)[0]["rule"],"private-key-marker")
 def test_safe_file_no_findings(self):
  with tempfile.TemporaryDirectory() as d:
   (Path(d)/"sample.py").write_text("print('hello')")
   self.assertEqual(scan(d),[])
 def test_non_directory_rejected(self):
  with self.assertRaises(ValueError): scan("nonexistent-repository-root-123")
if __name__=="__main__": unittest.main()
