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
  ### 2.3.2
  ### 2.3.3
  ### 2.3.4
  
## 3. Validation

  ### Script
  ### Results
  ### Reflections
