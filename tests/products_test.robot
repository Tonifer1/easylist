*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}       http://127.0.0.1:8000
${LOGIN_ENDPOINT}    /api/token/
${USERNAME}       teppo
${PASSWORD}       testaaja
${PRODUCTS_ENDPOINT}    /api/products/
${PRODUCTS}       tuotteet
${ACCESTOKEN}        



*** Test Cases ***
Hae JWT Token
    [Documentation]    Testaa kirjautumista ja access-tokenin saamista 
    Create Session    auth    ${BASE_URL}
    ${data}=    Create Dictionary    username=${USERNAME}    password=${PASSWORD}
    ${response}=    POST On Session    auth    ${LOGIN_ENDPOINT}    json=${data}
    Should Be Equal As Numbers    ${response.status_code}    200
    ${json}=    Evaluate    json.loads('''${response.text}''')    modules=json
    ${ACCESTOKEN}=    Get From Dictionary    ${json}    access
    Set Suite Variable    ${ACCESTOKEN}
    Log    Token: ${ACCESTOKEN}
    Log    ${response.json()}
Hae tuotteet
    [Documentation]    Testaa tuotteiden hakemista
    Create Session    prod    ${BASE_URL}
    ${headers}=    Create Dictionary    Authorization=Bearer ${ACCESTOKEN}
    ${response}=   GET On Session    prod    ${PRODUCTS_ENDPOINT}    headers=${headers}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}
Ei tokenia
    [Documentation]    Testaa tuotteiden hakemista ilman kirjautumista ja tokenia
    Create Session    prod    ${BASE_URL}
    ${response}=   GET On Session    prod    ${PRODUCTS_ENDPOINT}    
    Should Be Equal As Numbers    ${response.status_code}    401
    Log    ${response.json()}