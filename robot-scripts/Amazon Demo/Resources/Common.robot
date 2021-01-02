*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Begin web test
    log  ${BROWSER}
    Open Browser  about:blank  ${BROWSER}

End web test
    Close Browser