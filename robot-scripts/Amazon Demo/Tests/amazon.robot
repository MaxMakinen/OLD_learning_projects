*** Settings ***
Documentation  This is some basic info about the whole suite
Resource  ../Resources/AmazonApp.robot
Test Setup  Begin web test
Test Teardown  End web test

*** Variables ***
${BROWSER} =  ie
${START_URL} =  http://www.amazon.com
${SEARCH_TERM} =  teddy bear

*** Test Cases ***
Logged out user must sign in to check out
    [Documentation]  This test loads the amazon.com page, looks for a product and tries to check out. Once it verifies a sign in page it ends the tests.

    [Tags]  Smoke
    Search for Products
    Select product from Search Results
    Add Product to Cart
    Begin Checkout