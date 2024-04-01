import unittest
import urllib.request

class TestAtgWorldConnection(unittest.TestCase):
    
    def test_website_connection(self):
        url = "https://atg.world"
        
        # Step 1: Attempting to connect to the website
        print("Step 1: Connecting to the website...")
        try:
            response = urllib.request.urlopen(url)
            status_code = response.getcode()
            print(f"Status Code: {status_code}")
            
            # Step 2: Checking if the website loaded successfully
            if status_code == 200:
                print("Step 2: Website loaded successfully!")
                self.assertTrue(True)  # Asserting that the website loaded successfully
            else:
                print("Step 2: Website failed to load.")
                self.assertTrue(False)  # Failing the test as website failed to load
        
        # Step 3: Handling connection errors
        except urllib.error.URLError as e:
            print("Step 3: Connection error occurred.")
            print(f"Error: {e}")
            self.assertTrue(False)  # Failing the test due to connection error

if __name__ == '__main__':
    unittest.main()
