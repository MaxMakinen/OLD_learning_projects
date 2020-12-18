*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Verify Product Added
    Wait Until Page Contains  Added to Cart

Proceed To Checkout
    [Documentation]  first clicks on cart link in top right of page to ensure the "proceed to checkout" can be clicked
    Click Link  /gp/cart/view.html?ref_=nav_cart
    Click Button  Proceed to checkout