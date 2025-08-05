*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}       http://127.0.0.1:8000
${LOGIN_ENDPOINT}    /api/token/


*** Test Cases ***


Kirjaudu Väärillä Tunnuksilla
    [Documentation]    Kirjautuu API:iin väärillä tunnuksilla ja palauttaa 401
    Create Session    auth    ${BASE_URL}
    ${data}=    Create Dictionary    username=vaara    password=vaara
    Run Keyword And Expect Error    *401*    POST On Session    auth    ${LOGIN_ENDPOINT}    json=${data}

Kirjaudu Ilman Tunnuksia
    [Documentation]    Kirjautuu API:iin ilman  tunnuksia ja palauttaa 401 tai 404
    Create Session    auth    ${BASE_URL}
    ${data}=    Create Dictionary    username    password
    Run Keyword And Expect Error    *Client Error*    POST On Session    auth    ${LOGIN_ENDPOINT}    json=${data}

Virheellinen Kirjautuminen Ja Virheilmoitus
    [Documentation]    Testaa että API palauttaa oikean virheilmoituksen väärillä tunnuksilla
    Create Session    auth    ${BASE_URL}
    ${data}=    Create Dictionary    username=väärä    password=väärä
    
    ${response}=    Post On Session    auth    ${LOGIN_ENDPOINT}    json=${data}    expected_status=ANY

    Log    ${response.status_code}
    Log    ${response.text}

    Should Be Equal As Numbers    ${response.status_code}    401

    ${json}=    Evaluate    json.loads('''${response.text}''')    modules=json
    ${detail}=  Get From Dictionary    ${json}    detail

    Should Contain    ${json['detail']}    No active account found with the given credentials




    
