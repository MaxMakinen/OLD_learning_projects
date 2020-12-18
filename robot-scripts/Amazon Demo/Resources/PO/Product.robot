*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Verify Page loaded
    Wait Until Page Contains  Back to results

Add To Cart
        Click Button  id=add-to-cart-button