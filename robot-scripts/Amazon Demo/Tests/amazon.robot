*** Settings ***
Documentation  This is some basic info about the whole suite
Resource  ../Resources/Amazon.robot
Test Setup  Begin web test
Test Teardown  End web test

*** Variables ***


*** Test Cases ***
User must sign in to check out
    [Documentation]  This test loads the amazon.com page, looks for a product and tries to check out. Once it verifies a sign in page it ends the tests.

    [Tags]  Smoke
    Amazon.Search for Products
    Amazon.Select product from Search Results
    Amazon.Add Product to Cart
    Amazon.Begin Checkout