# TestAutomation
Please find here the test automation exercises: 
- Exercise 1 is a UI Automation: Using chrome webdriver we navigate to the page https://automationintesting.online/#/admin. we login with admin/password. 
The first room is creating, and we click on the creating room, next we come back to the previous page where we create second room with more features. Then we click on the second room when it is correctly created. Finally, we close and quit the webdriver.
this script is written in Python.
* Exercise 2 is aimed to automate an API call. We send a GET request to https://jsonplaceholder.typicode.com/todos/ and assert if the response is OK (status code is 200). Then we get the Json array, and we iterate the Json array to find the elements with id 5. We verify that the field completed is false for the first id: 5. If not, we receive a message. It is a Python script.
