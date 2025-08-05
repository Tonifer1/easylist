*** Settings ***
Library     RequestsLibrary
Resource    ../login/login_keyword_test.robot


*** Variables ***
${BASE_URL}       http://127.0.0.1:8000
${PRODUCTS_ENDPOINT}    /api/products/

*** Test Cases ***
Hae tuotteet suodatuksella
    ${token}=    Kirjaudu Ja Hae Token
    Create Session    prod    ${BASE_URL}
    ${headers}=    Create Dictionary    Authorization=Bearer ${token}
    ${params}=     Create Dictionary    productname=Omena
    ${response}=   GET On Session    prod    ${PRODUCTS_ENDPOINT}   params=${params}    headers=${headers}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}
