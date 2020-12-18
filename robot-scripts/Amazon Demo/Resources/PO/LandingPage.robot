*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Load
    Go To  http://www.amazon.com

Verify Page Loaded
    Wait Until Page Contains  Today's Deals
