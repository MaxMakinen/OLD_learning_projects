*** Settings ***
Resource  ../Resources/PO/LandingPage.robot
Resource  ../Resources/PO/SearchResults.robot
Resource  ../Resources/PO/TopNav.robot
Resource  ../Resources/PO/Cart.robot
Resource  ../Resources/PO/Product.robot
Resource  ../Resources/PO/SignIn.robot
Resource  ../Resources/Common.robot

*** Keywords ***
Search for Products
    LandingPage.Load
    LandingPage.Verify Page Loaded
    TopNav.Search For Products
    SearchResults.Verify Search Completed
Select product from Search Results
    SearchResults.ClickProduct Link
    Product.Verify Page Loaded
Add Product to Cart
    Product.Add To Cart
    Cart.Verify Product Added
Begin Checkout
    Cart.Proceed To Checkout
    SignIn.Verify Page Loaded