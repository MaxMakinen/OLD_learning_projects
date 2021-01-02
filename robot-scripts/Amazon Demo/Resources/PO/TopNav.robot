*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Search For Products
    Enter Search Term
    Submit Search

Enter Search Term
    Input Text  id=twotabsearchtextbox  ${SEARCH_TERM}

Submit Search
    [Documentation]  Clicks the search button
    Click Button  xpath=//*[@id="nav-search-submit-text"]/input