*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}       http://127.0.0.1:8000
${LOGIN_ENDPOINT}    /api/token/
${USERNAME}       teppo
${PASSWORD}       testaaja


*** Keywords ***
Kirjaudu Ja Hae Token
    [Documentation]    Kirjautuu API:iin ja palauttaa access-tokenin
    Create Session    auth    ${BASE_URL}
    ${data}=    Create Dictionary    username=${USERNAME}    password=${PASSWORD}
    ${response}=    POST On Session    auth    ${LOGIN_ENDPOINT}    json=${data}
    Should Be Equal As Numbers    ${response.status_code}    200
    ${json}=    Evaluate    json.loads('''${response.text}''')    modules=json
    ${ACCESTOKEN}=    Get From Dictionary    ${json}    access
    RETURN    ${ACCESTOKEN}



    