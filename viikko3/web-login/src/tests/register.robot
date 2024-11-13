*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle234
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation dont match

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username should be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle1
    Set Password Confirmation  kalle1
    Submit Credentials
    Register Should Fail With Message  Password should be atleast 8 characters long

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  abcdfeghjikl
    Set Password Confirmation  abcdfeghjikl
    Submit Credentials
    Register Should Fail With Message  Password must not consist only of letters

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
