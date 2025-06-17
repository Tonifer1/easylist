*** Settings ***
Library           RequestsLibrary

*** Variables ***
${BASE_URL}       http://127.0.0.1:8000
${LOGIN_ENDPOINT}    /api/token/
${USERNAME}       teppo
${PASSWORD}       testaaja
${INVALIDUSERNAME}       invalidname
${INVALIDPASSWORD}       invalidpassword

*** Test Cases ***
Hae JWT Token
    [Documentation]    Testaa kirjautumista ja access-tokenin saamista
    Create Session    auth    ${BASE_URL}
    ${data}=    Create Dictionary    username=${USERNAME}    password=${PASSWORD}
    ${response}=    POST On Session    auth    ${LOGIN_ENDPOINT}    json=${data}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}

Kirjaudu Väärillä Tunnuksilla
    [Documentation]    Kirjautuu API:iin väärillä tunnuksilla ja palauttaa 401
    Create Session    auth    ${BASE_URL}
    ${data}=    Create Dictionary    username=${INVALIDUSERNAME}    password=${INVALIDPASSWORD}
    Run Keyword And Expect Error    *401*    POST On Session    auth    ${LOGIN_ENDPOINT}    json=${data}



    
