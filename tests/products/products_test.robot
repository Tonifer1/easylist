*** Settings ***
Library        RequestsLibrary
Library        Collections
Resource       ../login/login_keyword_test.robot


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
    ${response}=    GET On Session    prod    ${PRODUCTS_ENDPOINT}    expected_status=401
    Should Be Equal As Integers    ${response.status_code}    401
    Log    ${response.status_code}
    Log    Tarkistettu: API vaatii tokenin.

Hae Tuotteet Ja Tarkista Sisältö
    ${token}=    Kirjaudu Ja Hae Token
    Create Session    getprod    ${BASE_URL}
    ${headers}=    Create Dictionary    Authorization=Bearer ${token}
    ${response}=    GET On Session    getprod    ${PRODUCTS_ENDPOINT}    headers=${headers}
    Log To Console    Statuscode: ${response}
    ${json}=    Set Variable    ${response.json()}
    ${maara}=    Get Length    ${json}
    Should Be True    ${maara} > 0
    Log To Console    Tuotteiden haku onnistui, tuotteita löytyi: ${maara}

Tarkista Että Ensimmäisellä Tuotteella On Nimi
    ${token}=    Kirjaudu Ja Hae Token
    Create Session    getfirstprod    ${BASE_URL}
    ${headers}=    Create Dictionary    Authorization=Bearer ${token}
    ${response}=    GET On Session    getfirstprod    ${PRODUCTS_ENDPOINT}    headers=${headers}
    ${tuotteet}=    Set Variable    ${response.json()}
    

    ${eka}=    Get From List    ${tuotteet}    0

    ${nimi}=    Get From Dictionary    ${eka}    product_name
    Should Not Be Empty    ${nimi}
    Log To Console    Ensimmäisen tuotteen nimi: ${nimi}

Tarkista Että Product_Id On Kokonaisluku
    ${token}=    Kirjaudu Ja Hae Token
    Create Session    sessionid    ${BASE_URL}
    ${headers}=    Create Dictionary    Authorization=Bearer ${token}
    ${response}=    GET On Session    sessionid    ${PRODUCTS_ENDPOINT}    headers=${headers}
    ${tuotteet}=    Set Variable    ${response.json()}
    ${eka}=    Get From List    ${tuotteet}    0
    ${id}=    Get From Dictionary    ${eka}    product_id
    ${is_int}=    Evaluate    isinstance(${id}, int)
    Should Be True    ${is_int}






