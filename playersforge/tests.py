import unittest
from app import app
from unittest import mock
import io
from io import StringIO, BytesIO

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass 

    # test that the index page loads correctly
    def test_index(self):
        tester = app.test_client(self)
        mock_response = mock.Mock()
        mock_response.status_code = 200
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, mock_response.status_code)
        print("\n SUCCESSFUL INDEX PAGE TEST ")

    # test that the mods page laods correctly
    def test_mods(self):
        tester = app.test_client(self)
        response = tester.get('/mods', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL MOD PAGE TEST ")

    # test that the forums page loads correctly
    def test_forums(self):
        tester = app.test_client(self)
        response = tester.get('/forums', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL FORUMS PAGE TEST ")

    # test that the sign up page loads correctly
    def test_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertTrue(b'Sign Up' in response.data)
        print("\n SUCCESSFUL SIGNUP PAGE TEST ")

    # test that adds a user called 'admin'
    def test_correct_signup(self):
        tester = app.test_client(self)
        response = tester.post(
            '/signup',
            data=dict(email="admin", username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'Hi there, admin!', response.data)
        print("\n SUCCESSFUL CORRECT SIGNUP TEST ")

    # test that the login page loads correctly
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Want to sign up instead?' in response.data)
        print("\n SUCCESSFUL LOGIN PAGE TEST ")

    # test that a person can log in correctly
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(email="tom@gmail.com", password="tom"),
            follow_redirects=True
        )
        self.assertIn(b'Hi there, tom!', response.data)
        print("\n SUCCESSFUL CORRECT LOGIN TEST ")

    # test that a person with wrong credentials does not get logged in
    def test_wrong_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(email="notadmin", password="notadmin"),
            follow_redirects=True
        )
        self.assertTrue(b"I can't find those credentials", response.data)
        print("\n SUCCESSFUL WRONG LOGIN TEST ")

    # test that the profile page works after someone logs in
    def test_profile(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(email="tom@gmail.com", password="tom"),
            follow_redirects=True
        )
        response = tester.get('/profile', content_type='html/text')
        self.assertTrue(b'Hi there, tom!' in response.data)
        print("\n SUCCESSFUL PROFILE PAGE TEST ")

    def test_logout(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(email="tom@gmail.com", password="tom"),
            follow_redirects=True
        )
        repsonse = tester.get('/logout', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL LOGOUT TEST ")

    # test that the upload page loads correctly after someone logs in
    def test_upload(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(email="tom@gmail.com", password="tom"),
            follow_redirects=True
        )
        response = tester.get('/upload', content_type='html/text')
        self.assertTrue(b'Upload' in response.data)
        print("\n SUCCESSFUL UPLOAD PAGE TEST ")

    def test_correct_upload(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(email="tom@gmail.com", password="tom"),
            follow_redirects=True
        )
        response = tester.post(
            '/upload',
            data=dict(name="name", description="description", game="game",
            inputFile=(BytesIO(b'my file contents'), 'test.txt'), imageFile=(BytesIO(b'Some stuff'), 'image.img')),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL MOD UPLOAD TEST ")

    def test_integration_signup(self):
        tester = app.test_client(self)

        response = tester.get('/signup', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST SIGN UP REDIRECT ")

        response = tester.post(
            '/signup',
            data=dict(email="someone", username="someone", password="someone"),
            follow_redirects=True
        )
        self.assertIn(b'Hi there, someone!', response.data)
        print("\n SUCCESSFUL INTEGRATION TEST SIGN UP ")

        repsonse = tester.get('/upload', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST UPLOAD REDIRECT ")

        response = tester.post(
            '/upload',
            data=dict(name="aname", description="adescription", game="agame",
            inputFile=(BytesIO(b'my file contents'), 'test.txt'), imageFile=(BytesIO(b'Some stuff'), 'image.img')),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST MOD UPLOAD ")

        repsonse = tester.get('/logout', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST LOGOUT ")

    def test_integration_login(self):
        tester = app.test_client(self)

        response = tester.get('/', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST HOMEPAGE REDIRECT ")

        response = tester.get('/mods', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST MODS REDIRECT ")

        response = tester.get('/forums', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST FORUMS REDIRECT ")

        response = tester.post(
            '/login',
            data=dict(email="joe@gmail.con", password="joe"),
            follow_redirects=True
        )
        self.assertTrue(b"I can't find those credentials", response.data)
        print("\n SUCCESSFUL INTEGRATION TEST WRONG LOGIN ")

        response = tester.post(
            '/login',
            data=dict(email="joe@gmail.com", password="joe"),
            follow_redirects=True
        )
        self.assertIn(b'Hi there, joe!', response.data)
        print("\n SUCCESSFUL INTEGRATION TEST LOGIN ")

        response = tester.post(
            '/upload',
            data=dict(name="aname", description="adescription", game="agame",
            inputFile=(BytesIO(b'my file contents'), 'test.txt'), imageFile=(BytesIO(b'Some stuff'), 'image.img')),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST MOD UPLOAD ")

        repsonse = tester.get('/logout', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("\n SUCCESSFUL INTEGRATION TEST LOGOUT ")


if __name__ == '__main__':
    unittest.main()