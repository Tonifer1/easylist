*** Settings ***
Library           RequestsLibrary
Library           Collections
Resource          login_keyword_test.robot

*** Variables ***
${BASE_URL}       http://127.0.0.1:8000
${LOGIN_ENDPOINT}    /api/token/
${PRODUCTS_ENDPOINT}    /api/products/
      



*** Test Cases ***

Hae tuotteet
    [Documentation]    Testaa tuotteiden hakemista
    ${token}=    Kirjaudu Ja Hae Token
    Create Session    prod    ${BASE_URL}
    ${headers}=    Create Dictionary    Authorization=Bearer ${token}
    ${response}=   GET On Session    prod    ${PRODUCTS_ENDPOINT}    headers=${headers}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}
Ei tokenia
    [Documentation]    Testaa tuotteiden hakemista ilman kirjautumista ja tokenia
    Create Session    prod    ${BASE_URL}
    Run Keyword And Expect Error    *401*    GET On Session    prod    ${PRODUCTS_ENDPOINT}
    Log    Tarkistettu: API vaatii tokenin.

