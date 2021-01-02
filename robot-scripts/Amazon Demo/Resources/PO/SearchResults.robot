*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Verify Search completed
    Wait Until Page Contains  results for "${SEARCH_TERM}"

Click Product Link
    [Documentation]  Clicks on the first product in the search results.
    Click Link  xpath=//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[1]/div/span/div/div/div/div/div[2]/h2/a

