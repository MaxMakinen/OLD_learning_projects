*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Verify Page Loaded
    Look For SignIn Element
    Verify Element Content

Look For SignIn Element
    Page Should Contain Element  //*[@id="authportal-main-section"]/div[2]/div/div[1]/form/div/div/div/h1

Verify Element Content
    [Documentation]  Element should contain the words "Sing-In".
    Element Text Should Be  //*[@id="authportal-main-section"]/div[2]/div/div[1]/form/div/div/div/h1  Sign-In
