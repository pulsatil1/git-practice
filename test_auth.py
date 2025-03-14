# Tests for auth module
import unittest
from auth import login, logout

class TestAuth(unittest.TestCase):
    def test_login_success(self):
        """Test successful login"""
        self.assertTrue(login("testuser", "correct_password"))
        
    def test_logout(self):
        """Test logout functionality"""
        self.assertTrue(logout("testuser"))
        
if __name__ == "__main__":
    unittest.main()
