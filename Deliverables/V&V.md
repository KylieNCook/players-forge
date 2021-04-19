# D.7 - Verification & Validation

Group 08 - PlayersForge\
Group Members: Kylie Cook, Fernando Diaz, David Hermann, Jared McNeece, Conrad Murphy, Noah Olono

## 1. Description

## 2. Verification (tests)

  ### 2.1 Unit Test

  #### 2.1.1 
  The test framework used to develop the unit tests was unittest.

  #### 2.1.2
  Automated Unit Tests [Location](https://github.com/KylieNCook/players-forge/blob/main/playersforge/tests.py)

  ### 2.1.3
  [Test Case](https://github.com/KylieNCook/players-forge/blob/main/playersforge/tests.py#L18) that makes use of mock objects\
  [Class](https://github.com/KylieNCook/players-forge/blob/main/playersforge/app.py#L12) being tested

  ### 2.1.4
  Tests and Coverage:\
  ![image](https://user-images.githubusercontent.com/78190024/115133848-16ccf480-9fc0-11eb-8114-ab0accbb4c50.png)

  ### 2.2 Integration Test
  
  ### 2.2.1
  The test framework used to develop the integration tests was unittest.
  
  ### 2.2.2
  Automated Integration Tests [Location](https://github.com/KylieNCook/players-forge/blob/main/playersforge/tests.py)
  
  ### 2.2.3
  [Integration Test](https://github.com/KylieNCook/players-forge/blob/main/playersforge/tests.py#L138)\
  The test_integration_signup() method puts together three different components. First,  we rediret to the signup page. The signup component is initiated, and a user signs up 
  with the email 'someone', username 'someone', and password 'someone'. Then, we check to make sure that the page was redirected to the 
  user's new profile page after posting (since the user automatically gets logged in after signing up).
  Then, we get the upload page from the user's profile page (the user wouldn't be able to get into the profile or upload page if they were not signed up/logged in.
  We then post a new mod to upload and check to make sure that it redirects to the same page, which means it was successful. After that, we get the logout page,
  which automatically logs the user out and redirects them to the main home page.
  
  ### 2.2.4
  ![image](https://user-images.githubusercontent.com/78190024/115135263-22261d00-9fcc-11eb-9a48-4a1720898073.png)

  ### 2.3 Acceptance
  
  ### 2.3.1
  The test framework used to develop the acceptance tests was Selenium.
  
  ### 2.3.2
  Automated Acceptance Tests [Location](https://github.com/KylieNCook/players-forge/blob/main/playersforge/selenium.py)
  
  ### 2.3.3
  [Acceptance Test](https://github.com/KylieNCook/players-forge/blob/main/playersforge/selenium.py#L41)\
  The test_signup() method brings up the local address that PlayersForge ran on and starts at the homepage. The Selenium bot then clicks the 'Login' section, which brings
  it to the login page, then clicks the 'Sign up' section, which brings it to the sign up page. Once the bot is at the sign up page, the bot enters an email, username, and  password, then clicks submit. After that, the bot is brought to its new profile page.
  ### 2.3.4
  ![image](https://user-images.githubusercontent.com/78190024/115175690-4e02da80-a080-11eb-9080-4bb380cad015.png)
  [Video of acceptance tests](https://youtu.be/nECknGIuEV8)
  
## 3. Validation

  ### Script
  - How do you like the design of PlayersForge?
  - Move around each page, do you like the designs of the other pages?
  - View and download a mod from the Homepage/Featured Mods page. How do you feel about the process?
  - Is there something that you would change about the process?
  - Try making an account with PlayersForge. Was it difficult to find the signup page?
  - If so, how and what would you change?
  - Upload a fake mod. How did you feel about this process?
  - If you could change certain aspects of the current website, what would you do?
  - How would you rate the website from 1-10 and why?
 
  ### Results
  #### Myles Abril
  - How do you like the design of PlayersForge?\
  I like it! I like the colors, the layout, the logo is okay. Everything is visible and easy to read. Nothing seems out of place.
  - Move around each page, do you like the designs of the other pages?\
  Yes, I really like it, everything is very user friendly. I really like the shadows. There is empty space on the mods page but I'm sure you could put graphics in those areas if you kept working on it.
  - View and download a mod from the Homepage/Featured Mods page. How do you feel about the process?\
  Very easy, painless, and pretty nifty.
  - Is there something that you would change about the process?\
  Maybe links for mod information, more description, or videos of the mod. It'd be cool to be able to move through multiple pictures for a mod.
  - Try making an account with PlayersForge. Was it difficult to find the signup page?\
  It's very easy to find the signup page.
  - If so, how and what would you change?\
  N/A
  - Upload a fake mod. How did you feel about this process?\
  It was seamless, smooth, and very easy. I would make it fo to the users profile immediately after uploading a mod. I would also have it preview the mode before publishing.
  - If you could change certain aspects of the current website, what would you do?\
  Maybe have a games section.
  - How would you rate the website from 1-10 and why?\
  I would rate it as a 10 because it's really cool and it's different from other websites. It is very inviting and makes me wana download stuff. It makes me happy before I destroy my games with all the mods I download.
  
  ### Reflections
  
  #### Myles Abril
  After the user evaluation with Myles, I came to a conclusion that the main changes of the website that could pull in users are more features. Myles thoroughly enjoyed the design of the website, and mainly brought up some additions to the uploading process and the overall website. It seemed as though the website was easy to navigate, and pleasing to look at. Myles performed each task as expected, though, he is an avid gamer and has experience in using previous modding websites, which could have given him an advantage.
